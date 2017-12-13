import os
import os.path
global ret
import pkg

def search(path,isnotrec=True):
    if (isnotrec):
        ret = []
    for root, dirs, files in os.walk(path):
        for e in files:
            if (e.endswith(".py")):
                ret.append(os.path.join(root,e))
        for e in dirs:
            search(os.path.join(root, e),True)
    if (isnotrec):
        return ret
print("Making all .py files into a single build.pkg file")
print("searching")
s = search(os.path.realpath("C:\\")) #search
print("Building Pakage")        
pkg.Make(s,"build.pkg")
print("Extraction")
pkg.breakpkg("build.pkg",os.path.realpath(".\py")) #comment out if you dont want to autoextract
                                          
