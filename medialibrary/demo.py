from storage import Storage

print('List all resources')
store = Storage()
collections = store.collections()
print(collections)

print('Upload a image')
file_path = '/home/quanvu/Pictures/6bb3b4abbd7f3e582699844c9d386df8.jpg'
collection_name = 'pyworks-asia-static'
file_uploaded = store.upload_image(file_path=file_path, collection_name=collection_name)
print(file_uploaded)


print('Upload a file')
file_path = '/home/quanvu/Documents/hero.mp4'
collection_name = 'pyworks-asia-static'
file_uploaded = store.upload_file(file_path=file_path, collection_name=collection_name)
print(file_uploaded)


