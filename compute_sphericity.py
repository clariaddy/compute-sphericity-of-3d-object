import trimesh
import numpy as np
import os

# Project: Compute sphericity of 3D object

def compute_sphericity(file_path):
    # Load the mesh from a file
    mesh = trimesh.load(file_path)

    # Compute the principal moments of inertia and the axes of the bounding box
    principal_inertia_transform = mesh.principal_inertia_transform
    
    # Print to check the structure of the returned value
    print(f"Principal inertia transform for {file_path}: {principal_inertia_transform}")
    
    inertia, principal_axes = principal_inertia_transform[:2]
    axes_lengths = np.sqrt(np.sum(principal_axes**2, axis=0))

    # Compute the volume of the mesh
    volume = mesh.volume

    # Compute the equivalent diameter of a sphere with the same volume
    diameter = (6 * volume / np.pi)**(1/3)

    # Compute the sphericity
    sphericity = diameter / (np.max(axes_lengths))

    return sphericity

def process_folder(folder_path, output_file):
    results = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.stl'):
            file_path = os.path.join(folder_path, file_name)
            sphericity = compute_sphericity(file_path)
            results.append(f"{file_name}: {sphericity}\n")

    with open(output_file, 'w') as f:
        f.writelines(results)

if __name__ == "__main__":
    folder_path = 'path/to/your/folder'  # Replace with your folder path
    output_file = 'sphericity_results.txt'
    process_folder(folder_path, output_file)
    print(f"Sphericity results saved to {output_file}")