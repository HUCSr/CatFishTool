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

replyID = {
    0 : ["博丽灵梦","Reimu"],
    1 : ["雾雨魔理沙","Marisa"],
    2 : ["十六夜咲夜","Sakuya"],
    3 : ["爱丽丝·玛格特洛依德","Alice"],
    4 : ["帕秋莉·诺蕾姬","Patchouli"],
    5 : ["魂魄妖梦","Youmu"],
    6 : ["蕾米莉亚·斯卡蕾特","Remilia"],
    7 : ["西行寺幽幽子","Yuyuko"],
    8 : ["八云紫","Yukari"],
    9 : ["伊吹萃香","Suika"],
    10 : ["铃仙·优昙华院·因幡","Reisen"],
    11 : ["射命丸文","Aya"],
    12 : ["小野塚小町","Komachi"],
    13 : ["永江衣玖","Iku"],
    14 : ["比那名居天子","Tenshi"],
    15 : ["东风谷早苗","Sanae"],
    16 : ["琪露诺","Cirno"],
    17 : ["红美铃","Meirin"],
    18 : ["灵乌路空","Utuho"],
    19 : ["洩矢诹访子","Suwako"]
}

def init_system_card (w,h) :
    global SystemCardphoto
    global SystemCardlargephoto
    for i in range (0,10) :
        commonImage = Image.open(process_path(CARDPATH+"common/card00"+str(i)+".png"))
        commonImage = commonImage.resize((w,h),Image.Resampling.LANCZOS)
        SystemCardphoto.append (ImageTk.PhotoImage(commonImage))
        
        commonImage = Image.open(process_path(CARDPATH+"common/card00"+str(i)+".png"))
        commonImage = commonImage.resize((96,156),Image.Resampling.LANCZOS)
        SystemCardlargephoto.append (ImageTk.PhotoImage(commonImage))
        
    for i in range (10,21) :
        commonImage = Image.open(process_path(CARDPATH+"common/card0"+str(i)+".png"))
        commonImage = commonImage.resize((w,h),Image.Resampling.LANCZOS)
        SystemCardphoto.append (ImageTk.PhotoImage(commonImage))
        
        commonImage = Image.open(process_path(CARDPATH+"common/card0"+str(i)+".png"))
        commonImage = commonImage.resize((96,156),Image.Resampling.LANCZOS)
        SystemCardlargephoto.append (ImageTk.PhotoImage(commonImage))
        
def init_charactor_card(w,h):
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
                    PowerCardImage = PowerCardImage.resize((w,h),Image.Resampling.LANCZOS)
                    PowerCardphotoList.append (ImageTk.PhotoImage(PowerCardImage))
                else:
                    SpellCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    SpellCardImage = SpellCardImage.resize((w,h),Image.Resampling.LANCZOS)
                    SpellCardphotoList.append (ImageTk.PhotoImage(SpellCardImage))

            PowerCardphoto[charactor] = PowerCardphotoList
            SpellCardphoto[charactor] = SpellCardphotoList

            PowerCardphotoList = []
            SpellCardphotoList = []
            for cards in CharactorFiles:
                cardID = int(cards[4:7])
                if cardID < 200 :
                    PowerCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    PowerCardImage = PowerCardImage.resize((96,156),Image.Resampling.LANCZOS)
                    PowerCardphotoList.append (ImageTk.PhotoImage(PowerCardImage))
                else:
                    SpellCardImage = Image.open(process_path(CARDPATH + charactor + "/" + cards))
                    SpellCardImage = SpellCardImage.resize((96,156),Image.Resampling.LANCZOS)
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
    
    for i in range (st,ed+1,2) :
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

def change_DeckName (DeckName) :
    global DECKNAME
    global CHARACTOR
    global changedeck

    DECKNAME = DeckName
    
    changedeck.title ("机签: " + PROFILE + " 角色: " + CHARACTOR + " 卡组: " + DeckName)

    with open ((PROFILEPATH),'rb') as f:
        byteval = bytearray(struct.unpack ("3386s",f.read(3386))[0])
        
    init_userDeck (byteval)

    update_userDeck ()


