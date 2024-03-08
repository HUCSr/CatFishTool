import tkinter as tk
from tkinter import Menu
import struct
import os
import threading
import json
from PIL import Image,ImageTk
import sys
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


   
def process_path (path) :
    if getattr (sys,'frozen',False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,path)
        
PROFILE = ""
CHARACTOR = ""
CARDPATH = "./lib/photo/cards/"
PROFILEPATH = ""
DECKNAME = ""
SystemCardphoto = []
PowerCardphoto = {}
SpellCardphoto = {}

SystemCardlargephoto = []
PowerCardlargephoto = {}
SpellCardlargephoto = {}

charactorID = {
    "东风谷早苗" : 0,
    "琪露诺" : 1,
    "红美铃" : 2,
    "灵乌路空" : 3,
    "洩矢诹访子" : 4,
    "博丽灵梦" : 5,
    "雾雨魔理沙" : 6,
    "爱丽丝·玛格特洛依德" : 7,
    "帕秋莉·诺蕾姬" : 8,
    "十六夜咲夜" : 9,
    "魂魄妖梦" : 10,
    "西行寺幽幽子" : 11,
    "蕾米莉亚·斯卡蕾特" : 12,
    "八云紫" : 13,
    "伊吹萃香" : 14,
    "铃仙·优昙华院·因幡" : 15,
    "射命丸文" : 16,
    "小野塚小町" : 17,
    "永江衣玖" : 18,
    "比那名居天子" : 19,
}



def new_profile() :
    global PROFILE
    global PROFILEPATH
    PROFILEPATH = asksaveasfilename(filetypes=[('profile','pf')])
    if PROFILEPATH[-3:] != '.pf':
        PROFILEPATH += ".pf"
    profilename = PROFILEPATH.split('/')[-1][:-3]
    val = bytes (b'\xff\x00\x00\x00\xc8\x00\x00\x00\xd0\x00\x00\x00\xcb\x00\x00\x00\xcd\x00\x00\x00,\x00\x00\x00-\x00\x00\x00.\x00\x00\x00\x1e\x00\x00\x00\x1f\x00\x00\x00 \x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\xff\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xd0\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00g\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xd0\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00g\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xd0\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00g\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xd0\x00\xd0\x00\xd0\x00\xd0\x00d\x00d\x00e\x00e\x00f\x00g\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00h\x00h\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00h\x00h\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00h\x00h\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00h\x00h\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xce\x00\xce\x00\xce\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xce\x00\xce\x00\xce\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xce\x00\xce\x00\xce\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xce\x00\xce\x00\xce\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xcd\x00\xcd\x00\xcd\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00e\x00f\x00g\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x00\x00\x00\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x00\x00\x00\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x00\x00\x00\x00\x14\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\x00\x00\x00\x00\x00\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00\xca\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00\xca\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00\xca\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xca\x00\xca\x00\xca\x00\xca\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xca\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xca\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xca\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xca\x00\xca\x00\xca\x00\xca\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\xd5\x00\xd5\x00\xd5\x00\xd5\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\xd5\x00\xd5\x00\xd5\x00\xd5\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\xd5\x00\xd5\x00\xd5\x00\xd5\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xcb\x00\xcb\x00\xcb\x00\xcb\x00\xd5\x00\xd5\x00\xd5\x00\xd5\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00\x14d\x00d\x00e\x00e\x00f\x00f\x00g\x00g\x00\xc8\x00\xc8\x00\xc8\x00\xc8\x00\xc9\x00\xc9\x00\xc9\x00\xc9\x00\xcc\x00\xcc\x00\xcc\x00\xcc\x00')
    with open ((PROFILEPATH),'wb') as f:
        f.write (struct.pack("3386s",val))
        f.close()
    PROFILE = profilename
    root.destroy()
    
def open_profile() :
    global PROFILE
    global PROFILEPATH
    PROFILEPATH = askopenfilename(filetypes=[('profile','pf')])
    if PROFILEPATH[-3:] != '.pf':
        PROFILEPATH += ".pf"
    profilename = PROFILEPATH.split('/')[-1][:-3]
    PROFILE = profilename
    root.destroy()

