from PIL import Image
import os

# The directory where all the images for the timelapse are stored.
input_dir = "/lhome/wim/Downloads/test/in/"

# The directory where the cropped images will be stored.
output_dir = "/lhome/wim/Downloads/test/out/"

# The filetypes to use.
included_extentions = ['jpg','JPG','bmp','BMP','png','PNG','gif','GIF'] ;

file_names = [fn for fn in os.listdir(input_dir) if any([fn.endswith(ext) for ext in included_extentions])];
print "Number of files to process: " + str(len(file_names))

resolution = Image.open(input_dir + "/" + file_names[0]).size
print "Original files have a resolution of " + str(resolution)

# The first version calculates the movement of the dolly from the bottom right to the top left.
# First top-left coordinates
first_top = resolution[1] - 1080
first_left = resolution[0] - 1920

# final top-left coordinates
final_top = 0
final_left = 0

count = 0
for image in sorted(file_names):
    #im=Image.open(input_dir + "/" + image)
    outfile = output_dir + "%07d.jpg" %count
    print "Copping file " + str(count)
    #region=im.crop((0, 0, 1920, 1080))
    #region.save(outfile, "JPEG")
    count += 1