def change_deck (charactor) :
    global CHARACTOR
    global menubar
    global Cards
    global Deck
    global userDeck
    global selectCardID
    global err_label
    global select_card_label
    global select_card_label_name
    global changedeck
    
    DeckName = " "
    
    CHARACTOR = charactor

    selectCardID = -1
    
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

        
    JoyfulDeck = tk.Button(changedeck,command = lambda p="喜":change_DeckName(p))
    JoyfulDeckImage = Image.open(process_path("./lib/photo/kidoairaku.png"))
    w,h = JoyfulDeckImage.size
    left = 0
    right = w*1/5
    upper = 0
    lower = h
    JoyfulDeckImage = JoyfulDeckImage.crop([left,upper,right,lower])
    JoyfulDeckImage = JoyfulDeckImage.resize((64,64),Image.Resampling.LANCZOS)
    JoyfulDeckImage = ImageTk.PhotoImage (JoyfulDeckImage)
    JoyfulDeck.config(image=JoyfulDeckImage)
    JoyfulDeck.place(x = 1001,y = 211,width=64,height=64)
    
    AngerDeck = tk.Button(changedeck,command = lambda p="怒":change_DeckName(p))
    AngerDeckImage = Image.open(process_path("./lib/photo/kidoairaku.png"))
    w,h = AngerDeckImage.size
    left = w*1/5
    right = w*2/5
    upper = 0
    lower = h
    AngerDeckImage = AngerDeckImage.crop([left,upper,right,lower])
    AngerDeckImage = AngerDeckImage.resize((64,64),Image.Resampling.LANCZOS)
    AngerDeckImage = ImageTk.PhotoImage (AngerDeckImage)
    AngerDeck.config(image=AngerDeckImage)
    AngerDeck.place(x = 1001,y = 323,width=64,height=64)
    
    LamentDeck = tk.Button(changedeck,command = lambda p="哀":change_DeckName(p))
    LamentDeckImage = Image.open(process_path("./lib/photo/kidoairaku.png"))
    w,h = LamentDeckImage.size
    left = w*2/5
    right = w*3/5
    upper = 0
    lower = h
    LamentDeckImage = LamentDeckImage.crop([left,upper,right,lower])
    LamentDeckImage = LamentDeckImage.resize((64,64),Image.Resampling.LANCZOS)
    LamentDeckImage = ImageTk.PhotoImage (LamentDeckImage)
    LamentDeck.config(image=LamentDeckImage)
    LamentDeck.place(x = 1001,y = 435,width=64,height=64)
    
    happyDeck = tk.Button(changedeck,command = lambda p="乐":change_DeckName(p))
    happyDeckImage = Image.open(process_path("./lib/photo/kidoairaku.png"))
    w,h = happyDeckImage.size
    left = w*3/5
    right = w*4/5
    upper = 0
    lower = h
    happyDeckImage = happyDeckImage.crop([left,upper,right,lower])
    happyDeckImage = happyDeckImage.resize((64,64),Image.Resampling.LANCZOS)
    happyDeckImage = ImageTk.PhotoImage (happyDeckImage)
    happyDeck.config(image=happyDeckImage)
    happyDeck.place(x = 1001,y = 547,width=64,height=64)
    
    with open ((PROFILEPATH),'rb') as f:
        byteval = bytearray(struct.unpack ("3386s",f.read(3386))[0])
    
    saveCard = tk.Button(changedeck,text="保存",command = lambda q = byteval : save_card(q))
    saveCard.place(x = 476,y = 211,width=128,height=64)
    
    addCard = tk.Button(changedeck,text="添加->",command = add_card)
    addCard.place(x = 476,y = 323,width=128,height=64)
    
    delCard = tk.Button(changedeck,text="<-移除",command = del_card)
    delCard.place(x = 476,y = 435,width=128,height=64)
  
    init_system_card(64,102)
    init_charactor_card(64,102)
    
    system_card()
        
    changedeck.mainloop()


    
