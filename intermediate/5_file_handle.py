###Fifth Class###
import os, json, csv, xml
#File Handle
#.txt
##The w+ means that it can do more then just write it
file_save = open("intermediate/practice_file.txt", 'w+')
file_save.write(
    "Mi nombre es Maximiliano\nMi apellido es Grosman\nTengo 29 anios\nY estoy aprendiendo Python"
)
file_save.close()
#The r+ is the same thing as the w+
file_save = open("intermediate/practice_file.txt", 'r+')
print(file_save.read(10))#How much it reads
print(file_save.readline())
for line in file_save.readlines(): print(line)
file_save.write("\nAunque tambien estoy trabajando en repasar C++")
print(file_save.readline())
file_save.close()
# os.remove("intermediate/practice_file.txt") #Eliminates the file

#.json file
json_file = open("intermediate/json_file.json", "w+")
json_test = {"name": "Maximiliano","surname": "Grosman",
    "age": 29, "language": ["Python", "C++", "Javascript"], "website": "none"}
json.dump(json_test, json_file, indent=1)
#Indent spaces from the beginning
json_file.close()
with open("intermediate/json_file.json") as to_read:
    for line in to_read.readlines(): print(line)

json_dict = json.load(open("intermediate/json_file.json"))
print(json_dict)
print(type(json_dict))

#.csv file
csv_file = open("intermediate/csv_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "Language", "Website"])
csv_writer.writerow(["Maximiliano", "Grosman", 29, "Python", "None"])
csv_writer.writerow(["TNB", "", 19, "Kobal", ""])
csv_file.close()

with open("intermediate/csv_file.csv") as to_read:
    for line in to_read.readlines(): print(line)
#.xlsx file doesn't come with Python, install module
#.xml file