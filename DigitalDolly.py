"""
PURPOSE: Prepare separate images for a timelapse to introduce movement of the camera. This 
          will crop the image to a resolution of 1920x1080. As a consequence, the movie
          will be zoomed, but the script will travel through the image.  
         
USAGE: DigitalDolly.py --inputDir <inputDirectory> --outputDir <outputDirectory> --beginX <beginX> --beginY <beginY> --endX <endX> --endY <endY>

INPUT: --inputDir : The directory where the input files for the timelapse are located.
       --outputDir : The directory where the adapted files will be saved.
       --beginX : The left pixel where the movement will start. This should be between [0, maxX - 1920]. If this option is not given, the value will be maxX - 1920.
       --beginY : The top pixel where the movement will start. This should be between [0, maxY - 1080]. If this option is not given, the value will be maxY - 1080.
       --endX : The left pixel where the movement will end. This should be between [0, maxX - 1920]. If this option is not given, the value will be 0.
       --endY : The top pixel where the movement will end. This should be between [0, maxY - 1080]. If this option is not given, the value will be 0.

OUTPUT: Each image will be cropped and will be moved a bit in comparison with the previous image.  

"""
from PIL import Image
import getopt
import os
import sys

# The directory where all the images for the timelapse are stored.
input_dir = "/Users/wim/Desktop/20150307-201512/"

# The directory where the cropped images will be stored.
output_dir = "/Users/wim/Desktop/out1/"

first_x = -1;
first_y = -1;
final_x = -1;
final_y = -1;

# The filetypes to use.
included_extentions = ['jpg','JPG','bmp','BMP','png','PNG','gif','GIF'] ;

def dolly(input_dir=input_dir, output_dir=output_dir, first_x=first_x, first_y=first_y, final_x=final_x, final_y=final_y):
    file_names = [fn for fn in os.listdir(input_dir) if any([fn.endswith(ext) for ext in included_extentions])];
    number_of_files = len(file_names)
    print "Number of files to process: " + str(number_of_files)
    
    resolution = Image.open(input_dir + "/" + file_names[0]).size
    print "Original files have a resolution of " + str(resolution)

    # If first_x is not given, we start at the right side of the image.
    if (first_x < 0):
        first_x = resolution[0] - 1920

    # If first_y is not given, we start at the bottom of the image.
    if (first_y < 0):
        first_y = resolution[1] - 1080
    
    # If final_x is not given, we end at the left side of the image.
    if (final_x < 0):
        final_x = 0
    
    # If final_y is not given, we end at the top of the image.
    if (final_y < 0):
        final_y = 0
        
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


def main(argv):
    global input_dir, output_dir, first_x, first_y, final_x, final_y
    try:
        opts, args = getopt.getopt(argv,"i:o:",["inputDir=","outputDir=","beginX=","beginy=","endX=", "endY="])
    except getopt.GetoptError:
        print "Error parsing arguments"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "Prepare separate images for a timelapse to introduce movement of the camera. This will crop the image to a resolution of 1920x1080. As a consequence, the movie will be zoomed, but the script will travel through the image."  
            print ""
            print "USAGE: DigitalDolly.py --inputDir <inputDirectory> --outputDir <outputDirectory> --beginX <beginX> --beginY <beginY> --endX <endX> --endY <endY>"
            print ""
            print "INPUT: --inputDir : The directory where the input files for the timelapse are located."
            print "       --outputDir : The directory where the adapted files will be saved."
            print "       --beginX : The left pixel where the movement will start. This should be between [0, maxX - 1920]. If this option is not given, the value will be maxX - 1920."
            print "       --beginY : The top pixel where the movement will start. This should be between [0, maxY - 1080]. If this option is not given, the value will be maxY - 1080."
            print "       --endX : The left pixel where the movement will end. This should be between [0, maxX - 1920]. If this option is not given, the value will be 0."
            print "       --endY : The top pixel where the movement will end. This should be between [0, maxY - 1080]. If this option is not given, the value will be 0."

            sys.exit()
        elif opt in ("-i", "--inputDir"):
            input_dir = arg
        elif opt in ("-o", "--outputDir"):
            output_dir = arg
        elif opt in ("--beginX"):
            first_x = arg
        elif opt in ("--beginY"):
            first_y = arg
        elif opt in ("--endX"):
            final_x = arg
        elif opt in ("--endY"):
            final_y = arg

    dolly(input_dir, output_dir, first_x, first_y, final_x, final_y)

if __name__ == "__main__":
    main(sys.argv[1:])
