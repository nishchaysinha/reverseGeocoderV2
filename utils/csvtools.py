import csv

fields=['FeatureID', 'AIM_Postal', 'AIM_Addres', 'Near_POI', 'Country', 'Admin_l1', 'Admin_l2', 'Direction', 'Street_Nm', 'Latitude', 'Longitude', 'Address']

class csvController():
    #constructor of csvController
    def __init__(self, filename):
        self.filename = filename
        pass

    #read csv file
    def read(self):
        data = []
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        return data
    #write csv file
    def write(self, data):
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for row in data:
                csvwriter.writerow(row)
    def append(self, data):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for row in data:
                csvwriter.writerow(row)