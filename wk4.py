import csv
import json


with open("text.txt","w") as file:
    Write = file.write("Hello There my name is horace. \n I am a Software Engineer and Biomedical Engineer.")
    print(Write)

with open("text.txt","r") as file:
    read = file.read()
    print(read)

data = [
     "Name","Age","Class"

]
with open("text.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(data)

with open("text.csv","r",newline="") as file:
    reader = csv.reader(file)
    context = next(reader)
    print(context)

my_data = {
    "name":"Horace",
    "age":22,
    "class":"Engineering"
}

with open("text.json","w",newline="") as file:
    json.dump(my_data,file)

with open("text.json","r") as file:
    read = json.load(file)
    print(read)