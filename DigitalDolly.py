from PIL import Image
im = Image.open('~/Pictures/IMG_20140320_072340.jpg')

outfile = "sth2.jpg"
region=im.crop((0, 0, 1920, 1080))
#Do some operations here if you want but on region not on im!
region.save(outfile, "JPEG")