def init_system_card () :
    global SystemCardphoto
    global SystemCardlargephoto
    for i in range (0,10) :
        commonImage = Image.open(process_path(CARDPATH+"common/card00"+str(i)+".png"))
        commonImage = commonImage.resize((64,102),Image.ANTIALIAS)
        SystemCardphoto.append (ImageTk.PhotoImage(commonImage))
        
        commonImage = Image.open(process_path(CARDPATH+"common/card00"+str(i)+".png"))
        commonImage = commonImage.resize((96,156),Image.ANTIALIAS)
        SystemCardlargephoto.append (ImageTk.PhotoImage(commonImage))
        
    for i in range (10,21) :
        commonImage = Image.open(process_path(CARDPATH+"common/card0"+str(i)+".png"))
        commonImage = commonImage.resize((64,102),Image.ANTIALIAS)
        SystemCardphoto.append (ImageTk.PhotoImage(commonImage))
        
        commonImage = Image.open(process_path(CARDPATH+"common/card0"+str(i)+".png"))
        commonImage = commonImage.resize((96,156),Image.ANTIALIAS)
        SystemCardlargephoto.append (ImageTk.PhotoImage(commonImage))
        
def init_charactor_card():
    global PowerCardphoto
    global SpellCardphoto
    global PowerCardlargephoto
    global SpellCardlargephoto
    
    PhotoFiles = os.listdir(process_path(CARDPATH))
    for charactor in PhotoFiles:
        if charactor == 'common':
            continue
        else:
            CharactorFiles = os.listdir(process_path(CARDPATH + charactor))

            PowerCardphotoList = []
            SpellCardphotoList = []
            for cards in CharactorFiles:
                cardID = int(cards[4:7])
                if cardID < 200 :
                    PowerCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    PowerCardImage = PowerCardImage.resize((64,102),Image.ANTIALIAS)
                    PowerCardphotoList.append (ImageTk.PhotoImage(PowerCardImage))
                else:
                    SpellCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    SpellCardImage = SpellCardImage.resize((64,102),Image.ANTIALIAS)
                    SpellCardphotoList.append (ImageTk.PhotoImage(SpellCardImage))

            PowerCardphoto[charactor] = PowerCardphotoList
            SpellCardphoto[charactor] = SpellCardphotoList

            PowerCardphotoList = []
            SpellCardphotoList = []
            for cards in CharactorFiles:
                cardID = int(cards[4:7])
                if cardID < 200 :
                    PowerCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    PowerCardImage = PowerCardImage.resize((96,156),Image.ANTIALIAS)
                    PowerCardphotoList.append (ImageTk.PhotoImage(PowerCardImage))
                else:
                    SpellCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    SpellCardImage = SpellCardImage.resize((96,156),Image.ANTIALIAS)
                    SpellCardphotoList.append (ImageTk.PhotoImage(SpellCardImage))

            PowerCardlargephoto[charactor] = PowerCardphotoList
            SpellCardlargephoto[charactor] = SpellCardphotoList

            
def init_card () :
    global Cards
    
    for i in range (0,24) :
        Cards[i].config(state= "disable")
        Cards[i].config(image="")
        
def system_card () :
    global Cards
    global SystemCardphoto
    
    init_card ()
    
    for i in range (0,21) :
        Cards[i].config(state= "normal")
        Cards[i].config(image=SystemCardphoto[i])
        Cards[i].config(command = lambda p = i : select_card(p))
        
def power_card () :
    global Cards
    global PowerCardphoto
    
    init_card ()

    for i in range (0,len(PowerCardphoto[CHARACTOR])) :
        Cards[i].config(state= "normal")
        Cards[i].config(image=PowerCardphoto[CHARACTOR][i])
        Cards[i].config(command = lambda p = i + 100 : select_card(p))


