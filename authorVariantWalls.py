from pxr import Usd, UsdGeom, Gf, Sdf

# This script takes 2 usd meshes and creates variants with them.

def createStage(n):
	stageName = "./usd/asmb/%s.usda" % n
	rootOverPath = "/%s"%n
	stage = Usd.Stage.CreateNew(stageName)
	UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
	#rootOver = stage.OverridePrim(rootOverPath)
	rootOver = UsdGeom.Xform.Define(stage, rootOverPath)
	spherePrim = UsdGeom.Sphere.Define(stage, "%s/world"%rootOverPath)
	print(rootOver)
	#stage.SetDefaultPrim(rootOver)
	for prim in stage.Traverse():
		print(prim.GetName())
	print("------\nCreate stage %s with root xform %s\n" % (stageName, rootOverPath))
	return stage, rootOver

def createVariants(p):
	rootPrim = stage.GetPrimAtPath('/Wall')
	vset = p.GetVariantSets().AddVariantSet('floorVariant')
	vset.AddVariant('floor_0')
	vset.AddVariant('floor_1')
	#p.GetReferences().Clear()
	print("vset", vset)
	vset.SetVariantSelection('floor_1')
	with vset.GetVariantEditContext():
		p.GetReferences().AddReference('usd/cmpt/walls_v15/geo_entrances/entrance_03.usd')
	vset.SetVariantSelection('floor_2')
	with vset.GetVariantEditContext():
		p.GetReferences().AddReference('usd/cmpt/walls_v15/geo_stairGrounds/stairground_01.usd')
	vset.SetVariantSelection('floor_0')
	with vset.GetVariantEditContext():
		p.GetReferences().AddReference('usd/cmpt/walls_v15/geo_walls/wall_03.usd')







#stage, over = createStage("Wall")
#createVariants(over)


stage = Usd.Stage.CreateNew("fuckthis.usda")
#xformPrim = UsdGeom.Xform.Define(stage, "/hello")
o = stage.OverridePrim("/Wall")

createVariants(o)


#vset = rootPrim.GetVariantSets().AddVariantSet('shadingVariant')


stage.Save()



print(stage.ExportToString())


