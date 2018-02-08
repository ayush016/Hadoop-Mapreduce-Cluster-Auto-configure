import os


f = open('ex.xml','r')
contents = f.readlines()
f.close()
#print contents
#print type(contents)
count = 0
for i in contents:
	count = count + 1
	print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break
#print count

contents.insert(count, "<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n")

f = open('ex.xml','w')
contents = "".join(contents)
f.write(contents)
f.close()
