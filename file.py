#f = open('sample.txt','w')
#string = """python programming   """
#f.write(string)
#f.close()
#print("file operation completed")


#append mode
#f = open('sample.txt','a')
#string = """java programming   """
#f.write(string)
#f.close()
#print("file operation completed")


#w+mode
f = open('sample.txt','r+')
#string = """java programming   """
#f.write(string)
f.write('Python')
content=f.read()        #content=f.readline()--> it prints all the contents like a list of elements means reading the each line as one element
print(content)    # or print(content[:])--> to print the whole content
f.close()
print("content added successfuly")