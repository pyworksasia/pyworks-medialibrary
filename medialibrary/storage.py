import uuid
import boto3
from os.path import basename
from config import config


class AWSS3Storage:

    def __init__(self) -> None:
        self.s3 = boto3.resource('s3')
        
    def collections(self):
        collections = []
        for bucket in self.s3.buckets.all():
            collections.append(bucket.name)
        return collections

    def put_image(self, file_path, bucket_name):
        file_content = open(file_path, 'rb')
        file_name = basename(file_path)
        # self.s3.Bucket(bucket_name).upload_file(
        #     Filename=file_path,
        #     Key=file_name,
        #     ExtraArgs={'ACL': 'public-read'}
        # )
        self.s3.Bucket(bucket_name).upload_fileobj(
            Fileobj=file_content,
            Key=file_name,
            ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/jpeg'}
        )
        # self.s3.Bucket(bucket_name).put_object(
        #     Body=file_content,
        #     Key=file_name
        # )
        s3_url = self.get_url(bucket_name, file_name=file_name)
        return s3_url
        
    def put_file(self, file_path, bucket_name):
        file_name = basename(file_path)
        self.s3.Bucket(bucket_name).upload_file(
            Filename=file_path,
            Key=file_name,
            ExtraArgs={'ACL': 'public-read'}
        )
        # self.s3.Bucket(bucket_name).put_object(
        #     Body=file_content,
        #     Key=file_name
        # )
        s3_url = self.get_url(bucket_name, file_name=file_name)
        return s3_url
        

    def get_url(self, bucket_name, file_name):
        return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

class Storage:

    def __init__(self, provider: str='s3') -> None:
        self.provider = provider
        self.storage = self._get_storage()

    def _get_storage(self):
        if self.provider == 's3':
            return AWSS3Storage()
        else:
            raise Exception('Storage provider is not support!')
    
    def collections(self):
        return self.storage.collections()

    def upload_image(self, file_path, collection_name):
        return self.storage.put_image(file_path, collection_name)

    def upload_file(self, file_path, collection_name):
            return self.storage.put_file(file_path, collection_name)