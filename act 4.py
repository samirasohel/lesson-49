file1=open('codingal.txt','r')
file2=open('sample.txt','r')

print(file1.read())
print("file 2 before merging")
print(file2.read())

file1.close()
file2.close()

f1=open('codingal.txt','r')
f2=open('sample.txt','w')

f2.write(f1.read())

f1.seek(0)
f2.seek(0)
f1.close()
f2.close()