def spell_card () :
    global Cards
    global SpellCardphoto
    
    init_card ()

    for i in range (0,len(SpellCardphoto[CHARACTOR])) :
        Cards[i].config(state= "normal")
        Cards[i].config(image=SpellCardphoto[CHARACTOR][i])
        Cards[i].config(command = lambda p = i + 200 : select_card(p))
        
def init_userDeck (byteval) :
    global userDeck
    userDeck = []
    with open(process_path("./lib/CardData.json"),'r',encoding = 'utf-8') as t:
        CardData = json.load (t)

    st = CardData[CHARACTOR][DECKNAME][0]
    ed = CardData[CHARACTOR][DECKNAME][1] + 1
    
    for i in range (st,ed,2) :
        if byteval[i] < 100:
            userDeck.append (CardData["系统卡"][str(byteval[i])][0])
        elif byteval[i] < 200:
            userDeck.append (CardData[CHARACTOR]["必杀"][str(byteval[i])][0])
        else:
            userDeck.append (CardData[CHARACTOR]["符卡"][str(byteval[i])][0])
        
def update_userDeck () :
    global Deck
    global userDeck

    userDeck.sort ()

    for i in range (0,20) :
        Deck[i].config (state= "disable")
        Deck[i].config (image="")

    for i in range (0,len(userDeck)) :

        Deck[i].config (state= "normal")
        if userDeck[i] < 100:
            Deck[i].config(image=SystemCardphoto[userDeck[i]])
        elif userDeck[i] < 200:
            Deck[i].config(image=PowerCardphoto[CHARACTOR][userDeck[i]-100])
        else :
            Deck[i].config(image=SpellCardphoto[CHARACTOR][userDeck[i]-200])
            
        Deck[i].config(command = lambda p = userDeck[i]: select_card(p))

def select_card (cardID) :
    global selectCardID
    global select_card_label
    global select_card_label_name
    # ←→↑↓↙↘ 「」

    with open(process_path("./lib/CardData.json"),'r',encoding = 'utf-8') as t:
            CardData = json.load (t)
    
    if cardID >= 0 and cardID < 100:
        select_card_label.config(image=SystemCardlargephoto[cardID])
        select_card_label_name .config(text=CardData["系统卡"][str(cardID)][1],
                                    font=('宋体',15))
    elif cardID < 200:
        select_card_label.config(image=PowerCardlargephoto[CHARACTOR][cardID-100])
        for i in CardData[CHARACTOR]["必杀"]:
            if CardData[CHARACTOR]["必杀"][i][0] == cardID:
                select_card_label_name.config(text=CardData[CHARACTOR]["必杀"][i][1],
                                            font=('宋体',15))
    else:    
        select_card_label.config(image=SpellCardlargephoto[CHARACTOR][cardID-200])
        for i in CardData[CHARACTOR]["符卡"]:
            if CardData[CHARACTOR]["符卡"][i][0] == cardID:
                select_card_label_name.config(text=CardData[CHARACTOR]["符卡"][i][1],
                                            font=('宋体',15))
    
    selectCardID = cardID
    pass

def save_card (byteval):
    global userDeck
    global err_label
    if len (userDeck) < 20:
        print ("卡牌数不足20张")
        err_label.config(text="卡牌数不足20张",fg = "red")
        return
    if len (userDeck) > 20:
        print ("卡牌数多于20张")
        err_label.config(text="卡牌数多于20张",fg = "red")
        return
    with open(process_path("./lib/CardData.json"),'r',encoding = 'utf-8') as t:
        CardData = json.load (t)
    st = CardData[CHARACTOR][DECKNAME][0]
    ed = CardData[CHARACTOR][DECKNAME][1] + 1
    
    for i in range (0,20) :
        if userDeck[i] < 100:
            byteval[st] = userDeck[i]
        elif userDeck[i] < 200 :
            for j in CardData[CHARACTOR]["必杀"]:
                if CardData[CHARACTOR]["必杀"][j][0] == userDeck[i] :
                    byteval[st] = int(j)
                    break
        else :
            for j in CardData[CHARACTOR]["符卡"]:
                if CardData[CHARACTOR]["符卡"][j][0] == userDeck[i] :
                    byteval[st] = int(j)
                    break
        st = st + 2
        
    val = bytes (byteval)
    
    with open ((PROFILEPATH),'wb') as f:
        f.write (struct.pack("3386s",val))
        f.close()

    err_label.config(text="保存成功",fg = "green")

