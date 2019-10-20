import shutil
import os

def copyrename(w_wallpaper,dest):
    shutil.copytree(w_wallpaper,dest) 
    folder_images = os.listdir(dest) # Returns list of images in the folder
    for files in folder_images:
        filename=os.path.join(dest,files)
        if not os.path.getsize(filename) <(300*1024):
            name,ext= os.path.splitext(files)
            #print(name)
            #print(ext)
            filename=os.path.join(dest,name)
            filename=os.path.normpath(filename)
            #print(filename)
            os.rename(filename,filename +".jpg")
        else:
            os.remove(filename)
    wallpapers = len(os.listdir(dest))        
    return print("{} wallpapers copied to {}".format(wallpapers,dest) )

def img_resolution(image):
    with open(image, 'rb') as img_file:
        img_file.seek(163)

        a = img_file.read(2)

        height = (a[0]<<8) + a[1]
        a= img_file.read(2)

        width = (a[0]<<8)+a[1]

    return width, height
    
