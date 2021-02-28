from config import config
from s3_storage import AWSS3Storage

class Storage:

    def __init__(self) -> None:
        pass

    def disk(self, disk_name: str='s3'):
        if disk_name == 's3':
            return AWSS3Storage(config.AWS_BUCKET_NAME)
        else:
            raise Exception('Storage provider is not support!')
    
    # def collections(self):
    #     return self.disk.collections()

    # def upload_image(self, file_path, collection_name):
    #     return self.disk.put_image(file_path, collection_name)

    # def upload_file(self, file_path, collection_name):
    #         return self.disk.put_file(file_path, collection_name)