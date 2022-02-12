import re #regular expression library
import csv #csv file library

#open the file with raw values
raw_file = open('Book1.csv')

#store and print the raw content
contents = raw_file.read()
print(contents)

#apply regular expression to find values (four digit number)
results = re.findall(r"\b(\d{4})\b", contents)

#print just to verify
print(results)

#Open new CSV file with write permission
with open('converted2.csv','w') as new_file:
    write=csv.writer(new_file)
    write.writerow(results) #write results in csv column
