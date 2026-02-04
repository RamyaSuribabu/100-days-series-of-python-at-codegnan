import csv


try:
    with open('contact.csv','w') as f:
        data = csv.writer(f)
        print(data)
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")