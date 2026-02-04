import csv


try:
    with open('contact.csv','r') as f:
        data = csv.reader(f)
       print()
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")