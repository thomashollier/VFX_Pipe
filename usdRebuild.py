from pxr import Usd, UsdGeom, Gf, Sdf
import xml.etree.ElementTree as ET

import random

def createStage(n):
	stageName = "./usd/asmb/%s.usda" % n
	rootName = "/%s"%n
	stage = Usd.Stage.CreateNew(stageName)
	UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
	rootPrim = UsdGeom.Xform.Define(stage, rootName)
	stage.SetDefaultPrim(stage.GetPrimAtPath(rootName))
	for prim in stage.Traverse():
		print(prim.GetName())
	print("------\nCreate stage %s with root xform %s\n" % (stageName, rootName))
	return stage

def createChild(n, stage, attrib):
	top = stage.GetPrimAtPath("/").GetChildrenNames()[0]
	loc = "/%s%s" % (top,n)
	child = UsdGeom.Xform.Define(stage, loc)
	translate = eval(attrib['translate'])
	translate = (translate[0], translate[1], translate[2])
	rotate = eval(attrib['rotate'])
	rotate = (rotate[0], rotate[1], rotate[2])
	scale = eval(attrib['scale'])
	scale = (scale[0], scale[1], scale[2])
	geo = attrib['filePath'].replace("M:/house/data/ass/","").replace(".ass.gz", ".usd").replace("ass", "usda").replace("v16", "v19").replace('ramparts_v04', 'ramparts_v05')
	geo = "../cmpt/%s" % geo
	geo = geo.replace("/Dressing_v05/", "/setDressing_v05/")
	if geo.find("Rock")>0 or geo.find("ent")>0 or geo.find("meto")>0 or True:
		print(geo)
		child.GetPrim().GetReferences().AddReference(geo)
		child.GetPrim().SetInstanceable(True)
		modelAPI = Usd.ModelAPI(child.GetPrim())
		modelAPI.SetKind('assembly')
		try:
			child.AddTranslateOp(opSuffix=attrib['name']).Set(value=translate)
			child.AddRotateYOp(opSuffix=attrib['name']).Set(value=rotate[1])
			child.AddScaleOp(opSuffix=attrib['name']).Set(value=scale)
		except:
			print("failed at %s" % n)

def saveStage(stage):
	stage.Save()

########################################

def dig(el, path):
	if not el.get('name'):
		path = "%s/%s" % ( path, el.tag)
		for nextEl in el.findall("./"):
			dig(nextEl, path)
	else:
		path = "%s/%s" % (path,el.get('name'))
		createChild(path, stage, el.attrib)

########################################

myXML = ET.parse('xml/exportRamparts.xml')
root = myXML.getroot()

stageName = "ramparts_v05"

stage = createStage(stageName)

for h in root.findall("./"):
	dig(h,"")

saveStage(stage)


