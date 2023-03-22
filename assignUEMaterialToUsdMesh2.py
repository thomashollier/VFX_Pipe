from pxr import Usd, UsdGeom, Sdf, UsdShade
import os



##############
# Assuming a single mesh usd file
# Create a material and a binding to an Unreal material location so it gets automagically assined on load
# Remove the existing material assignment if one is found  in the file
#
##############


def findNodes(stage):
	look = None
	for x in stage.Traverse():
		if x.GetTypeName() == 'Mesh':
			geo = x	
		if x.GetTypeName() == 'Material':
			if x.GetParent().GetTypeName() == "Scope":
				look = x.GetParent()
	return geo, look

def addUnrealMtlAttrs(stage, prim, mtl):
	primPath = prim.GetPath()
	_material = stage.DefinePrim("%s/UnrealMaterial"% primPath, "Material")
	_shader = stage.DefinePrim("%s/UnrealMaterial/UnrealShader"% primPath, "Shader")
	sourceAsset= _shader.CreateAttribute('info:unreal:sourceAsset', Sdf.ValueTypeNames.Asset, variability = Sdf.VariabilityUniform)
	sourceAsset.Set(mtl)
	implementationSource = _shader.CreateAttribute('info:implementationSource', Sdf.ValueTypeNames.Token, variability = Sdf.VariabilityUniform)
	implementationSource.Set('sourceAsset')
	outputsToken = _shader.CreateAttribute('outputs:out', Sdf.ValueTypeNames.Token)
	connect = _material.CreateAttribute("outputs:unreal:surface", Sdf.ValueTypeNames.Token)
	connect.SetConnections([outputsToken.GetPath()])
	UsdShade.MaterialBindingAPI(prim).GetDirectBindingRel().SetTargets([_material.GetPath()])

def processFile(srcFile, unrealMtlPath, dryRun = True):
	print("Processing %s" % srcFile)
	dstDir = "%s_processed" % os.path.dirname(srcFile)
	dstFile = "%s/%s" % (dstDir, os.path.basename(srcFile))
	stage = Usd.Stage.Open(srcFile)
	primMesh, primLooks = findNodes(stage)
	if primLooks:
		print("\tRemoving Looks at %s" % primLooks.GetPath())
		stage.RemovePrim(primLooks.GetPath())
	else:
		primMesh.ApplyAPI(UsdShade.MaterialBindingAPI)
	print("\tAssigning unreal mtl to %s" % primMesh.GetPath())
	addUnrealMtlAttrs(stage, primMesh, unrealMtlPath)
	print("\tOutput to: %s"% dstFile)
	if not dryRun:
		print("\t\tExporting %s\n" % dstFile)
		os.makedirs(dstDir, exist_ok = True)
		stage.Export(dstFile)
	else:
		print("\t\tNot saving: dryRun is True\n")


for root, dirs, files in os.walk("./usd/cmpt/walls_v20"):
	unrealMtlPath = "/Game/Set/mtl/mtl_env_houses.mtl_env_houses"
	for f in files:
		if f.find("usd")>0:
			srcFile = os.path.join(root, f)
			processFile(srcFile, unrealMtlPath, dryRun = 1)

exit()


