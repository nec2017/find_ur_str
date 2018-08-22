# encoding = utf-8
import os
import pdb
import sys

count = 0
name = "none"

def input_target():
    key = input("*which key word do you need?:")
    path = input("*please input path of the folder:")
    '''path_type = input("absolute path or relative path? a/r")
    path = [path, path_type]
    if path_type == "a":
        pass
    else:
        pass
    path = path[0]'''
    mono = [path, key]
    return mono

def judge_exist(path):
    #pdb.set_trace()
    if os.path.exists(path):
        return path
    else:
        option = input("*folder or file path doesn't exist!\n try again? y/n:")
        if option == "y":
            return False
        else:
            sys.exit()

def iterate(key, path):
    try:
        for i in os.listdir(path):
            #pdb.set_trace()
            i = path + "/" + i
            if i[-4:] == ".zip":
                continue
            elif os.path.isdir(i):
                name = os.path.relpath(i)
                #i = path + "/" + i
                iterate(key, i)
            elif os.path.isfile(i):
                #i = path + "/" + i
                readNsearch(key, i)
    except:
        pass

def readNsearch(key, filename):
    with open(filename) as f:
        contents = f.read()
        if key in contents:
            print("key word exists in " + filename)
        else:
            print("not in " + filename)

'''
def output_form():
    print(count*"   " + "├──" + name)
    print("└──" + name)'''

def main():
    targ = input_target()
    targ_path = targ[0]
    targ_key = targ[1]
    sth = judge_exist(targ_path)
    if sth:
        filename = iterate(targ_key, sth)
    else:
        main()
    #readNsearch(targ_key, filename)    

main()    
