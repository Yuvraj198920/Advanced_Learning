# Development Documentation for CSV to KML Converter Tool
## Introduction
This document provides the necessary information for developers to set up, understand, and contribute to the CSV to KML Converter Tool. This tool is designed to convert geographic data from CSV format to KML format, primarily for use in mapping applications like Google Earth.

## Environment Setup
### Requirements
- Python 3.6 or higher.
- Access to a command-line interface (CLI).

## Setting Up a Python Virtual Environment
1.**Create a Virtual Environment**: Run the following command in your project directory:
```commandline
python -m venv venv
```
2.**Activate the Virtual Environment:**
- On Windows:
```commandline
.\venv\Scripts\activate
```
- On Linux:
```commandline
source venv/bin/activate
```
## Dependency Installation
Install all required dependencies by running the following command within the virtual environment:
`pip install pandas simplekml tkinter PyInstaller
`
## Running the Script Locally
To run the CSV to KML GUI application:
`python gui_csv_to_kml.py`

## Code Structure
`gui_csv_to_kml.py`: Main script containing the GUI and logic for converting CSV files to KML format.
- Functions:
  - GUI related functions for file selection and triggering the conversion process.

## Building the Executable
To create a standalone executable for distribution:
`pyinstaller --onefile --windowed gui_csv_to_kml.py
`
## Testing
#### 1. Test the script in the development environment with various CSV files to ensure proper conversion.
#### 2. Test the standalone executable on different systems to ensure compatibility.

## Contributing

#### 1. Fork the repository (if hosted on a platform like GitHub).
#### 2. Create a new feature branch for your changes.
#### 3. After making changes, test the application thoroughly.
#### 4. Submit a pull request with a clear description of the changes.