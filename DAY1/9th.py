count = 4
for i in range (5):
    for j in range (5):
        if(j<=count):
            print("_", end="")
        else:
            print("*", end="")
    count= count -1
    print()