from storage import Storage

print('Create new storage')
store = Storage.disk('s3')

print('Upload a image')
file_path = '/home/quanvu/Pictures/avatar-1.jpg'
file_uploaded = store.put_image(file_path=file_path)
print(file_uploaded)


# print('Upload a file')
# file_path = '/home/quanvu/Documents/hero.mp4'
# collection_name = 'pyworks-asia-static'
# file_puted = store.put_file(file_path=file_path, collection_name=collection_name)
# print(file_puted)


