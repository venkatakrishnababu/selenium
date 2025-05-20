with open("source.txt", "r") as E:
    with open("target2.txt","w") as F:
        for i in E.readlines():
            if "error" in i:
                b=i.strip()
                F.writelines(b+'\n')