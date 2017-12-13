import os
import os.path
global ret
import pkg

def search(path,isnotrec=True):
    if (isnotrec):
        ret = []
    for root, dirs, files in os.walk(path):
        for e in files:
            if (e.endswith(".pkg")):
                ret.append(os.path.join(root,e))
        for e in dirs:
            search(os.path.join(root, e),True)
    if (isnotrec):
        return ret
print("searching")
s = search(os.path.realpath("C:\\Users\\User\\Desktop"))
print("Building Pakage")        
pkg.Make(s,"build.pkg")
print("Extraction")
pkg.breakpkg("build.pkg",os.path.realpath(".\py"))
                                          
