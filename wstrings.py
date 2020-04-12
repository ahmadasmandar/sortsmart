import re
import string
invalid_list=[]
with open("file_list.log","r") as lg:
    for line in lg.readlines():
        new_line=str(line)

        for char in new_line:
            if (char == ']'):
                invalid_list.append(new_line)
            else:
                pass
    
    lg.close()
for x in invalid_list:
    print(x)