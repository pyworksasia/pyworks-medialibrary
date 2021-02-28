from os import path
from interfaces import StorageInterface

class Storage(StorageInterface):

    def __init__(self, provider: str='s3') -> None:
        self.provider = provider
        self.storage = self._get_storage()

    def disk(self, path: str, file_name: str):
        """Load disk"""
        print("Load disk")

    def _get_storage(self):
        if self.provider == 's3':
            return None
        else:
            raise Exception('Storage provider is not support!')
    
    def collections(self):
        return self.storage.collections()

    def upload_image(self, file_path, collection_name):
        return self.storage.put_image(file_path, collection_name)

    def upload_file(self, file_path, collection_name):
            return self.storage.put_file(file_path, collection_name)

print('List all resources')
store = Storage()
store.disk(path='', file_name='')
# collections = store.collections()
# print(collections)