def deck_menu():
    main = tk.Tk()
    main.geometry('1080x640')
    main.title ("机签: " + PROFILE)

    Sanae = tk.Button(main,command = lambda p="东风谷早苗":change_deck(p))
    Sanaephoto = Image.open(process_path("./lib/photo/Sanae.png"))
    w,h = Sanaephoto.size
    left = 0
    right = 9*w/10
    upper = 0
    lower = 9*h/10
    Sanaephoto = Sanaephoto.crop([left,upper,right,lower])
    Sanaephoto = ImageTk.PhotoImage(Sanaephoto)
    Sanae.config(image=Sanaephoto)
    Sanae.place(x = 108 * 0,y = 320 * 0,width=108,height=320)

    Cirno = tk.Button(main,command = lambda p="琪露诺":change_deck(p))
    Cirnophoto = Image.open(process_path("./lib/photo/Cirno.png"))
    w,h = Cirnophoto.size
    left = w/10
    right = w
    upper = 0
    lower = 9*h/10
    Cirnophoto = Cirnophoto.crop([left,upper,right,lower])
    Cirnophoto = ImageTk.PhotoImage(Cirnophoto)
    Cirno.config(image=Cirnophoto)
    Cirno.place(x = 108 * 1,y = 320 * 0,width=108,height=320)

    Meirin = tk.Button(main,command = lambda p="红美铃":change_deck(p))
    Meirinphoto = Image.open(process_path("./lib/photo/Meirin.png"))
    w,h = Meirinphoto.size
    left = 0
    right = w
    upper = 0
    lower = 9*h/10
    Meirinphoto = Meirinphoto.crop([left,upper,right,lower])
    Meirinphoto = ImageTk.PhotoImage(Meirinphoto)
    Meirin.config(image=Meirinphoto)
    Meirin.place(x = 108 * 2,y = 320 * 0,width=108,height=320)

    Utuho = tk.Button(main,command = lambda p="灵乌路空":change_deck(p))
    Utuhophoto = Image.open(process_path("./lib/photo/Utuho.png"))
    w,h = Utuhophoto.size
    left = w/10
    right = 19*w/20
    upper = 0
    lower = 9*h/10
    Utuhophoto = Utuhophoto.crop([left,upper,right,lower])
    Utuhophoto = ImageTk.PhotoImage(Utuhophoto)
    Utuho.config(image=Utuhophoto)
    Utuho.place(x = 108 * 3,y = 320 * 0,width=108,height=320)   
    Suwako = tk.Button(main,command = lambda p="洩矢诹访子":change_deck(p))
    Suwakophoto = Image.open(process_path("./lib/photo/Suwako.png"))
    w,h = Suwakophoto.size
    left = 0
    right = 9*w/10
    upper = 0
    lower = 8*h/10
    Suwakophoto = Suwakophoto.crop([left,upper,right,lower])
    Suwakophoto = ImageTk.PhotoImage(Suwakophoto)
    Suwako.config(image=Suwakophoto)
    Suwako.place(x = 108 * 4,y = 320 * 0,width=108,height=320)

    Reimu = tk.Button(main,command = lambda p="博丽灵梦":change_deck(p))
    Reimuphoto = Image.open(process_path("./lib/photo/Reimu.png"))
    w,h = Reimuphoto.size
    left = 0
    right = 9*w/10
    upper = 0
    lower = 9*h/10
    Reimuphoto = Reimuphoto.crop([left,upper,right,lower])
    Reimuphoto = ImageTk.PhotoImage(Reimuphoto)
    Reimu.config(image=Reimuphoto)
    Reimu.place(x = 108 * 5,y = 320 * 0,width=108,height=320)  

    Marisa = tk.Button(main,command = lambda p="雾雨魔理沙":change_deck(p))
    Marisaphoto = Image.open(process_path("./lib/photo/Marisa.png"))
    w,h = Marisaphoto.size
    left = 0
    right = 7*w/10
    upper = 0
    lower = h
    Marisaphoto = Marisaphoto.crop([left,upper,right,lower])
    Marisaphoto = ImageTk.PhotoImage(Marisaphoto)
    Marisa.config(image=Marisaphoto)
    Marisa.place(x = 108 * 6,y = 320 * 0,width=108,height=320)  

    Alice = tk.Button(main,command = lambda p="爱丽丝·玛格特洛依德":change_deck(p))
    Alicephoto = Image.open(process_path("./lib/photo/Alice.png"))
    w,h = Alicephoto.size
    left = 0
    right = 9*w/10
    upper = 0
    lower = 8*h/10
    Alicephoto = Alicephoto.crop([left,upper,right,lower])
    Alicephoto = ImageTk.PhotoImage(Alicephoto)
    Alice.config(image=Alicephoto)
    Alice.place(x = 108 * 7,y = 320 * 0,width=108,height=320)  

    Patchouli = tk.Button(main,command = lambda p="帕秋莉·诺蕾姬":change_deck(p))
    Patchouliphoto = Image.open(process_path("./lib/photo/Patchouli.png"))
    w,h = Patchouliphoto.size
    left = w/20
    right = w
    upper = 0
    lower = 9*h/10
    Patchouliphoto = Patchouliphoto.crop([left,upper,right,lower])
    Patchouliphoto = ImageTk.PhotoImage(Patchouliphoto)
    Patchouli.config(image=Patchouliphoto)
    Patchouli.place(x = 108 * 8,y = 320 * 0,width=108,height=320)  

    Sakuya = tk.Button(main,command = lambda p="十六夜咲夜":change_deck(p))
    Sakuyaphoto = Image.open(process_path("./lib/photo/Sakuya.png"))
    w,h = Sakuyaphoto.size
    left = w/20
    right = w
    upper = 0
    lower = 8*h/10
    Sakuyaphoto = Sakuyaphoto.crop([left,upper,right,lower])
    Sakuyaphoto = ImageTk.PhotoImage(Sakuyaphoto)
    Sakuya.config(image=Sakuyaphoto)
    Sakuya.place(x = 108 * 9,y = 320 * 0,width=108,height=320)  

    Youmu = tk.Button(main,command = lambda p="魂魄妖梦":change_deck(p))
    Youmuphoto = Image.open(process_path("./lib/photo/Youmu.png"))
    w,h = Youmuphoto.size
    left = 0
    right = w
    upper = 0
    lower = h*19/20
    Youmuphoto = Youmuphoto.crop([left,upper,right,lower])
    Youmuphoto = ImageTk.PhotoImage(Youmuphoto)
    Youmu.config(image=Youmuphoto)
    Youmu.place(x = 108 * 0,y = 320 * 1,width=108,height=320)  

    Yuyuko = tk.Button(main,command = lambda p="西行寺幽幽子":change_deck(p))
    Yuyukophoto = Image.open(process_path("./lib/photo/Yuyuko.png"))
    w,h = Yuyukophoto.size
    left = 0
    right = w
    upper = 0
    lower = h*9/10
    Yuyukophoto = Yuyukophoto.crop([left,upper,right,lower])
    Yuyukophoto = ImageTk.PhotoImage(Yuyukophoto)
    Yuyuko.config(image=Yuyukophoto)
    Yuyuko.place(x = 108 * 1,y = 320 * 1,width=108,height=320)      
    Remilia = tk.Button(main,command = lambda p="蕾米莉亚·斯卡蕾特":change_deck(p))
    Remiliaphoto = Image.open(process_path("./lib/photo/Remilia.png"))
    w,h = Remiliaphoto.size
    left = 0
    right = w*19/20
    upper = 0
    lower = h*19/20
    Remiliaphoto = Remiliaphoto.crop([left,upper,right,lower])
    Remiliaphoto = ImageTk.PhotoImage(Remiliaphoto)
    Remilia.config(image=Remiliaphoto)
    Remilia.place(x = 108 * 2,y = 320 * 1,width=108,height=320)  

    Yukari = tk.Button(main,command = lambda p="八云紫":change_deck(p))
    Yukariphoto = Image.open(process_path("./lib/photo/Yukari.png"))
    w,h = Yukariphoto.size
    left = 0
    right = w*19/20
    upper = 0
    lower = h*17/20
    Yukariphoto = Yukariphoto.crop([left,upper,right,lower])
    Yukariphoto = ImageTk.PhotoImage(Yukariphoto)
    Yukari.config(image=Yukariphoto)
    Yukari.place(x = 108 * 3,y = 320 * 1,width=108,height=320)  

    Suika = tk.Button(main,command = lambda p="伊吹萃香":change_deck(p))
    Suikaphoto = Image.open(process_path("./lib/photo/Suika.png"))
    w,h = Suikaphoto.size
    left = 5*w/10
    right = w
    upper = 0
    lower = h
    Suikaphoto = Suikaphoto.crop([left,upper,right,lower])
    Suikaphoto = ImageTk.PhotoImage(Suikaphoto)
    Suika.config(image=Suikaphoto)
    Suika.place(x = 108 * 4,y = 320 * 1,width=108,height=320)  

    Reisen = tk.Button(main,command = lambda p="铃仙·优昙华院·因幡":change_deck(p))
    Reisenphoto = Image.open(process_path("./lib/photo/Reisen.png"))
    w,h = Reisenphoto.size
    left = 0
    right = w*19/20
    upper = 0
    lower = h*19/20
    Reisenphoto = Reisenphoto.crop([left,upper,right,lower])
    Reisenphoto = ImageTk.PhotoImage(Reisenphoto)
    Reisen.config(image=Reisenphoto)
    Reisen.place(x = 108 * 5,y = 320 * 1,width=108,height=320)  

    Aya = tk.Button(main,command = lambda p="射命丸文":change_deck(p))
    Ayaphoto = Image.open(process_path("./lib/photo/Aya.png"))
    w,h = Ayaphoto.size
    left = 0
    right = w*8/10
    upper = 0
    lower = h*8/10
    Ayaphoto = Ayaphoto.crop([left,upper,right,lower])
    Ayaphoto = ImageTk.PhotoImage(Ayaphoto)
    Aya.config(image=Ayaphoto)
    Aya.place(x = 108 * 6,y = 320 * 1,width=108,height=320)  

    Komachi = tk.Button(main,command = lambda p="小野塚小町":change_deck(p))
    Komachiphoto = Image.open(process_path("./lib/photo/Komachi.png"))
    w,h = Komachiphoto.size
    left = 0
    right = w
    upper = 0
    lower = h*8/10
    Komachiphoto = Komachiphoto.crop([left,upper,right,lower])
    Komachiphoto = ImageTk.PhotoImage(Komachiphoto)
    Komachi.config(image=Komachiphoto)
    Komachi.place(x = 108 * 7,y = 320 * 1,width=108,height=320)  

    Iku = tk.Button(main,command = lambda p="永江衣玖":change_deck(p))
    Ikuphoto = Image.open(process_path("./lib/photo/Iku.png"))
    w,h = Ikuphoto.size
    left = w/10
    right = w
    upper = 0
    lower = h
    Ikuphoto = Ikuphoto.crop([left,upper,right,lower])
    Ikuphoto = ImageTk.PhotoImage(Ikuphoto)
    Iku.config(image=Ikuphoto)
    Iku.place(x = 108 * 8,y = 320 * 1,width=108,height=320)  

    Tenshi = tk.Button(main,command = lambda p="比那名居天子":change_deck(p))
    Tenshiphoto = Image.open(process_path("./lib/photo/Tenshi.png"))
    w,h = Tenshiphoto.size
    left = 0
    right = w*9/10
    upper = 0
    lower = h*8/10
    Tenshiphoto = Tenshiphoto.crop([left,upper,right,lower])
    Tenshiphoto = ImageTk.PhotoImage(Tenshiphoto)
    Tenshi.config(image=Tenshiphoto)
    Tenshi.place(x = 108 * 9,y = 320 * 1,width=108,height=320)  


    main.mainloop()
    
