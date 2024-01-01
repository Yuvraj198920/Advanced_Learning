import tkinter as tk
from tkinter import filedialog
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

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_file_path)

def select_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(defaultextension='.kml', filetypes=[("KML files", "*.kml")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_file_path)

def convert_files():
    csv_to_kml(input_file_path, output_file_path)
    tk.messagebox.showinfo("Success", "File converted successfully")

app = tk.Tk()
app.title("CSV to KML Converter")

input_file_path = ""
output_file_path = ""

# Input file selection
input_label = tk.Label(app, text="Input CSV File")
input_label.pack()
input_entry = tk.Entry(app, text="", width=50)
input_entry.pack()
input_button = tk.Button(app, text="Browse", command=select_input_file)
input_button.pack()

# Output file selection
output_label = tk.Label(app, text="Output KML File")
output_label.pack()
output_entry = tk.Entry(app, text="", width=50)
output_entry.pack()
output_button = tk.Button(app, text="Browse", command=select_output_file)
output_button.pack()

# Convert button
convert_button = tk.Button(app, text="Convert", command=convert_files)
convert_button.pack()

app.mainloop()
