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

count = 0
for image in sorted(file_names):
    #im=Image.open(input_dir + "/" + image)
    outfile = output_dir + "%07d.jpg" %count
    print outfile
    #region=im.crop((0, 0, 1920, 1080))
    #region.save(outfile, "JPEG")
    count += 1