def save_reply_deck (deckName,byteval):
    if os.path.exists("CatFishDeck"):
        pass
    else:
        os.mkdir("CatFishDeck")
    filenewpath = "./CatFishDeck/" + deckName + ".cfd"
    
    _byteval = []
    _byteval.append (charactorID[deckName.split('-')[0]])
    _byteval.append (20)
    
    with open(process_path("./lib/CardData.json"),'r',encoding = 'utf-8') as t:
        CardData = json.load (t)
        
    
    for i in range (0,len(byteval),2):
        if byteval[i] < 100:
            _byteval.append (CardData["系统卡"][str(byteval[i])][0])
        elif byteval[i] < 200:
            _byteval.append (CardData[deckName.split('-')[0]]["必杀"][str(byteval[i])][0])
        else:
            _byteval.append (CardData[deckName.split('-')[0]]["符卡"][str(byteval[i])][0])
        
    val = bytes (_byteval) 
    with open ((filenewpath),'wb') as f:
        f.write (struct.pack("22s",val))
        f.close()
    
def reply_menu (replyName,byteval):
    
    global CHARACTOR
    
    main = tk.Tk()
    main.geometry('960x480')
    main.title (replyName)
    P1 = tk.Label(main, relief=tk.GROOVE)
    P1photo = Image.open(process_path("./lib/photo/"+replyID[byteval[14]][1]+".png"))
    P1photo = ImageTk.PhotoImage(P1photo.resize((480,480),Image.Resampling.LANCZOS))
    P1.config(image=P1photo)
    P1.place(x = 0,y = 0,width=480,height=480)
    
    P2 = tk.Label(main, relief=tk.GROOVE)
    P2photo = Image.open(process_path("./lib/photo/"+replyID[byteval[63]][1]+".png"))
    P2photo = P2photo.transpose(Image.FLIP_LEFT_RIGHT)
    P2photo = ImageTk.PhotoImage(P2photo.resize((480,480),Image.Resampling.LANCZOS))
    P2.config(image=P2photo)
    P2.place(x = 480,y = 0,width=480,height=480)
    
    Deck = []
    
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 5 + 55 * i,y = 475 - 80 * 4 - 5 * 3,width=50,height=80)
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 5 + 55 * i,y = 475 - 80 * 3 - 5 * 2,width=50,height=80)
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 5 + 55 * i,y = 475 - 80 * 2 - 5 * 1,width=50,height=80)
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 5 + 55 * i,y = 475 - 80 * 1 - 5 * 0,width=50,height=80)
        Deck.append (Card)

    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 955 - 50 * (5-i) - 5 * (5-i-1),y = 475 - 80 * 4 - 5 * 3,width=50,height=80)
        Deck.append (Card)
    
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 955 - 50 * (5-i) - 5 * (5-i-1),y = 475 - 80 * 3 - 5 * 2,width=50,height=80)
        Deck.append (Card)
    
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 955 - 50 * (5-i) - 5 * (5-i-1),y = 475 - 80 * 2 - 5 * 1,width=50,height=80)
        Deck.append (Card)
        
    for i in range (0,5) :
        Card = tk.Label(main, relief=tk.RAISED)
        Card.place(x = 955 - 50 * (5-i) - 5 * (5-i-1),y = 475 - 80 * 1 - 5 * 0,width=50,height=80)
        Deck.append (Card)
           
    init_system_card(50,80)
    
    init_charactor_card(50,80)
    
    with open(process_path("./lib/CardData.json"),'r',encoding = 'utf-8') as t:
        CardData = json.load (t)
        
    st = 20
    
    CHARACTOR = replyID[byteval[14]][0]
    
    for i in range (0,20) :
        if byteval[st] < 100:
            Deck[i].config (image = 
                            SystemCardphoto[CardData["系统卡"][str(byteval[st])][0]])
        elif byteval[st] < 200:
            Deck[i].config (image = 
                            PowerCardphoto[CHARACTOR][CardData[CHARACTOR]["必杀"][str(byteval[st])][0] - 100])
        else:
            Deck[i].config (image = 
                            SpellCardphoto[CHARACTOR][CardData[CHARACTOR]["符卡"][str(byteval[st])][0] - 200])
        st = st + 2
        
    st = 69
    
    CHARACTOR = replyID[byteval[63]][0]
    
    for i in range (20,40) :
        if byteval[st] < 100:
            Deck[i].config (image = 
                            SystemCardphoto[CardData["系统卡"][str(byteval[st])][0]])
        elif byteval[st] < 200:
            Deck[i].config (image = 
                            PowerCardphoto[CHARACTOR][CardData[CHARACTOR]["必杀"][str(byteval[st])][0] - 100])
        else:
            Deck[i].config (image = 
                            SpellCardphoto[CHARACTOR][CardData[CHARACTOR]["符卡"][str(byteval[st])][0] - 200])
        st = st + 2
    
    Save1P = tk.Button(main,command = 
                       lambda p=replyID[byteval[14]][0] + "-" + replyName,
                       q = byteval[20:60]
                       :save_reply_deck(p,q),text="保存卡组")
    Save1P.place (x = 325,y = 285,width=105,height=45)
    
    Save2P = tk.Button(main,command = 
                       lambda p=replyID[byteval[63]][0] + "-" + replyName,
                       q = byteval[69:109]
                       :save_reply_deck(p,q),text="保存卡组")
    Save2P.place (x = 530,y = 285,width=105,height=45)
    # 282.5 - 22.5
    # 255
    # 127.5
    main.mainloop()
    return
    
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
    deck_menu()
    
