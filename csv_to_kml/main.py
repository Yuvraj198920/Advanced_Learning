import pandas as pd
import simplekml


def csv_to_kml(csv_file_path, kml_file_path):
    # Load the CSV data
    df = pd.read_csv(csv_file_path)

    # Convert the datetime column to datetime objects and sort by this column
    df['Datetime (UTC)'] = pd.to_datetime(df['Datetime (UTC)'])
    df = df.sort_values(by='Datetime (UTC)')

    # Convert altitude from feet to meters (1 foot = 0.3048 meters)
    df['GPS Altitude (m)'] = df['GPS Altitude (ft MSL)'] * 0.3048

    # Create a simple KML object
    kml = simplekml.Kml()

    # Create two folders: one for points and one for the line
    points_folder = kml.newfolder(name="Points")
    line_folder = kml.newfolder(name="Flight Path")

    # Add points to the Points folder
    for index, row in df.iterrows():
        pnt = points_folder.newpoint(name=str(row['Datetime (UTC)']),
                                     coords=[(row['Longitude'], row['Latitude'], row['GPS Altitude (m)'])])

    # Add a LineString to the Flight Path folder
    linestring = line_folder.newlinestring(name="Flight Path")
    linestring.coords = [(row['Longitude'], row['Latitude'], row['GPS Altitude (m)']) for index, row in df.iterrows()]
    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
    linestring.style.linestyle.color = simplekml.Color.red
    linestring.style.linestyle.width = 2

    # Save the KML file
    kml.save(kml_file_path)


# Example usage
csv_file_path = r'C:\Users\yuvra\OneDrive\Desktop\flight_from_Tue_Dec_12_2023_4_45_44_PM_SkydioX2_83cd.csv'  # Replace with your CSV file path
kml_file_path = 'output_file.kml'  # Replace with your desired KML file path

# Convert the CSV file to a KML file
csv_to_kml(csv_file_path, kml_file_path)
