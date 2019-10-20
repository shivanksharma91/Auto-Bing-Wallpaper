#copy files from windows folder to new location
#change the file extension
#Set wallpaper
#add new file everyday
    #compare from yestrday, if today then add else not add

if __name__ == '__main__':
    import shutil
    import os
    import Copy_Rename as cr
    from PIL import Image
    w_wallpaper = "C:/Users/Shivank/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
    dest= "C:/Users/Shivank/Pictures/Windows Wallpapers"
    try:
        cr.copyrename(w_wallpaper,dest)
    except:
        shutil.rmtree(dest)
        cr.copyrename(w_wallpaper,dest)

    for img in os.listdir(dest):
        print(cr.img_resolution(img))
else:
    print("Run Wallpaper.py")




