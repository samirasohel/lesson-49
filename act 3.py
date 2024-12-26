file=open('sample.txt','r')
count=0
content=file.read()

colist=content.split("\n")
for i in colist:
    count+=1

print("Number of line in file is",count)
file.close()