def add_card () :
    global userDeck
    global err_label
    
    if len (userDeck) == 20:
        print ("卡组已满")
        err_label.config(text="卡组已满",fg = "red")
        return
    if selectCardID == -1:
        print ("未选择卡")
        err_label.config(text="未选择卡",fg = "red")
        return
    Count = 0
    for i in range (0,len(userDeck)):
        if userDeck[i] == selectCardID:
            Count = Count + 1
    if Count == 4:
        print ("无法添加更多该卡")
        err_label.config(text="无法添加更多该卡",fg = "red")
        return
    
    err_label.config(text="")
    
    userDeck.append (selectCardID)
    update_userDeck()
    pass

def del_card() :
    global userDeck
    global err_label
    
    if selectCardID not in userDeck:
        print ("无法删除不存在的卡")
        err_label.config(text="无法删除不存在的卡",fg = "red")
        return
    else:
        userDeck.remove (selectCardID)
        
    err_label.config(text="")

    update_userDeck()
    pass
    
def save_catfish_deck():
    filenewpath = asksaveasfilename(filetypes=[('cfd','cfd')])
    
    if filenewpath[-4:] != '.cfd':
        filenewpath += ".cfd"
        
    byteval = []
    byteval.append (charactorID[CHARACTOR])
    byteval.append (len(userDeck))
    for i in userDeck:
        byteval.append (i)
        
    while len(byteval) < 22 :
        byteval.append (255)
    
    val = bytes (byteval) 
    with open ((filenewpath),'wb') as f:
        f.write (struct.pack("22s",val))
        f.close()
    pass
def load_catfish_deck():
    global userDeck
    global err_label

    fileloadpath = askopenfilename(filetypes=[('cfd','cfd')])

    if fileloadpath[-4:] != '.cfd':
        fileloadpath += ".cfd"

    with open ((fileloadpath),'rb') as f:
        byteval = bytearray(struct.unpack ("22s",f.read(22))[0])
    
    userDeck = []
    
    if byteval[0] == charactorID[CHARACTOR]:
        for i in range (2,byteval[1] + 2) :
            
            if byteval[i] < 100:
                userDeck.append (byteval[i])
            elif byteval[i] < 200:
                userDeck.append (byteval[i])
            else:
                userDeck.append (byteval[i])
    else:
        for i in charactorID:
            if charactorID[i] == byteval[0]:
                print ("该卡组属于\n" + i + "\n无法应用于当前角色")
                err_label.config(text="该卡组属于\n" + i + "\n无法应用于当前角色",fg = "red")
            return
        return
    update_userDeck()
    pass   

