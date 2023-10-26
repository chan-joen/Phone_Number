import os
import csv
import pandas as pd

name_num = []
name =[]
number = []

#directory = "\\phone_num"

#file_name = os.listdir(directory)
file_name = os.listdir()

 # = "output_1.csv"
for filename in file_name:
    if filename.startswith('output') == True:
        file_path = os.path.join(filename)
        #file_path = os.path.join(directory, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                tmp = line.strip()
                name_num.append(tmp)

if __name__ == "__main__":
    i=0
    j=0
    while i != len(name_num):
        while j != len(name_num):
            if name_num[i] == name_num[j] and i != j:
                name_num.pop(j)
                j-=1
            j+=1
        j=0
        i+=1

    for i in range(len(name_num)):
        for j in range(len(name_num[i])):
            if name_num[i][j] == ",":
                tmp = name_num[i][:j]
                name.append(tmp)
                tmp = name_num[i][j+1:]
                number.append(tmp)

    for i in range(len(number)):
        tmp = number[i]
        if tmp.startswith('11') == True:
            tmp = '0'+tmp[:2]+'-'+tmp[2:5]+'-'+tmp[5:9]
            number[i] = tmp
        elif tmp.startswith('10') == True:
            tmp = '0'+tmp[:2]+'-'+tmp[2:6]+'-'+tmp[6:10]
            number[i] = tmp
#with open(directory+"\\orgnized_file.csv", mode="w", newline="",encoding="utf-8") as csv_file:
with open("orgnized_file.csv", mode="w", newline="",encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    for i in range(len(name_num)):
        tmp = [
            name[i],number[i]
        ]
        writer.writerow(tmp)
name.pop(0)
number.pop(0)
df = pd.DataFrame({
    '이름':name,
    '전화번호':number,
})
#df.to_excel(directory+"\\orgnized_file.xlsx", index=False ,engine='openpyxl')
df.to_excel("orgnized_file.xlsx", index=False ,engine='openpyxl')