from datetime import date

## Format the data gotten from NOAA into csv

def write_data():
    today = date.today()
    filename = str(today) + ".csv"
    print(filename)
    # create file for today's data, open for writing
    f = open(filename, "w")
    f.write("Data, Data, Data")

if __name__ == "__main__":
    write_data()