def change_deck (DeckName) :
    global chooseDeck
    global CHARACTOR
    global menubar
    global Cards
    global Deck
    global userDeck
    global selectCardID
    global err_label
    global select_card_label
    global select_card_label_name
    global DECKNAME
    
    DECKNAME = DeckName

    selectCardID = -1
    # main.destroy()
    chooseDeck.destroy()
    
    changedeck = tk.Toplevel()
    changedeck.geometry('1080x640')
    changedeck.title ("机签: " + PROFILE + " 角色: " + CHARACTOR + " 卡组: " + DeckName)
        
    menubar = Menu(changedeck)
    changedeck.config(menu=menubar)
    
    menubar.add_command(label="保存卡组",command=save_catfish_deck)
    menubar.add_command(label="载入卡组",command=load_catfish_deck)
    
    err_label = tk.Label(changedeck,text = "",
                         height=3,width=15,justify="center")
    err_label.place(x = 485,y = 520)
    
    
    select_card_label = tk.Label(changedeck)
    select_card_label.place(x = 626,y = 18)
    
    select_card_label_name = tk.Label(changedeck,
                                      text="修改完卡组后记得\n按中间的按钮来保存卡组",
                                      font=('宋体',15))
    select_card_label_name.place(x = 732,y = 18)
    # 96 156
    
    
    SystemCard = tk.Button(changedeck,command = system_card)
    SystemCard.config(text="系统卡")
    SystemCard.place(x = 27,y = 71,width=100,height=50)
    
    PowerCard = tk.Button(changedeck,command = power_card)
    PowerCard.config(text="必杀卡")
    PowerCard.place(x = 187,y = 71,width=100,height=50)
    
    SkillCard = tk.Button(changedeck,command = spell_card)
    SkillCard.config(text="符卡")
    SkillCard.place(x = 347,y = 71,width=100,height=50)
    
    Cards = []
    
    Deck = []
    
    for i in range (0,6) :
        Card = tk.Button(changedeck)
        Card.place(x = 20 + 74 * i,y = 192,width=64,height=102)
        Card.config (state= "disabled")
        Cards.append (Card)
    
    for i in range (0,6) :
        Card = tk.Button(changedeck)
        Card.place(x = 20 + 74 * i,y = 192 + 112,width=64,height=102)
        Card.config (state= "disabled")
        Cards.append (Card)
        
    for i in range (0,6) :
        Card = tk.Button(changedeck)
        Card.place(x = 20 + 74 * i,y = 192 + 112 * 2,width=64,height=102)
        Card.config (state= "disabled")
        Cards.append (Card)
        
    for i in range (0,6) :
        Card = tk.Button(changedeck)
        Card.place(x = 20 + 74 * i,y = 192 + 112 * 3,width=64,height=102)
        Card.config (state= "disabled")
        Cards.append (Card)
    
    for i in range (0,5) :
        Card = tk.Button(changedeck)
        Card.place(x = 626 + 74 * i,y = 192,width=64,height=102)
        Card.config (state= "disabled")
        Deck.append (Card)
    
    for i in range (0,5) :
        Card = tk.Button(changedeck)
        Card.place(x = 626 + 74 * i,y = 192 + 112,width=64,height=102)
        Card.config (state= "disabled")
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Button(changedeck)
        Card.place(x = 626 + 74 * i,y = 192 + 112 * 2,width=64,height=102)
        Card.config (state= "disabled")
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Button(changedeck)
        Card.place(x = 626 + 74 * i,y = 192 + 112 * 3,width=64,height=102)
        Card.config (state= "disabled")
        Deck.append (Card)

    with open ((PROFILEPATH),'rb') as f:
        byteval = bytearray(struct.unpack ("3386s",f.read(3386))[0])

    saveCard = tk.Button(changedeck,text="保存",command = lambda q = byteval : save_card(q))
    saveCard.place(x = 476,y = 211,width=128,height=64)
    
    addCard = tk.Button(changedeck,text="添加->",command = add_card)
    addCard.place(x = 476,y = 323,width=128,height=64)
    
    delCard = tk.Button(changedeck,text="<-移除",command = del_card)
    delCard.place(x = 476,y = 435,width=128,height=64)
  
    init_system_card()
    init_charactor_card()
    
    system_card()
    
    init_userDeck (byteval)

    update_userDeck ()
        
    changedeck.mainloop()
    
def choose_deck (charactor) :
    global chooseDeck
    global CHARACTOR
    global main

    CHARACTOR = charactor
    chooseDeck = tk.Toplevel()
    chooseDeck.geometry('300x150')
    chooseDeck.title ("机签: " + PROFILE + " 角色: " + CHARACTOR)
    
    JoyfulDeck = tk.Button(chooseDeck,command = lambda p="喜":change_deck(p))
    JoyfulDeck.config(text="喜")
    JoyfulDeck.place(x = 150 * 0,y = 75 * 0,width=150,height=75)
    
    AngerDeck = tk.Button(chooseDeck,command = lambda p="怒":change_deck(p))
    AngerDeck.config(text="怒")
    AngerDeck.place(x = 150 * 1,y = 75 * 0,width=150,height=75)

    LamentDeck = tk.Button(chooseDeck,command = lambda p="哀":change_deck(p))
    LamentDeck.config(text="哀")
    LamentDeck.place(x = 150 * 0,y = 75 * 1,width=150,height=75)
    
    happyDeck = tk.Button(chooseDeck,command = lambda p="乐":change_deck(p))
    happyDeck.config(text="乐")
    happyDeck.place(x = 150 * 1,y = 75 * 1,width=150,height=75)
    
    chooseDeck.mainloop()
    pass    

