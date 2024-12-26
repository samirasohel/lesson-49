file=open('codingal.txt','r')
print(file.read())
file.close()

file_write=open('codingal.txt','w')
file_write.write("Hi I am samira\n")
file_write.close()

file_append=open('codingal.txt','a')
file_append.write("I am a student\n")
file_append.close