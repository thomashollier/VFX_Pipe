# VFX_Pipe
Tools, Tips and Tricks for small team/high end VFX production

1. [Must have tools](#must-have-tools)
2. [Open source packages](#open-source-packages)
3. [Commercial software](#commercial-software)
4. [Online services](#online-services)
5. [Cool Tricks](#cool-tricks)

## Platform:
Windows 10 with WSL

## Must have tools.
In addition to artistry, the key to a succesfull VFX project is to efficiently process data in a non destructive way that targets the specific intended goal with the right level of accuracy.

### ACES ocio ditribution.
This allows you to properly ingest imagery and deliver it in a way that maintains the integrity of the original data. Typically, footage will be ingested in some custom camera LOG format, be worked on in linear ACEScg, and deliver either in ACES or some display referred space. Most software tools are now aces compliant, and you need a properly set up environment to take advantage of it.

### oiio tools
No matter how thorough software is, production always seems to create situations where something needs to be translated or converted in some custom fashion that is not easily achievable within the established workflow. oiiotool is a swiss army knife that can handle all common VFX image formats, color space conversions, generate textures, as well as some basic color correction and image processing. It has a python API and can easily be embedded in scripted tasks.

### ffmpeg
ffmpeg is similar to oiio in that it is a swiss army knife. It can provide simple and efficient solutions to workflows involving the ingest or generation of video clips. Although it is very different in legacy and background from oiio, it makes a great partner to it and there is very little that can't be done with the two together. It also has various APIs that aloows it to be embedded in scripted processes.

### python
Because you need glue to stick things together

### bash
and sometimes, when you don't have time for the glue to dry, you can use duct tape to get you through your immediate need.

### openCV/PIL/imagemagick/vips
It's always good to have ways to manipulate images on the command line. The above commands and/or libraries do that. They each have their pluses and minuses. More or less fast, complicated to use, etc... No clear winner here but I use these to fill in the gap where oiiotool is missing specific functionality.

### Installing these
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
