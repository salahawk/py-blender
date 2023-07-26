# Py-Blender: Blender Python Script for Obj File Manipulation

[![License](https://img.shields.io/github/license/salahawk/py-blender)](https://github.com/salahawk/py-blender/blob/main/LICENSE)

Welcome to Py-Blender, a repository containing a Python script for manipulating Obj files in Blender. This script showcases how to perform various tasks using Blender's 'python/bpy' module. It is designed to work with Python version ^3.10 and managed with Poetry.

## Getting Started

To use Py-Blender and perform the tasks mentioned above, follow these steps:

1. Clone this repository: `git clone https://github.com/salahawk/py-blender.git`
2. Set up a Python environment with Python version ^3.10 and use Poetry to manage dependencies.
3. Run the Python script or Jupyter Notebook containing the code.
4. The script will automatically download the [airboat.obj](https://people.sc.fsu.edu/~jburkardt/data/obj/airboat.obj) file, import it into Blender, apply the subdivision surface modifier, and then export the smoothed object.

## Requirements

- Blender: Make sure you have Blender installed on your machine. You can download it from [blender.org](https://www.blender.org/).
- Python: Py-Blender requires Python version ^3.10. Please ensure you have the correct version installed in your environment.
- Poetry: The project is managed with Poetry. If you don't have Poetry installed, you can find installation instructions at [python-poetry.org](https://python-poetry.org/).

## Usage

1. Clone the repository and navigate to the project directory.
2. Install the project dependencies using Poetry: `poetry install`.
3. Run the Python script: `poetry run python script.py`.
4. The script will automatically download 'airboat.obj', perform the manipulations in Blender, and export the smoothed object.

## Contributions

Contributions to this repository are welcome! If you have any improvements, bug fixes, or additional features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of this license.

## Acknowledgments

Special thanks to [John Burkardt](https://people.sc.fsu.edu/~jburkardt/) for providing the 'airboat.obj' file.

## Contact

For any questions or inquiries, please reach out to the repository [owner](https://twitter.com/salahawk).

Happy 3D modeling with Blender and Python!