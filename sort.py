import os
content=os.listdir()
target="Tutsgalaxy.com"
target2="FreeCourseWeb.com"
# print(len(target2))

for item in content:
    # delete the text files and the urls files to clean the library
    # print(item)
    if (item.find(".txt") > 0 or item.find(".url")> 0 ):
        print(item)
        os.remove(item)
        
    # #rename the files and folders
    if (item.find(target2) >0):
        print(item)
        # print(item.find(target2))
        new_name=item[22:]
        # print(new_name)
        os.rename(item,new_name)
    elif (item.find(target) >0):
        new_name=item[19:]
        # print(new_name)
        os.rename(item,new_name)
    