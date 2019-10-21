# Auto-Bing-Wallpaper

Whenever i started a windows 10 machine, i wasw always greeted with a beautiful wallpaper of some landscape, animal, location etc. I wanted to use the same images as my desktop's wallpaper.

These images are provided by Microsoft Bing but they are noe easily available over the internet, plus i wanted to automate this task.

On doing a bit of googling i founnd out the location where windows is storing these files. But on looking in that location i found out that it does not contained these beautiful wallpapers but also some random stuff, moreover, non of these files were having a ".jpg" extension.

So to automate it using Python, i wanted the script to fulfill the following tasks:
  1. Copy the folder to a specific location.
  2. Add .jpg extension to all the files.
  3. Keep files only greater than 300 kb
  4. Keep only image files whose resolution is  1080 x 1920
  5. Repeat the above steps everytime i log on. (For getting fresh stock of images)
