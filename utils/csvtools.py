import csv

fields=['FeatureID', 'AIM_Postal', 'AIM_Addres', 'Near_POI', 'Country', 'Admin_l1', 'Admin_l2', 'Direction', 'Street_Nm', 'Latitude', 'Longitude', 'Address']

def csvread(filename):
    data = []
    with open(filename, mode='r') as file:
        csvreader = csv.reader(file)
        for lines in csvreader:
            data.append(lines)
    return data

def csvwrite(filename):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
    return 0

