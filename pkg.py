import os
import base64
import os.path
pathjoin = os.path.join
import shutil

def Make(filelist,output):
    files = {}
    os.mkdir("tmp")
    for e in filelist:
        outfile = e.split("\\")[-1].split(".")[0]
        base64.encode(open(e,'rb'), open("tmp\\"+outfile+".b64",'wb'))
        files[e] = open("tmp\\"+outfile+".b64","rb").read().decode("ascii")
                                                
    r = open("tmp\\pkg.rawpkg","w")
    r.write("arc = {\n")
    for file in files:
        
        data = files[file]
        r.write("\""+file.split("\\")[-1]+"\":\""+data.replace("\n","\\n")+"\",\n")
    r.write("}")
    r.close()
    base64.encode(open("tmp\\pkg.rawpkg",'rb'), open(output,'wb'))
    shutil.rmtree("tmp", ignore_errors=True)
    return pathjoin(os.path.realpath(os.curdir),output)



def breakpkg(pkg,path):
    base64.decode(open(pkg,'rb'), open("tmp.py",'wb'))
    pak =  __import__("tmp")
    arc = pak.arc
    try:
        os.mkdir("tmpex")
    except:
        osx=os
    for file in arc:
        data = arc[file]
        f = open("tmpex\\"+file.split(".")[0]+".b64","w")
        f.write(data)
        f.close()
    for file in arc:
        base64.decode(open("tmpex\\"+file.split(".")[0]+".b64",'rb'), open(os.path.join(path,file),'wb'))
    shutil.rmtree("tmpex", ignore_errors=True)
    os.remove("tmp.py")
##try:       
##    filename = Make(["pyphone.py","appapi.py"],"pypy.pkg")
##except:
##    shutil.rmtree("tmp", ignore_errors=True)
##    filename = "pypy.pkg"
##breakpkg(filename,".")

