# from settings import logger, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, S3_REGION, S3_MARKETING_SC, S3_TAG
# from botocore.exceptions import NoCredentialsError
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import base64
import six
import uuid
import imghdr
import io
import aioboto3


class S3ImageRepository(BaseRespository):
    def __init__(self):
        pass

    def __get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension

    def __decode_base64_file(self, data):
        """
        Fuction to convert base 64 to readable IO bytes and auto-generate file name with extension
        :param data: base64 file input
        :return: tuple containing IO bytes file and filename
        """
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                TypeError('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.__get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            return io.BytesIO(decoded_file), complete_file_name

    async def upload_image_to_aws(self, data_url: str) -> str:
        logger.info("upload_image_to_aws")
        file_type = data_url.split(";")[0].split("image/")[1]
        img = Image.open(urlopen(data_url))
        width, height = img.size
        basewidth = 800
        if width > basewidth:
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img_resize = img.resize((basewidth, hsize), Image.ANTIALIAS)
            buffer = io.BytesIO()
            img_resize.save(buffer, file_type)
            myimage = buffer.getvalue()
            file, file_name = (
                self.__decode_base64_file("data:image/jpeg;base64," + base64.b64encode(
                    myimage).decode()))
        else:
            file, file_name = self.__decode_base64_file(data_url)

        async with aioboto3.client(
                "s3",
                aws_access_key_id=S3_ACCESS_KEY_ID,
                aws_secret_access_key=S3_SECRET_ACCESS_KEY,
                region_name=S3_REGION) as s3:
            try:
                await s3.upload_fileobj(
                    file, f"{S3_MARKETING_SC}", f"{S3_TAG}/{file_name}",
                    ExtraArgs={
                        'ACL': 'public-read',
                        'ContentType': data_url.split(";")[0].split(":")[1]
                    }
                )
                logger.info("upload image to S3 successful.")

                return (f"https://{S3_MARKETING_SC}.s3-{S3_REGION}"
                        f".amazonaws.com/{S3_TAG}/{file_name}")

            except FileNotFoundError:
                logger.info("Can't upload image to S3! : The file was not found")
                raise Exception
            except NoCredentialsError:
                logger.info("Can't upload image to S3! : Credentials not available")
                raise Exception
            except Exception:
                logger.info("Can't upload image to S3! : Something went wrong")
                raise Exception