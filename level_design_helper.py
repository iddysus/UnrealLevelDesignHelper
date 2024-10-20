
import unreal
import random

# Written by Idlan bin Hafiz

# Define the folder path for your asset (static meshes) in Unreal
asset_path = "/Game/Props/Trees"

# Define grid size and spacing
grid_size = 5  # Number of objects per row and column
grid_spacing = 500  # Distance between objects in Unreal units

# Define randomization ranges
scale_range = (0.8, 1.2)  # Random scale factor range (e.g., from 0.8 to 1.2 times the original size)
rotation_range = (-180, 180)  # Random rotation range in degrees

# Get the asset tools helper
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Get a reference to the editor level library (to place objects)
editor_level_lib = unreal.EditorLevelLibrary()

# Get the static meshes from the asset path
def get_assets_from_path(asset_path):
    assets = unreal.EditorAssetLibrary.list_assets(asset_path)
    static_meshes = [unreal.EditorAssetLibrary.load_asset(asset) for asset in assets if isinstance(unreal.EditorAssetLibrary.load_asset(asset), unreal.StaticMesh)]
    return static_meshes

# Place objects in a grid and randomize their scale and rotation
def place_objects_in_grid():
    static_meshes = get_assets_from_path(asset_path)
    
    if not static_meshes:
        print("No static meshes found at the specified asset path.")
        return
    
    # Starting position for the grid
    start_x, start_y, start_z = 0, 0, 0
    
    for i in range(grid_size):
        for j in range(grid_size):
            # Choose a random static mesh to place
            static_mesh = random.choice(static_meshes)
            
            # Calculate position for this object in the grid
            x = start_x + i * grid_spacing
            y = start_y + j * grid_spacing
            z = start_z
            
            # Set random scale and rotation
            scale_factor = random.uniform(scale_range[0], scale_range[1])
            rotation_yaw = random.uniform(rotation_range[0], rotation_range[1])
            
            # Spawn the object in the world
            transform = unreal.Transform(location=(x, y, z), rotation=(0, 0, rotation_yaw), scale=(scale_factor, scale_factor, scale_factor))
            actor = editor_level_lib.spawn_actor_from_object(static_mesh, transform)
            
            if actor:
                print(f"Placed {static_mesh.get_name()} at ({x}, {y}, {z}) with scale {scale_factor} and rotation {rotation_yaw}°.")

# Call the function
if __name__ == "__main__":
    place_objects_in_grid()
