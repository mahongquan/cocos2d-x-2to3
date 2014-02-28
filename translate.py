#!/usr/bin/env python
import os
import re
import sys
import codecs
#############################
dic1_2={}
tocreate=["spriteWithFile","actionWithDuration","menuWithItem","itemWithLabel","transitionWithDuration","spriteWithFile","labelWithString","node"]#,"Object","Sprite","Point","Scene","Node","MoveTo","Director","Application","Size","Touch","Event"]
dic1_2["CCMutableArray"]="CCArray"
dic1_2["CGFloat"]="float"
dic1_2["ccTime"]="float"
for one in tocreate:
    dic1_2[one]="create"
########################
addcc=["Sprite","SpriteFrame","Node","Director","Point","Size","Layer"
,"LayerColor"
,"Rect","Event","Touch","SpriteBatchNode","FadeOut","FadeIn","TintBy"
,"Sequence","RepeatForever","ShaderCache","OrbitCamera","ShaderCache"
,"SkewBy","SkewTo","JumpBy","JumpTo","BezierTo","BezierBy","Place"
,"RotateBy","rotateTo","MoveTo","MoveBy","ScaleBy","ScaleTo","ActionInterval"
,"Blink","SpriteFrameCache","Animation","AnimationCache","Animate"
,"CallFunc","CallFuncN","CallFuncND","DelayTime"
,"Menu","MenuItem","MenuItemFont","MenuItemLabel","MenuItemToggle","MenuItemSprite"
,"LabelBMFont","Label","LabelTTF","labelAtlas","EaseElasticOut","RemoveSelf"
,""]
dic2_3={}
dic2_3["objectAtIndex"]="getObjectAtIndex"
dic2_3["sharedDirector"]="getInstance"
dic2_3["CCArray"]="__Array"
dic2_3["CCString"]="__String"
for one in addcc:
    dic2_3["CC"+one]=one
###########################
dic=dic2_3
###########################
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


