# DigitalDolly
Digital dolly prepares the pictures for a timelapse to mimic the movement made by a dolly.

Modern digital cameras have a resolution that exceeds the resolution of full-HD timelapse movies (1920x1080). By shooting the separate pictures in full resolution, it is possible to move inside the picture to add movement to your timelapse movies.

To run this python script, you need to have PIL (python-imaging) installed. PIL is automatically installed in python distributions like <a href="https://store.continuum.io/cshop/anaconda/">Anaconda</a>. The script only works when the resolution of all images is the same (and larger than 1920x1080).

### Usage

You have to specify at least the `inputDir` and the `outputDir` parameters. If no other parameters are given, the timelapse will move from the bottom right of the image to the top left.

    python DigitalDolly.py --inputDir=/home/USER/myInputDir --outputDir=/home/USER/myOutputDir

You can also give the `beginX`, `beginY`, `endX` and `endY` parameters. These parameters describe the upper left pixel of the images. So make sure to `beginX` and `endX` are not larger than the horizontal number of pixels of the image - 1920. Also make sure that `endX` and `endY` are not larger than the vertical number of pixels of the image - 1080.

    python DigitalDolly.py --inputDir=/home/USER/myInputDir --outputDir=/home/USER/myOutputDir --beginX=120 --endX=1000 --beginY=2000 --endY=250

### Example
In the example below, you see the timelapse of a mountain in Austria without using DigitalDolly: 
<br /><br />
<a href="http://www.youtube.com/watch?feature=player_embedded&v=sSKWPCDhgO8" target="_blank"><img src="http://img.youtube.com/vi/sSKWPCDhgO8/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

In the next example, you see the same timelapse, but the images are prepared using DigitalDolly: 
<br /><br />
<a href="http://www.youtube.com/watch?feature=player_embedded&v=7Ng0Xvd8J5w" target="_blank"><img src="http://img.youtube.com/vi/7Ng0Xvd8J5w/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
