# Compute sphericity of 3D object

## Introduction
This script computes the sphericity of 3D objects using volume information and the principal inertia transform of the model itself.

## Dependencies
- Python3.7 or later with pip
- Python libraries : `trimesh` and `numpy.`

## How to go

clone the repository folder
```
git clone git@gitlab.com:clariaddy/compute-sphericity-of-3d-object.git

```
Install the dependencies
```
pip install trimesh and numpy
```

## Usage

To compute the sphericity of STL files in a folder, run the script as follows:
```
python3 compute_sphericity.py`
```

Make sure to update the `folder_path` variable in the script with the path to your folder containing the STL files. The results will be saved to `sphericity_results.txt` in the same directory as the script.

## Notes

The script will print the principal inertia transform details for debugging purposes. The code is adapted only to STL files.
