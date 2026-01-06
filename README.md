# DSTV Tools
A Python library for visualizing and exporting structural steel profiles in DSTV format (NC/NC1).
🎯 Features

DSTV File Parsing: Full support for NC and NC1 files
Interactive Visualization: Interactive matplotlib plotters to analyze profile faces
DXF Export: Automatic generation of DXF files for each profile face
Face Management: Intelligent composition of profile faces with offset support
Hole Labeling: Automatic annotations for holes and machining operations

# Installation
## Clone the repository
```bash
git clone https://github.com/serg-you-lin/dstv-tools.git
cd dstv-tools
```
 
## Install dependencies
pip install -r requirements.txt

## Or install in development mode
pip install -e .

# Quick Start
## Example 1: Profile Visualization
```python
from dstvparser.parsers.factory import NCFileParserFactory
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstv_tools.plotters.profile_plotter import ProfilePlotter

# Load NC file
nc_path = 'your_nc_file
nc_part = NCFileParserFactory.create_parser(nc_path)
profile = nc_part.parse()

# Compose profile faces
profile_faces = ComposeProfileFaces(profile)

# Visualize the profile
plotter = ProfilePlotter(profile_faces)
plotter.plot_all_faces()
plotter.show()
```

## Example 2: Interactive Visualization
```python
from dstvparser.parsers.factory import NCFileParserFactory
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstv_tools.plotters.interactive_plotter import InteractiveProfilePlotter

# Load NC file
nc_path = 'your_nc_file
nc_part = NCFileParserFactory.create_parser(nc_path)
profile = nc_part.parse()

# Create an interactive plotter with offset between faces
profile_faces = ComposeProfileFaces(profile, offset_between_faces=150)
plotter = InteractiveProfilePlotter(profile_faces, y_plot_lim=150)

# Display all faces with offset
fig = plotter.plot_all_faces(with_offset=True)
plotter.show(fig)

# Or display a single face (e.g., top flange 'o')
fig = plotter.plot_face('o')
plotter.show(fig)
```
## Example 3: DXF Export
```python
from dstvparser.parsers.factory import NCFileParserFactory
from dstv_tools.exporters.compose_profile_faces import ComposeProfileFaces
from dstv_tools.exporters.profile_dxf_exporter import ProfileDXFExporter

# Load NC file
nc_path = 'your_nc_file
nc_part = NCFileParserFactory.create_parser(nc_path)
profile = nc_part.parse()

# Create the exporter
exporter = ProfileDXFExporter(profile_faces)

# Export a single face
file_single = exporter.export_face('o', add_labels=True)
print(f"Exported file: {file_single}")

# Export all faces to separate files
files = exporter.export_all_faces(
    base_file_path="output/profile_722",
    separate_files=True,
    add_labels=True
)

# Export all faces to a single DXF file with offset
profile_faces = ComposeProfileFaces(profile, offset_between_faces=150)
exporter = ProfileDXFExporter(profile_faces)
file_complete = exporter.export_all_faces(
    base_file_path="output/complete_profile",
    separate_files=False,
    add_labels=True
)
```

# Project Structure
```bash
dstv-tools/
├── dstv_tools/
│   ├── exporters/          # Export modules
│   │   ├── compose_profile_faces.py
│   │   └── profile_dxf_exporter.py
│   ├── plotters/           # Visualization modules
│   │   ├── profile_plotter.py
│   │   └── interactive_plotter.py
│   └── utils/              # Utilities and schemas
│       ├── drawers.py
│       ├── faces_name_schemas.py
│       ├── profile_schemas.py
│       └── utilities.py
├── examples/               # Usage examples
│   ├── inspect_DXF_export.py
│   ├── inspect_interactive_plotting.py
│   ├── inspect_plotting_faces.py
│   └── data/               # Sample NC files
└── requirements.txt
```

🔧 Dependencies

dstvparser: For parsing DSTV NC/NC1 files
matplotlib: For visualization
ezdxf: For DXF file generation
numpy: For numerical operations

# Documentation
## ComposeProfileFaces
The ComposeProfileFaces class handles the composition and organization of profile faces.
Parameters:

profile: Parsed profile object from dstvparser
offset_between_faces: (optional) Distance between faces when displaying multiple faces (default: 0)

## ProfilePlotter
Basic plotter for static visualization of profile faces.
Methods:

plot_face(face_name): Plot a specific face
plot_all_faces(): Plot all faces
show(): Display the plot
save(filename): Save the plot to file

## InteractiveProfilePlotter
Advanced plotter with interactive features.
Parameters:

profile_faces: ComposeProfileFaces object
y_plot_lim: (optional) Y-axis limit for the plot

Methods:

plot_face(face_name): Create interactive plot for a specific face
plot_all_faces(with_offset=True): Create interactive plot for all faces
show(fig): Display the interactive plot

## ProfileDXFExporter
Export profile faces to DXF format.
Methods:

export_face(face_name, add_labels=False): Export a single face
export_all_faces(base_file_path, separate_files=True, add_labels=False): Export all faces

separate_files=True: Creates one DXF file per face
separate_files=False: Creates a single DXF file with all faces (with offset)



# Face Naming Convention
The library uses a standard naming convention for profile faces:

'o': Top flange
'u': Bottom flange
'l': Left web
'r': Right web

(Face names may vary depending on the profile type)
💡 Use Cases

Steel Fabrication: Visualize and verify CNC machining operations
Quality Control: Check hole positions and dimensions
CAD Integration: Export faces to DXF for use in CAD software
Documentation: Generate technical drawings of profile faces
Analysis: Interactive exploration of complex profile geometries

## Inspection scripts
The examples folder contains manual inspection scripts.
These can be run directly after installing the package with pip install -e ..

## License
MIT License — feel free to use, modify, and share with attribution.

## Contributions
Pull requests are welcome! If you find issues or have suggestions, please open an issue in the repository.

## Author
Federico Sidraschi https://www.linkedin.com/in/federico-sidraschi-059a961b9/

Built on top of dstvparser
Uses the DSTV standard for steel profile data exchange


Note: This library requires the dstvparser package to function. Make sure it's properly installed and accessible in your Python environment.