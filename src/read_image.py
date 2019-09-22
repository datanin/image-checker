import os
import shutil
from PIL import Image, ExifTags

photo_dir = "/home/jd/Nextcloud/Photos/"

file_list = os.listdir(photo_dir)

for file in file_list:
    if file.lower().endswith(".jpg"):
        print(file)
        img = Image.open(photo_dir + file)
        try:
            exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
            file_new = exif["DateTimeOriginal"].replace(":", "")
            file_new = file_new.replace(" ", "_") + ".jpg"
            os.rename(photo_dir+file, photo_dir+file_new)
            print("Old: {} > New: {}".format(file, file_new))
        except:
            print("Error @{}".format(file))
            shutil.move(photo_dir+file, "/home/jd/Nextcloud/Photos/00_rest/"+file)