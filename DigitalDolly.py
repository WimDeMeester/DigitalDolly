from PIL import Image
import os
from _hotshot import resolution

# The directory where all the images for the timelapse are stored.
input_dir = "/lhome/wim/Pictures/"

# The directory where the cropped images will be stored.
output_dir = "~/Downloads/"

# The filetypes to use.
included_extentions = ['jpg','bmp','png','gif' ] ;

file_names = [fn for fn in os.listdir(input_dir) if any([fn.endswith(ext) for ext in included_extentions])];

resolution = Image.open(input_dir + "/" + file_names[0]).size
print resolution

for image in sorted(file_names):
    print image
    #im=Image.open(input_dir + "/" + image)
    #print im.size
#im = Image.open('~/Pictures/IMG_20140320_072340.jpg')

#outfile = "sth2.jpg"
#region=im.crop((0, 0, 1920, 1080))
##Do some operations here if you want but on region not on im!
#region.save(outfile, "JPEG")
