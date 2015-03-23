from PIL import Image
import os

# The directory where all the images for the timelapse are stored.
input_dir = "/Users/wim/Desktop/20150307-201512/"

# The directory where the cropped images will be stored.
output_dir = "/Users/wim/Desktop/out1/"

# The filetypes to use.
included_extentions = ['jpg','JPG','bmp','BMP','png','PNG','gif','GIF'] ;

file_names = [fn for fn in os.listdir(input_dir) if any([fn.endswith(ext) for ext in included_extentions])];
number_of_files = len(file_names)
print "Number of files to process: " + str(number_of_files)

resolution = Image.open(input_dir + "/" + file_names[0]).size
print "Original files have a resolution of " + str(resolution)

# The first version calculates the movement of the dolly from the bottom right to the top left.
# First top-left coordinates
first_y = resolution[1] - 1080
first_x = resolution[0] - 1920

# final top-left coordinates
final_y = 0
final_x = 0

step_x = (final_x - first_x) / (number_of_files - 1.)
step_y = (final_y - first_y) / (number_of_files - 1.)

count = 0
for image in sorted(file_names):
    im=Image.open(input_dir + "/" + image)
    outfile = output_dir + "%07d.jpg" %count
    x = (int)(first_x + step_x * count)
    y = (int)(first_y + step_y * count)
    print "Cropping file " + str(count) + ": im.crop(%d, %d, %d, %d)" % (x, y, x + 1920, y + 1080)
    region=im.crop((x, y, x + 1920, y + 1080))
    region.save(outfile, "JPEG")
    count += 1

