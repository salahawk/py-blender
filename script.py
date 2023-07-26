import requests
import bpy
from pywavefront import Wavefront
from const import MESH_NAME, OBJECT_NAME, MODIFIER_NAME


def download_obj_file(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)


def create_mesh(vertices, faces):
    # Create a new mesh
    mesh = bpy.data.meshes.new(MESH_NAME)

    # Create a new object with the mesh data
    obj = bpy.data.objects.new(OBJECT_NAME, mesh)

    # Link the object to the scene
    bpy.context.collection.objects.link(obj)

    # Set the mesh data
    mesh.from_pydata(vertices, [], faces)

    # Update the mesh geometry
    mesh.update()


def import_obj_file(obj_file_path):
    # Load the .obj file using pywavefront
    obj = Wavefront(obj_file_path)

    # Access the contents of the .obj file
    vertices = obj.vertices
    faces = obj.faces

    # Call the function to create the mesh
    create_mesh(vertices, faces)

    return obj


def apply_subdivision_surface_modifier(obj):
    # Add a Subdivision Surface modifier to the object
    modifier = obj.modifiers.new(name=MODIFIER_NAME, type="SUBSURF")

    # Set the subdivision level
    modifier.levels = 2

    # Apply the modifier to the object
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=modifier.name)


def export_smoothed_object(obj, output_path):
    # Select the object
    obj.select_set(True)

    # Apply the Subdivision Surface modifier
    # apply_subdivision_surface_modifier(obj)

    # Export the object as an OBJ file
    bpy.ops.export_scene.obj(filepath=output_path, use_selection=True)


if __name__ == "__main__":
    download_path = "https://people.sc.fsu.edu/~jburkardt/data/obj/airboat.obj"
    save_file_path = "airboat.obj"
    smoothed_file_path = "smoothed.obj"

    # Download & import obj file
    download_obj_file(url=download_path, save_path=save_file_path)
    import_obj_file(obj_file_path=save_file_path)

    # Get the object by name
    obj = bpy.data.objects.get(OBJECT_NAME)

    if obj is not None:
        # Apply the Subdivision Surface modifier to the object
        apply_subdivision_surface_modifier(obj)
        export_smoothed_object(obj, output_path=smoothed_file_path)
    else:
        print(f"Object '{OBJECT_NAME}' not found in the scene.")

    apply_subdivision_surface_modifier(obj=obj)
