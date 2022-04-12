from datetime import date
import csv

## Format the data gotten from NOAA into csv

def setup():
    today = date.today()
    filename = str(today) + ".csv"

    # create file for today's data, open for writing
    f = open(filename, "w")
    f.write(str(today) + "\n")
    f.write("Time Stamp, Water Temperature, Air Temperature, Wind, Tide, Barometric Pressure\n")
    f.close()

def write_data(wTemp, aTemp, wind, tide, pressure):
    today = date.today()
    filename = str(today) + ".csv"
    
    f = open(filename, "a")
    #csvwriter = csv.writer(f)
    
    f.write(wTemp + "," + aTemp + "," + wind + "," + tide + "," + pressure + "\n")
    f.close()

if __name__ == "__main__":
    f = setup()
    write_data("56.7", "56.7", "3.11", "4.3", "1026.2")