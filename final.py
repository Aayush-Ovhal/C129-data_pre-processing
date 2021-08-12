import csv

dataset_1 = []
dataset_2 = []

with open("final.csv", "r") as f:
     csv_reader = csv.reader(f)
     for row in csv_reader:
          dataset_1.append(row)

with open("caltech_data_sorted.csv", "r") as f:
     csv_reader = csv.reader(f)
     for row in csv_reader:
          dataset_2.append(row)

data1_header = dataset_1[0]
data2_header = dataset_2[0]

data1_planet_data = dataset_1[1:]
data2_planet_data = dataset_2[1:]

headers = data1_header + data2_header

planet_data = []
for index, data_row in enumerate(data1_planet_data):
      planet_data.append(data1_planet_data[index] + data2_planet_data[index])

with open("finalest.csv", "a+") as f:
     csvwriter = csv.writer(f)
     csvwriter.writerow(headers)
     csvwriter.writerows(planet_data)