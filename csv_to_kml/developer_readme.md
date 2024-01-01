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

## CSV File Format Requirements
The CSV to KML Converter Tool is designed to work with CSV files that adhere to a specific format. The expected structure of the CSV file is detailed below:
### Required Columns
The CSV file must contain the following columns:
- `Latitude`: The latitude of the location (in decimal degrees).
- `Longitude`: The longitude of the location (in decimal degrees).
- `GPS Altitude (ft MSL)`: The altitude in feet above Mean Sea Level (MSL).
- `Datetime (UTC)`: The timestamp in UTC, formatted as **`YYYY-MM-DDTHH:MM:SS.ssssss+00:00`**
### Example CSV Structure
```commandline
Datetime (UTC),Latitude,Longitude,GPS Altitude (ft MSL),...
2023-12-13T00:45:07.581272+00:00,37.534575,-122.331322,495.288729,...
2023-12-13T00:45:07.700970+00:00,37.534577,-122.331323,496.811003,...
...

```
***Note***: The CSV file can contain additional columns, but they will be ignored by the tool.
### Handling CSV Files
- Ensure the CSV file adheres to the above format for the tool to process it correctly.
- The tool reads the CSV file in the order of the rows. Make sure that the data is sorted chronologically if the order of points matters for the KML file.
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