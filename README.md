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
I've worked in high end VFX and animation production facilities for many years and I am part of what I call the "first wave" of people who ended up inventing the workflow of what has now been codified into the fairly standard VFX production pipeline. (By the way, I don't want to take undue credit: there are so many other way smarter people who made significant impacts but I like to think some of my contributions have left a trace here or there...). Economic and personal circumstances have made it such that I am now working independently on the periphery of larger facilities, and I am pleased to experience a new environment where the kinds of resources necessary to produce high end work that once were the exclusivity of large facilities are now available to smaller and perhaps more flexible and efficient organizations. One of the ongoing challenges of digital production is having the ability to quickly scale up or down.

## Must have tools.
In addition to artistry, the key to a succesfull VFX project is to efficiently process data in a non destructive way that targets the specific intended goal with the right level of accuracy.

### ACES ocio ditribution.
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
