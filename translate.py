#!/usr/bin/env python
import os
import re
import sys
import codecs
#############################
dic1_2={}
tocreate=["menuWithItems","itemFromString","spriteWithFile","actionWithDuration","menuWithItem","itemWithLabel","transitionWithDuration","spriteWithFile","labelWithString","node"]#,"Object","Sprite","Point","Scene","Node","MoveTo","Director","Application","Size","Touch","Event"]
dic1_2["CCMutableArray"]="CCArray"
dic1_2["CGFloat"]="float"
dic1_2["ccTime"]="float"
dic1_2["LAYER_NODE_FUNC"]="CREATE_FUNC"
dic1_2["CCTextAlignmentCenter"]="kCCTextAlignmentCenter"
dic1_2["setDisplayFPS"]="setDisplayStats"
dic1_2["setIsTouchEnabled"]="setTouchEnabled"
dic1_2["getObjectAtIndex"]="objectAtIndex"
dic1_2["locationInView"]="getLocationInView"
dic1_2["setIsVisible"]="setVisible"
for one in tocreate:
    dic1_2[one]="create"
########################
addcc=["GLProgram","TMXLayer","RenderTexture","FiniteTimeAction","TMXTiledMap","TextureCache","Texture2D","Object","Scene","Sprite","SpriteFrame","Node","Director","Point","Size","Layer"
,"LayerColor","LayerGradient"
,"Rect","Event","Touch","SpriteBatchNode"
,"ShaderCache","OrbitCamera","ShaderCache"
,"PointArray","Color4B"

,"Action","FadeOut","FadeIn","FadeTo","TintBy","TintTo","Sequence","RepeatForever","CatmullRomTo","CatmullRomBy"
,"CardinalSplineBy","CardinalSplineTo"
,"SkewBy","SkewTo","JumpBy","JumpTo","BezierTo","BezierBy","Place"
,"RotateBy","rotateTo","MoveTo","MoveBy","ScaleBy","ScaleTo","ActionInterval"
,"Blink","SpriteFrameCache","Animation","AnimationCache","Animate"
,"CallFunc","CallFuncN","CallFuncND","DelayTime","ToggleVisibility","TargetedAction"
,"Shaky3D","Waves3D","FlipX3D","FlipY3D","Lens3D"

,"Menu","MenuItem","MenuItemFont","MenuItemLabel","MenuItemToggle","MenuItemSprite"
,"LabelBMFont","Label","LabelTTF","labelAtlas","EaseElasticOut","RemoveSelf"
]
dic2_3={}
dic2_3["objectAtIndex"]="getObjectAtIndex"
dic2_3["sharedDirector"]="getInstance"
dic2_3["sharedEngine"]="getInstance"
dic2_3["CCArray"]="__Array"
dic2_3["CCString"]="__String"
dic2_3["ccc3"]="Color3B"
dic2_3["CCLog"]="log"
dic2_3["CCObject"]="Ref"
dic2_3["Object"]="Ref"
dic2_3["CCSizeMake"]="Size"
dic2_3["CCSet"]="__Set"
dic2_3["CCDictionary"]="__Dictionary"
dic2_3["ccp"]="Point"
dic2_3["CCRectMake"]="Rect"
dic2_3["CCPointMake"]="Point"
dic2_3["sharedAnimationCache"]="getInstance"
dic2_3["sharedSpriteFrameCache"]="getInstance"
dic2_3["sharedUserDefault"]="getInstance"
dic2_3["sharedTextureCache"]="getInstance"
dic2_3["textureForKey"]="getTextureForKey"
dic2_3["sharedFileUtils"]="getInstance"
dic2_3["spriteFrameByName"]="getSpriteFrameByName"
dic2_3["animationByName"]="getAnimation"
dic2_3["ccBlendFunc"]="BlendFunc"
dic2_3["CCPointZero"]="Vec2()"
dic2_3["tileGIDAt"]="getTileGIDAt"
dic2_3["ccColor4F"]="Color4F"
dic2_3["kCCTextAlignmentLeft"]="TextHAlignment::LEFT"
dic2_3["kCCTextAlignmentRight"]="TextHAlignment::RIGHT"
dic2_3["kCCTextAlignmentCenter"]="TextHAlignment::CENTER"
dic2_3["layerNamed"]="getLayer"
dic2_3["tileAt"]="getTileAt"
dic2_3["propertiesForGID"]="getPropertiesForGID"
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
  print inputFileName
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
  if len(sys.argv)>1:
    translateDir(sys.argv[1])
  else:
    print "This program should be use like this:\n\n\t\tpython translate.py srcdir"



