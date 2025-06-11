f=open("C:\\Users\\Administrator\\Desktop\\mahammad.txt",'r')
print("the filepointer ia at byte:",f.tell())
content=f.read();
print("after readinf,the filepointer is at:",f.tell())
