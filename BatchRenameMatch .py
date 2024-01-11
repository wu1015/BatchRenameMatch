import os
from fnmatch import fnmatch

# 文件夹路径
folderpath=input(r"请输入路径:"+"\n")
# 需要匹配的字符key
matchDict={"key":"value"}
#更改当前路径
os.chdir(folderpath) 
# 该文件夹下所有的文件（包括文件夹）
filelist = os.listdir(folderpath)  
# flag为操作数，0为替换目标字符串，1为使用字符串进行覆盖
flag=input("0为替换目标字符串，1为使用字符串进行覆盖:\n")
print("该文件夹总共"+str(len(filelist))+"个文件或文件夹")
print("重命名结果为:")
for i in matchDict.keys():
    for j in filelist:
        # 需要文件有扩展名，否则会报错
        stxt=str(j).split(".")
        # 使用通配符匹配字符串（如“啊123不”，“123”，匹配“123”）
        if(fnmatch(stxt[0],"*"+i+"*") or fnmatch(stxt[0],"*"+matchDict.get(i)+"*")):
            if(flag=="0"):
                lsTmp=str(stxt[0]).split(i,1)
                # 加上原文件名和扩展名
                newName=lsTmp[0]+i+matchDict.get(i)+lsTmp[1]+"."+stxt[len(stxt)-1]
            elif(flag=="1"):
                # 补上原扩展名
                newName=i+matchDict.get(i)+"."+stxt[len(stxt)-1]
            # 重命名，j为旧文件名，newName为新文件名
            print(newName)
            YN=input("是否确定重命名，y or n\n")
            if(YN=="Y"):
                os.rename(j,newName) 
    
