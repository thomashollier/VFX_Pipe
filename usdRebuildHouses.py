from pxr import Usd, UsdGeom, Gf, Sdf
import xml.etree.ElementTree as ET

import random

# this reads a xml file written out of maya with scale
# transforms, and arnold archive files. The maya file describes houses
# which are made out of square "room" transforms made out of various wall geometry





def createHouse(n):
	stage = Usd.Stage.CreateNew("%s.usda" % n)
	UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
	return stage

def createRoom(n, stage, attrib):
	print(n)
	room = UsdGeom.Xform.Define(stage, "/%s" % n)
	modelAPI = Usd.ModelAPI(room)
	modelAPI.SetKind('component')
	translate = eval(attrib['translate'])
	translate = (translate[0]*57, translate[1]*57, translate[2]*57)
	room.AddTranslateOp(opSuffix='Translate').Set(value=translate)
	room.AddScaleOp(opSuffix='Scale').Set(value=(57, 57, 57))

def createWall(n, stage, attrib):
	wall = UsdGeom.Xform.Define(stage, "/%s" % n)
	translate = eval(attrib['translate'])
	translate = (translate[0], translate[1], translate[2])
	rotate = eval(attrib['rotate'])
	rotate = (rotate[0], rotate[1], rotate[2])
	scale = eval(attrib['scale'])
	scale = (scale[0], scale[1], scale[2])
	geo = attrib['geo']
	geoDir = "geo_%ss" % geo.split("_")[0].rstrip("F")
	geo = "../walls_v20/%s/%s.usd" % (geoDir, geo)
	geo = geo.replace("balconys", "balconies")
	floor = n.split("/")[1][-1:][0]
	if int(floor) > 0:
		geo = geo.replace("geo_wall", "geo_wallFloor")
		geo = geo.replace("wall_", "wallFloor_")
	wall.GetPrim().GetReferences().AddReference(geo)
	print(geo)
	try:
		wall.AddTranslateOp(opSuffix=attrib['name']).Set(value=translate)
		wall.AddRotateYOp(opSuffix=attrib['name']).Set(value=rotate[1])
		wall.AddScaleOp(opSuffix=attrib['name']).Set(value=scale)
	except:
		print("failed at %s" % n)
#	print("\t\t%s"%geo)

def saveHouse(stage):
	stage.Save()
	


houses = ET.parse('xml/exportAssetshouses_v20.xml')


root = houses.getroot()

for h in root.findall("./"):
	house = "%s" % h.attrib['name']
	stage=createHouse(house)
	for r in h.findall("./"):
		room = "%s/%s" % (house, r.attrib['name'])
		createRoom(room, stage, r.attrib)
		for w in r.findall("./"):
			wall = "%s/%s" % (room, w.attrib['name'])
			createWall(wall, stage, w.attrib)
			#print("\t\t%s" % w.attrib['name'])
	stage.SetDefaultPrim(stage.GetPrimAtPath("/%s" %  house))
	saveHouse(stage)

