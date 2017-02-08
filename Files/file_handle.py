file = open("example.txt",'r')
content = file.read()
print(content)
file.close()
 file.readlines reads into a list. this means using things like seek and maybe even rstrip

file = open("example1.txt",'w')
file.write("Line 1")
file.close()

file1 = open("example1.txt",'a')
file1.write("\nHello")
file1.close()

with open("example1.txt",'a+') as file2:
    file2.seek(0)
    content=file2.read()
    file2.write("\nNow how great is this. No need for close")
