#!/usr/bin/env python
import os
import re
import sys
import codecs
#############################
dic={}
jiacc=["spriteWithFile","actionWithDuration","menuWithItem","itemWithLabel","transitionWithDuration","spriteWithFile","labelWithString","node"]#,"Object","Sprite","Point","Scene","Node","MoveTo","Director","Application","Size","Touch","Event"]
dic["CCMutableArray"]="CCArray"
dic["CGFloat"]="float"
dic["ccTime"]="float"
for one in jiacc:
    dic[one]="create"
##############################
pattern = re.compile(r"""   (//[^\r\n]*) # match a single line comment
                            | (/\*.*?\*/)      # match a multi line comment
                            | ("[^"]*")        # match a string literal
                            | ([a-zA-Z_][a-zA-Z_0-9]*) #identifier
                        """
                           , re.X | re.S)
def translateValue(old):
    new=dic.get(old)
    if new!=None:
        return new
    return old
def func(match):
    if match.group(1) or match.group(2) or match.group(3):
        return match.group()
    if match.group(4):
        return  translateValue(match.group())#
        #raw_input()
    else:
      return match.group()
def translateStr(source):
  return re.sub(pattern,func,source)
def translateFile(inputFileName):
  s=codecs.open(inputFileName,"r","utf-8").read()
  return translateStr(s)
def treatfile(inputFileName):
  print inputFileName
  #bak
  cmd="cp %s %s" %(inputFileName,inputFileName+".bak")
  os.system(cmd)
  #translate
  fc=translateFile(inputFileName)
  #output
  f=codecs.open(inputFileName,"w","utf-8")
  f.write(fc)
  f.close()
#dir##################
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
def translateDir(path):#
    files=mylistdir(path,"*.cpp")
    files2=mylistdir(path,"*.h")
    for f in files2:
        files.append(f)
    for f in  files:
        fn=path+"/"+f
        treatfile(fn)
if __name__=="__main__":
    translateDir(sys.argv[1])
