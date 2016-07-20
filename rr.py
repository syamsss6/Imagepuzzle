with open("2.txt","r") as input:
    with open("newfile.txt","wb") as output: 
        for line in input:
            if line!="GET"+"\n":
                output.write(line)
