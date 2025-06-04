file_path="output.txt"
with open(file_path,"w")as file:
    file.write("hello,world!\n")
    file.write("this is a simple text")
    print("content writte to",file_path)
