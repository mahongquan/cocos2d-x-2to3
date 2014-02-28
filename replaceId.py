import os
import re
import time
import codecs
dic={}
jiacc=["spriteWithFile","actionWithDuration","menuWithItem","itemWithLabel","transitionWithDuration","spriteWithFile","labelWithString","node"]#,"Object","Sprite","Point","Scene","Node","MoveTo","Director","Application","Size","Touch","Event"]
dic["CCMutableArray"]="CCArray"
dic["CGFloat"]="CCFloat"
dic["ccTime"]="float"
for one in jiacc:
    dic[one]="create"
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
       #print "append"
    return lr
def myfindstr(a,p):
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    return re.search(p2,a,re.IGNORECASE)
def fileAS(f):
    return(len(open(f).readlines()))
def removeSingleComment(string):
    pattern=re.compile(r"//.*")
    repl=""
    #m=re.search(p,s)#r"/\*.*\*/",s)
    #print m.group(0)
    return re.sub(pattern, repl, string)#, count=0, flags=0)
def removeMutilComment(string):
    pattern=re.compile(r"""/\*.*?\*/""", re.X | re.S)
    repl=""
    #m=re.search(p,s)#r"/\*.*\*/",s)
    #print m.group(0)
    return re.sub(pattern, repl, string)#, count=0, flags=0)
def treadfile(inputFileName,srcpath,outputpath):
    print inputFileName
    (path,filename)=os.path.split(inputFileName)
    path=path[len(srcpath):]
    (leftname,ext)=os.path.splitext(filename)
    s=codecs.open(inputFileName,"r","utf-8").read()
    if ord(s[0])>256:
        s=s[1:]
    s=removeSingleComment(removeMutilComment(s))

    fc=replaceId(s)  
    #output
    if path!="":
        path=outputpath+"/"+path
    else:
        path=outputpath
    print path+"/"+filename  
    f=codecs.open(path+"/"+filename,"w","utf-8")
    f.write(fc)
    f.close()
def main():
    lt=time.localtime()
    path="../test_input"
    files=mylistdir(path,"*.cpp")
    files2=mylistdir(path,"*.h")
    for f in files2:
        files.append(f)
    print files
    for f in  files:
        fn=path+"/"+f
        treadfile(fn,path,"../test_output")
def rep_func(a):
    old=a.group(0)
    new=dic.get(old)
    if new!=None:
        return new
    return old
def replaceId(string):
    pattern=re.compile(r"([a-zA-Z_][a-zA-Z_0-9]*)",re.U)
    return re.sub(pattern,rep_func, string)#, count=0, flags=0)
def test1():
    src=r"""static PyObject*
    py_\1(void)
    {"""
    print re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
            src,
            'def myfunc():')
    print re.sub(r"([a-zA-Z_][a-zA-Z_0-9]*)","xx","a1  is B1,c1 is d1,_c1")
if __name__=="__main__":
    main()
