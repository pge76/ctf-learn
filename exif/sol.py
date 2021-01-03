from exif import Image

with open('Computer-Password-Security-Hacker.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    #print(my_image.has_exif)
    print(my_image.camera_owner_name)