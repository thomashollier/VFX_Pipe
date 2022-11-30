# VFX_Pipe
Tools, Tips and Tricks for small team/high end VFX production

1. [Background](#background)
2. [Must have pipeline tools](#must-have-tools)
3. [Open source packages](#open-source-packages)
4. [Commercial software](#commercial-software)
5. [Hardware](#hardware)
6. [Online services](#online-services)
7. [Cool Tricks](#cool-tricks)

## Background:
I've worked in high end VFX and animation production facilities for many years and I am part of the "first wave" of people who ended up inventing the workflow that has now been codified into the standard VFX production pipeline. (To be clear, there are many other people way smarter than me who made much bigger impacts in the field but I like to think some of my contributions have left a trace here or there...). I am now doing more work independently or on the periphery of larger facilities, and I have found that the resources necessary to produce high end work that once were the exclusivity of those large facilities are now available to smaller efficient organizations. 

## Must have tools.
In addition to artistry, an effective VFX production needs to efficiently process data in a non destructive way that targets specific tasks with a meaningful level of accuracy. The following tools provide that capability as long as you don't mind putting your pipeline builder hat on.

### ocio and ACES config files
This allows you to properly ingest imagery and deliver it in a way that maintains the integrity of the original data. Typically, footage will be ingested in some custom camera LOG format, be worked on in linear ACEScg, and deliver either in ACES or some display referred space. Most software tools are now aces compliant, and you need a properly set up environment to take advantage of it.

### oiio tools
Production always seems to create situations where something needs to be translated or converted in some custom fashion that is not easily achievable within the main software packages. oiiotool is a swiss army knife that can handle all common VFX image formats, color space conversions, generate textures, as well as some basic color correction and image processing. It has a python API and can easily be embedded in scripted tasks.

### ffmpeg
Ffmpeg is a workhorse that provides efficient solutions to needs relating to the ingest or the generation of video clips. Although it is very different in legacy and background from oiio, it makes a great partner to it and there is very little that can't be done with the two together. It also has various APIs that aloows it to be embedded in scripted processes.

### python
Because you need glue to stick things together

### bash
and sometimes, when you don't have time for the glue to dry, you can use duct tape to get you through your immediate need.

### openCV/pillow/imagemagick/vips
It's always good to have ways to manipulate images on the command line. The above commands and/or libraries do that. They each have their pluses and minuses. More or less fast, complicated to use, etc... No clear winner here but I use these to fill in the gap where oiiotool is missing specific functionality.

### Installing these tools
Installing software on linux can be quite an undertaking if you're not (or, actually, also if you are...) a developer. Fortunately, I found that the "brew" package manager has all the important packages, and they all seem quite up to date. So, install brew and just do this:

brew install ffmpeg opencolorio openimageio imagemagick opencv

Another necessary evil in this software soup is the python package manager "pip". The process of installing the right package in the right place with the right version of python can be very time consuming.

pip3 install pillow    # image processing library
pip3 install pyseq     # manage file sequences
pip3 install pycubelut # apply cube luts in python

## Open source or free software packages
Even though the subscription models for commercial packages offer an entry point for smaller organizations, these costs can quickly add up. There are many open source solutions that can offer similar functionality.

### Blender
I'm not a power user but I am continuing to learn it as I go. A lot of great dev work is going into Blender and it has grown significantly more powerful over the last few years. It will continue to grab an increasing part of the production base, particularly as USD becomes more universally adopted.

### Davinci Resolve
This is the free version of a commercial product. Its main focus is color correction and editorial but it includes Fusion which is a very capable compositing package. It has ACES support, 3D, great masking and roto tools, and it is fast. The free version can only output to UHD and has a few disabled features but it's a very well rounded production tool.

### Meshroom
This is a great free photogrammetry tool. I've been able to capture large sets and accurately place cameras in those sets.

### Darktable or Digikam
Lightroom is a great tool but I find that its cost is too steep for the specific functionality I am looking for. These two tools offer a good solution for handling photo reference and digital negatives for data aquisition.

### Gimp and Krita
Same as Darktable or Digikam: If you don't feel you are getting the value out of the Adobe Creative Suite, these tools can offer most of photoshop's functionality.

### djv, mrViewer
These programs give the artist the ability to play back full dynamic range image sequences or movie files with frame accuracy in a color space compliant, which is definitely not trivial. You need a lot more than just a movie player. Looks like djv is no longer being maintained but MrViewer is.

## Commercial software
### Subscription model
There was a time when purchasing a license to professional VFX production software represented an investment that could easily reach in the tens of thousands of dollars. This is no longer the case. Most major packages offer affordable short term licenses, as well as significant discounts for independent operators. This provides the flexibility to make use of the right tool at the right time without breaking the bank.

### Special mentions
While the above model has been adopted by most of the major players, some packages are still using a "buy to own" model which are not prohibitive. The first one is Davinci Resolve. It's a production tested editing and color correction system, and it includes Fusion which is a very capable compositor that includes 3d tools and some great masking and rotoing options. It's very affordable and you get a really surprisingly fast and powerful suite of tools. 
The other tool worth a mention is syntheyes for match moving. It's fairly unintuitive but it's very fast and powerful. 

## Online services
### Fiber internet service
If you don't have fast internet, you can't really do any production work remotely. Simple as that. Lucky for me, my neighborhood was just outfitted with fiber and I now get 900 Mbps downloads AND uploads. Obviously, it's not instantaneous but it is completely adequate for my needs. It's a game changer. My "fast" cable service was 60 Mbps down and 6 Mbps up. 
### Cloud rendering services
This is another game changer. I do not have to invest in hardware to get my final work rendered. My last project involved a 450 hour final 3d render that I was able to complete in 3 hours for a very reasonable cost. Debugging the setup and the uploads took some work but once it was done, it was very transparent.
### Google drive
My projects are continually synced to a large google drive. It's pretty transparent. Sometimes, I may need to pause the service when I need to use bandwidth for something else but other than that, it's great. Don't forget that it's NOT a backup in that if you delete a file on your local machine, it gets deleted in google drive.
Another benefit of Google drive is the ability to easily share content with others when necessary. The team can have access to the same home directories and configurations.
And lastly, it's great to have the ability to access content online if you happen to be away from the workspace.
### Hightail
I think this used to be "sendit" or is a new service filling the same niche. This is designed for large file transfers, typically for footage turnovers and final deliveries.

## Cool tricks
### cube and HALD luts from ACES OCIO transforms
Use imagemagick to create a HALD image (this makes a 512x512 which seems accurate enough for my purpose but if you want a 24 bit, use 17 instead of 8):
~~~
magick hald:8 hald512_Neutral.png
~~~
Use oiiotool to bake any color correction in a new HALD image. In this case, I am creating a convert from ARRI Log space to aces, increasing the exposure by 2 stops, and then converting to sRGB.
~~~
oiiotool hald512_Neutral.png --colorconvert "Input - ARRI - V3 LogC (EI800) - Wide Gamut" "ACES - ACEScg" \
  -mulc 4 \
  --colorconvert "ACES - ACEScg" "output - sRGB" -o hald512_log2sRGB+2.png
~~~
Finally, I use [this handy little python script](https://github.com/thomashollier/LUT-Convert) to generate a cube lut
~~~
./hald_to_cube.py hald512_log2sRGB+2.png hald512_log2sRGB+2.cube
~~~
You can then apply any ACES color transforms in ffmpeg (extremely useful to quickly create accurate proxies)
~~~
ffmpeg -i darkCameraClipInLog.mxf -vf "lut3d=hald512_log2sRGB+2.cube,scale=1920:-1" twoStopsBrighterInsRGBClip.mov
~~~
### Watermarks with ffmpeg
You can add watermarks to your lut converted proxies
~~~
#!/bin/bash

input=/path/to/movie/A029C001_220610_CPEK.mov

recipient="vendorX"
copyright="©2022 Relentless Play"

textCommand=\
'drawtext=text='${recipient}':fontsize=(w/20):fontcolor=white:alpha=.25:x=(w-text_w)/2:y=(h-text_h)/2+(1.5*w/20)\
,drawtext=text=--- DO NOT DISTRIBUTE ---:fontsize=(w/20):fontcolor=white:alpha=.25:x=(w-text_w)/2:y=(h-text_h)/2\
,drawtext=text='${copyright}':fontsize=(w/20):fontcolor=white:alpha=.25:x=(w-text_w)/2:y=(h-text_h)/2-(1.5*w/20)'

ffmpeg -i ${input} -vf "lut3d=/mnt/f/RP_WTN//bin/cubeluts/log2sRGB.cube,${textCommand}" \
-c:v h264 -crf 28 -pix_fmt yuv420p -an ${recipient}_$(basename ${input}) -y
~~~
### Global texture correction with HALD luts
A texture paint package should allow you to apply global color corrections to a whole set of textures in one step but sometimes, you need to apply arbitrary correction to a set of texture images you inherited. You can color correct one texture in gimp or photoshop until you get the desired result, apply that correction to your neutral HALD image, save it out and apply it to all your textures.
~~~
#!/bin/bash
mkdir original
for tx in *_color.png
do
magick $tx hald_photoshopCC.png -hald-clut transform.png
mv $tx original
mv transform.png $tx
done
~~~
### Dailies
This isn't quite finished yet. I forked a github repo and tried to adapt it to my needs but didn't quite get there. If I were to go back, I'd probably want to start from scratch and figure out ahead of time all the possible use cases for this kind of script and design it in a more flexible and modular way.
