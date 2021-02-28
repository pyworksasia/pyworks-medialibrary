from medialibrary.interfaces import StorageInterface
from medialibrary.storage import Storage
from medialibrary.s3_storage import AWSS3Storage


class TestInterfaces:

    def test_is_storage(self):
        print('Create new storage')
        store = Storage.disk('s3')
        assert isinstance(store, AWSS3Storage) 

