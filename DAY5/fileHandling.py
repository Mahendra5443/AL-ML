path =r"C:\Users\MY-PC\Desktop\test.txt"
path1 ="C:\\Users\MY-PC\Desktop\test.txt"
path2 ="C:/Users/MY-PC/Desktop/test.txt"
with open(path1,"w") as file:
    file.write("text")
    
with open(path1,"r") as file:
    text = file.read()
    print(text)