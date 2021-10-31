def listSites():
    with open(r"C:\Windows\System32\drivers\etc\hosts","r") as f:
        fileContent=f.readlines()
        return fileContent


def addSite(website):
        if website != "" and " " not in website:
            with open(r"C:\Windows\System32\drivers\etc\hosts","a") as f:
                f.write("\n127.0.0.1		"+website)
            
            
def removeSite(website):
    if website != "" and " " not in website:
        rows=[]
        with open(r"C:\Windows\System32\drivers\etc\hosts","r") as f:
            fileContent=f.readlines()
            for i in fileContent:
                if website in i:
                    continue
                    print("removed")
                rows.append(i)   
            
        with open(r"C:\Windows\System32\drivers\etc\hosts","w") as f:
            for i in rows:
                f.write(i)              