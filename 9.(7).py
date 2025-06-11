f=open("C:\\Users\\Administrator\\Desktop\\mahammad.txt",'r')
print("the filepointer is at byte:",f.tell())
f.seek(10);
print("after reading, the filepointer is at :",f.tell())
