from medialibrary.storage import Storage


class TestStorage:

    def test_put_image(self):
        store = Storage.disk('s3')
        file_path = '/home/quanvu/Pictures/avatar-1.jpg'
        uploaded_link = store.put_image(file_path=file_path)
        assert 's3.amazonaws.com' in  uploaded_link
        assert 'avatar-1.jpg' in  uploaded_link




# print('Upload a image')


# print('Upload a file')
# file_path = '/home/quanvu/Documents/hero.mp4'
# collection_name = 'pyworks-asia-static'
# file_puted = store.put_file(file_path=file_path, collection_name=collection_name)
# print(file_puted)
