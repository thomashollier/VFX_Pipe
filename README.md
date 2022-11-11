# VFX_Pipe
Tools, Tips and Tricks for small team/high end VFX production

1. [Background](#background)
2. [Must have tools](#must-have-tools)
3. [Open source packages](#open-source-packages)
4. [Commercial software](#commercial-software)
5. [Hardware](#hardware)
6. [Online services](#online-services)
7. [Cool Tricks](#cool-tricks)

## Background:
I've worked in high end VFX and animation production facilities for many years and I am part of the "first wave" of people who ended up inventing the workflow that has now been codified into the standard VFX production pipeline. (By the way, I don't want to take undue credit: there are so many other way smarter people who made significant impacts but I like to think some of my contributions have left a trace here or there...). Economic and personal circumstances have made it such that I am now working independently on the periphery of larger facilities, and I have found that the resources necessary to produce high end work that once were the exclusivity of large facilities are now available to smaller and perhaps more flexible and efficient organizations. 

## Must have tools.
In addition to artistry, the key to a succesfull VFX project is to efficiently process data in a non destructive way that targets the specific intended goal with the right level of accuracy. No matter what the brochure for the latest version of the software says, managing the production of VFX will always throw some convoluted set of circumstances for which there is simple no push button solution. You need to be fluent with both the abstracted data flow and the specific tools that constitute the building blocks, and you need to have the ability to get them to interact with each other in an efficient, coherent and reproducible way.

### ocio and ACES config files
This allows you to properly ingest imagery and deliver it in a way that maintains the integrity of the original data. Typically, footage will be ingested in some custom camera LOG format, be worked on in linear ACEScg, and deliver either in ACES or some display referred space. Most software tools are now aces compliant, and you need a properly set up environment to take advantage of it.

### oiio tools
No matter how thorough software is, production always seems to create situations where something needs to be translated or converted in some custom fashion that is not easily achievable within the main software packages. oiiotool is a swiss army knife that can handle all common VFX image formats, color space conversions, generate textures, as well as some basic color correction and image processing. It has a python API and can easily be embedded in scripted tasks.

### ffmpeg
If oiiotools is a swiss army knife, then ffmpeg is a set of Ginsu knifes that can make quick work of most digital video needs. It provides simple and efficient solutions to workflows involving the ingest or generation of video clips. Although it is very different in legacy and background from oiio, it makes a great partner to it and there is very little that can't be done with the two together. It also has various APIs that aloows it to be embedded in scripted processes.

### python
Because you need glue to stick things together

### bash
and sometimes, when you don't have time for the glue to dry, you can use duct tape to get you through your immediate need.

### openCV/PIL/imagemagick/vips
It's always good to have ways to manipulate images on the command line. The above commands and/or libraries do that. They each have their pluses and minuses. More or less fast, complicated to use, etc... No clear winner here but I use these to fill in the gap where oiiotool is missing specific functionality.

### Installing these tools
Installing software on linux can be quite an undertaking if you're not (or, actually, also if you are...) a developer. Fortunately, I found that the "brew" package manager has all the important packages, and they all seem quite up to date. So, install brew and just do this:

brew install ffmpeg opencolorio openimageio imagemagick 

If everything goes according to plan, it should fail in various unpredictable ways that will take you a while to figure out. To be fair, though, I've found that brew is actually fairly reliable in terms of providing the latest versions while handling dependencies without too much headache. It's also available on osX.


## Open source packages
### Blender
### Darktable or Digikam
### Meshroom
### Gimp
### Krita
### djv, mrViewer

## Commercial software
### Maya/Arnold, Houdini, VRay
### Nuke
### Resolve/fusion
### Cinesync
### Syntheyes

## Online services
### Google drive
### Hightail
### Cloud rendering service
### Fiber internet service

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
A texture paint package should allow you to apply global color corrections to a whole set of textures in one step but if you want to apply arbitrary correction to a set of texture images you inherited, you can color correct one texture in photoshop until you like where you are and then apply that correction in photoshop to your neutral HALD lut, save it out and apply it to all your textures.
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