def open_profile() :
    global PROFILE
    global PROFILEPATH
    PROFILEPATH = askopenfilename(filetypes=[('profile','pf')])
    if PROFILEPATH[-3:] != '.pf':
        PROFILEPATH += ".pf"
    profilename = PROFILEPATH.split('/')[-1][:-3]
    PROFILE = profilename
    root.destroy()
    deck_menu()

def load_reply() :
    replyPath = askopenfilename(filetypes=[('reply','rep')])
    if replyPath[-4:] != '.rep':
        replyPath += ".rep"
    replyName = replyPath.split('/')[-1][:-4]
    with open ((replyPath),'rb') as f:
        byteval = bytearray(struct.unpack ("108s",f.read(108))[0])

    root.destroy()
  
    reply_menu(replyName,byteval)
    
if __name__ == '__main__':
    global root
    global main
    
    # os.mkdir ("CatFishDeck")
    
    root = tk.Tk()
    root.title("CatFishTool")
    root.geometry("320x240")
    
    new_profile_Button = tk.Button(root, text="新建机签", command=new_profile,width=40,height=4)
    new_profile_Button.pack()
    open_profile_Button = tk.Button(root, text="修改卡组", command=open_profile,width=40,height=4)
    open_profile_Button.pack()
    load_reply_Button = tk.Button(root, text="提取录像卡组", command=load_reply,width=40,height=4)
    load_reply_Button.pack()
    root.mainloop()