if __name__ == '__main__':
    global root
    global main
    
    # os.mkdir ("CatFishDeck")
    
    root = tk.Tk()
    root.title("CatFishTool")
    root.geometry("320x160")
    
    new_profile_Button = tk.Button(root, text="新建机签", command=new_profile,width=40,height=4)
    new_profile_Button.pack()
    open_profile_Button = tk.Button(root, text="载入机签", command=open_profile,width=40,height=4)
    open_profile_Button.pack()
    root.mainloop()
    
    if PROFILE != "" :
        
        main = tk.Tk()
        main.geometry('1080x640')
        main.title ("机签: " + PROFILE)
        
        Sanae = tk.Button(main,command = lambda p="东风谷早苗":choose_deck(p))
        Sanaephoto = tk.PhotoImage(file=process_path("./lib/photo/Sanae.png"))
        Sanae.config(image=Sanaephoto)
        Sanae.place(x = 108 * 0,y = 320 * 0,width=108,height=320)
        
        Cirno = tk.Button(main,command = lambda p="琪露诺":choose_deck(p))
        Cirnophoto = tk.PhotoImage(file=process_path("./lib/photo/Cirno.png"))
        Cirno.config(image=Cirnophoto)
        Cirno.place(x = 108 * 1,y = 320 * 0,width=108,height=320)
        
        Meirin = tk.Button(main,command = lambda p="红美铃":choose_deck(p))
        Meirinphoto = tk.PhotoImage(file=process_path("./lib/photo/Meirin.png"))
        Meirin.config(image=Meirinphoto)
        Meirin.place(x = 108 * 2,y = 320 * 0,width=108,height=320)
        
        Utuho = tk.Button(main,command = lambda p="灵乌路空":choose_deck(p))
        Utuhophoto = tk.PhotoImage(file=process_path("./lib/photo/Utuho.png"))
        Utuho.config(image=Utuhophoto)
        Utuho.place(x = 108 * 3,y = 320 * 0,width=108,height=320)

        Suwako = tk.Button(main,command = lambda p="洩矢诹访子":choose_deck(p))
        Suwakophoto = tk.PhotoImage(file=process_path("./lib/photo/Suwako.png"))
        Suwako.config(image=Suwakophoto)
        Suwako.place(x = 108 * 4,y = 320 * 0,width=108,height=320)
        
        Reimu = tk.Button(main,command = lambda p="博丽灵梦":choose_deck(p))
        Reimuphoto = tk.PhotoImage(file=process_path("./lib/photo/Reimu.png"))
        Reimu.config(image=Reimuphoto)
        Reimu.place(x = 108 * 5,y = 320 * 0,width=108,height=320)  
        
        Marisa = tk.Button(main,command = lambda p="雾雨魔理沙":choose_deck(p))
        Marisaphoto = tk.PhotoImage(file=process_path("./lib/photo/Marisa.png"))
        Marisa.config(image=Marisaphoto)
        Marisa.place(x = 108 * 6,y = 320 * 0,width=108,height=320)  
        
        Alice = tk.Button(main,command = lambda p="爱丽丝·玛格特洛依德":choose_deck(p))
        Alicephoto = tk.PhotoImage(file=process_path("./lib/photo/Alice.png"))
        Alice.config(image=Alicephoto)
        Alice.place(x = 108 * 7,y = 320 * 0,width=108,height=320)  
        
        Patchouli = tk.Button(main,command = lambda p="帕秋莉·诺蕾姬":choose_deck(p))
        Patchouliphoto = tk.PhotoImage(file=process_path("./lib/photo/Patchouli.png"))
        Patchouli.config(image=Patchouliphoto)
        Patchouli.place(x = 108 * 8,y = 320 * 0,width=108,height=320)  
        
        Sakuya = tk.Button(main,command = lambda p="十六夜咲夜":choose_deck(p))
        Sakuyaphoto = tk.PhotoImage(file=process_path("./lib/photo/Sakuya.png"))
        Sakuya.config(image=Sakuyaphoto)
        Sakuya.place(x = 108 * 9,y = 320 * 0,width=108,height=320)  
        
        Youmu = tk.Button(main,command = lambda p="魂魄妖梦":choose_deck(p))
        Youmuphoto = tk.PhotoImage(file=process_path("./lib/photo/Youmu.png"))
        Youmu.config(image=Youmuphoto)
        Youmu.place(x = 108 * 0,y = 320 * 1,width=108,height=320)  
        
        Yuyuko = tk.Button(main,command = lambda p="西行寺幽幽子":choose_deck(p))
        Yuyukophoto = tk.PhotoImage(file=process_path("./lib/photo/Yuyuko.png"))
        Yuyuko.config(image=Yuyukophoto)
        Yuyuko.place(x = 108 * 1,y = 320 * 1,width=108,height=320)  

        Remilia = tk.Button(main,command = lambda p="蕾米莉亚·斯卡蕾特":choose_deck(p))
        Remiliaphoto = tk.PhotoImage(file=process_path("./lib/photo/Remilia.png"))
        Remilia.config(image=Remiliaphoto)
        Remilia.place(x = 108 * 2,y = 320 * 1,width=108,height=320)  
        
        Yukari = tk.Button(main,command = lambda p="八云紫":choose_deck(p))
        Yukariphoto = tk.PhotoImage(file=process_path("./lib/photo/Yukari.png"))
        Yukari.config(image=Yukariphoto)
        Yukari.place(x = 108 * 3,y = 320 * 1,width=108,height=320)  
        
        Suika = tk.Button(main,command = lambda p="伊吹萃香":choose_deck(p))
        Suikaphoto = tk.PhotoImage(file=process_path("./lib/photo/Suika.png"))
        Suika.config(image=Suikaphoto)
        Suika.place(x = 108 * 4,y = 320 * 1,width=108,height=320)  
        
        Reisen = tk.Button(main,command = lambda p="铃仙·优昙华院·因幡":choose_deck(p))
        Reisenphoto = tk.PhotoImage(file=process_path("./lib/photo/Reisen.png"))
        Reisen.config(image=Reisenphoto)
        Reisen.place(x = 108 * 5,y = 320 * 1,width=108,height=320)  
        
        Aya = tk.Button(main,command = lambda p="射命丸文":choose_deck(p))
        Ayaphoto = tk.PhotoImage(file=process_path("./lib/photo/Aya.png"))
        Aya.config(image=Ayaphoto)
        Aya.place(x = 108 * 6,y = 320 * 1,width=108,height=320)  
        
        Komachi = tk.Button(main,command = lambda p="小野塚小町":choose_deck(p))
        Komachiphoto = tk.PhotoImage(file=process_path("./lib/photo/Komachi.png"))
        Komachi.config(image=Komachiphoto)
        Komachi.place(x = 108 * 7,y = 320 * 1,width=108,height=320)  
        
        Iku = tk.Button(main,command = lambda p="永江衣玖":choose_deck(p))
        Ikuphoto = tk.PhotoImage(file=process_path("./lib/photo/Iku.png"))
        Iku.config(image=Ikuphoto)
        Iku.place(x = 108 * 8,y = 320 * 1,width=108,height=320)  
        
        Tenshi = tk.Button(main,command = lambda p="比那名居天子":choose_deck(p))
        Tenshiphoto = tk.PhotoImage(file=process_path("./lib/photo/Tenshi.png"))
        Tenshi.config(image=Tenshiphoto)
        Tenshi.place(x = 108 * 9,y = 320 * 1,width=108,height=320)  
        
        
        main.mainloop()