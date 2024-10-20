
# Unreal Level Design Helper Tool

This tool automates the placement of objects in Unreal Engine using Python scripting. It allows designers to quickly place objects like trees or props in a grid and randomize their scale and rotation for a natural look.

## Features
- **Batch Object Placement**: Place objects in a grid pattern in the world.
- **Randomization**: Randomly adjust the scale and rotation of placed objects to add variety.
- **Supports Static Meshes**: Uses Unreal Engine's Static Meshes from a specified asset folder.

## Setup
1. Enable the **Python Editor Script Plugin** in Unreal Engine.
2. Clone this repository into your Unreal project directory.
3. Place the `level_design_helper.py` file in the `Scripts` folder of your project.

## Usage
1. Open the **Output Log** in Unreal Engine.
2. Run the script by typing the following command:
   ```python
   import level_design_helper
   level_design_helper.place_objects_in_grid()
   ```

3. Customize the script variables like `grid_size`, `grid_spacing`, `scale_range`, and `rotation_range` to fit your needs.
