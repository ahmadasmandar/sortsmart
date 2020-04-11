import os
content=os.listdir()
target="Tutsgalaxy.com"

for item in content:
    # delete the text files and the urls files to clean the library
    if (item.find(".txt") > 0 or item.find(".url")> 0 ):
        print(item)
        os.remove(item)
        
    #rename the files and folders
    if (item.find(target) >0):
        # print(len(target))
        # print(item.find(target))
        new_name=item[19:]
        os.rename(item,new_name)
    