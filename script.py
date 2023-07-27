import bpy
import urllib.request

# First, we need to clear all meshes in the scene
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.delete()

# URL of the object file
obj_url = "https://people.sc.fsu.edu/~jburkardt/data/obj/airboat.obj"

# Specify a path to a directory on your system where you want to save the downloaded file.
# Make sure to adjust this to a valid directory on your system.
local_path = "C:\\temp\\airboat.obj"

# Download the obj file
obj_file = urllib.request.urlretrieve(obj_url, local_path)

# Import the obj file into the scene
bpy.ops.import_scene.obj(filepath=local_path)

# Get the imported object
imported_obj = bpy.context.selected_objects[0]

# Apply a subdivision surface modifier to the object
bpy.context.view_layer.objects.active = imported_obj
bpy.ops.object.modifier_add(type="SUBSURF")

# Increase the levels of the subdivision
bpy.context.object.modifiers["Subdivision"].levels = 2

# Apply the subdivision surface modifier
bpy.ops.object.modifier_apply(
    {"object": bpy.context.active_object}, modifier="Subdivision"
)

# Specify a path to a directory on your system where you want to save the exported file.
export_path = "C:\\temp\\smoothed_airboat.obj"

# Export the smoothed object
bpy.ops.export_scene.obj(filepath=export_path)
