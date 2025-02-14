global voicempfile
global mention
global globalfile
global proxies
global backup_token
global delay
global proxytype
global alive_token
global ffmpegfile
global alive_proxies
global tokens
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
import os
import old.gui.icon
import asyncio
import subprocess
import urllib.parse
import urllib.request
import urllib
import requests
import time
import datetime
delay = 0
tokens = []
alive_token = []
backup_token = []
proxies = []
alive_proxies = []
root = tk.Tk()
ffmpegfile = None
voicempfile = None
statussussy = 'Active'
root.title('SussyRaider status: ' + str(statussussy) + ' thread: ' + str(threading.active_count()))
root.geometry('1120x630')
root.configure(bg='grey13')
data = old.gui.icon.geticon()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))
import old.gui.raidtool.tokentool.fastchecker
import old.gui.raidtool.spamtool.joiner
import old.gui.raidtool.spamtool.leaver
import old.gui.raidtool.spamtool.spammer.spammer
import old.gui.raidtool.spamtool.nick
import old.gui.raidtool.spamtool.avator
import old.gui.raidtool.spamtool.friend
import old.gui.raidtool.spamtool.dm
import old.gui.raidtool.spamtool.vc
import old.gui.raidtool.spamtool.reaction
import old.gui.raidtool.spamtool.ticket
import old.gui.raidtool.spamtool.report
import old.gui.raidtool.proxy
globalfile = None
proxytype = ''

def token_filepath():
    global tokens
    fTyp = [('', '*')]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile)
    try:
        tokens = open(iFilePath, 'r').read().splitlines()
    except:
        print('ファイルパスを指定してください')
        return None
    for token in tokens:
        print('[+] Load: ' + token)
    print('Success', 'Load Tokens: ' + str(len(tokens)))

def tokenbutton():
    threading.Thread(target=FastChecker).start()

def FastChecker():
    global alive_token
    global backup_token
    token_filepath()
    if proxyset.get() and alive_proxies == []:
        messagebox.showerror('Error', 'Please load the proxies')
        return
    loop = None
    loop = asyncio.new_event_loop()
    if proxyset.get():
        old.gui.raidtool.tokentool.fastchecker.check(tokens, True, delay, loop)
    else:
        old.gui.raidtool.tokentool.fastchecker.check(tokens, False, delay, loop)
    alive_token = []
    alive_token = old.gui.raidtool.tokentool.fastchecker.alive_token
    backup_token = []
    backup_token = old.gui.raidtool.tokentool.fastchecker.alive_token
    print(backup_token)
    print('Success', 'Tokens: ' + str(len(alive_token)))
    tokenlabel.set('Tokens: ' + str(len(alive_token)))
    tokenscale.set('Tokenrange: ' + str(len(alive_token)))
    dt_now = datetime.datetime.now()
    time = dt_now.strftime('%Y-%m-%d-%H-%M-%S')
    tokenpath = os.path.join(os.getcwd(), 'tokens.txt')
    f = open(tokenpath, 'w')
    for token in alive_token:
        f.write(token + '\n')
    f.close()

def proxy_filepath():
    global proxies
    fTyp = [('', '*')]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile)
    try:
        proxies = open(iFilePath, 'r').read().splitlines()
    except Exception as err:
        print('ファイルパスを指定してください err: ' + str(err))
        return None
    for proxy in proxies:
        print('[+] Load: ' + proxy)
    print('Success', 'Load Proxies: ' + str(len(proxies)))

def proxytypeselect():
    root5 = tk.Tk()
    root5.title('ProxyType')
    root5.geometry('180x180')
    root5.configure(bg='grey13')

    def socks4():
        global proxytype
        proxytype = 'socks4'
        root5.destroy()

    def socks5():
        global proxytype
        proxytype = 'socks5'
        root5.destroy()

    def http():
        global proxytype
        proxytype = 'http'
        root5.destroy()

    def https():
        global proxytype
        proxytype = 'https'
        root5.destroy()

    def close():
        proxytype = ''
        root5.destroy()
    socks4b = tk.Button(root5, text='socks4', command=socks4, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
    socks4b.place(x=10, y=10)
    socks5b = tk.Button(root5, text='socks5', command=socks5, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
    socks5b.place(x=10, y=40)
    httpb = tk.Button(root5, text='http', command=http, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
    httpb.place(x=10, y=70)
    httpsb = tk.Button(root5, text='https', command=https, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
    httpsb.place(x=10, y=100)
    closeb = tk.Button(root5, text='close', command=close, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
    closeb.place(x=10, y=130)
    root5.mainloop()

def proxybutton():
    threading.Thread(target=proxyChecker).start()

def proxyChecker():
    global alive_proxies
    proxytypeselect()
    print(proxytype)
    if proxytype == '':
        print('Cancel proxy')
        return
    proxy_filepath()
    print('Success', 'proxytype: ' + proxytype)
    old.gui.raidtool.proxy.requests_proxy(proxies, proxytype)
    alive_proxies = []
    alive_proxies = old.gui.raidtool.proxy.alive_proxy
    print('Success', 'Proxies: ' + str(len(alive_proxies)))
    proxylabel.set('Proxies: ' + str(len(alive_proxies)))
    dt_now = datetime.datetime.now()
    proxiespath = os.path.join(os.getcwd(), 'proxies.txt')
    f = open(proxiespath, 'w')
    for proxy in alive_proxies:
        f.write(proxy + '\n')
    f.close()
labelframe1 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Settings')
labelframe1.place(x=10, y=10)
proxychecker = tk.Button(root, text='LoadProxy', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=proxybutton)
proxychecker.place(x=25, y=40)
proxylabel = tk.StringVar()
proxylabel.set('Loaded proxy: 0')
proxy_label = tk.Label(root, textvariable=proxylabel, bg='grey13', fg='white', font=('', 11, 'bold'))
proxy_label.place(x=25, y=66)
tokenchecker = tk.Button(root, text='LoadToken', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=tokenbutton)
tokenchecker.place(x=25, y=90)
tokenlabel = tk.StringVar()
tokenlabel.set('Loaded token: 0')
token_label = tk.Label(root, textvariable=tokenlabel, bg='grey13', fg='white', font=('', 11, 'bold'))
token_label.place(x=25, y=116)
proxyset = tk.BooleanVar()
proxyset.set('False')

def delay_value(value):
    global delay
    scaletext.set('Delay: ' + value)
    delay = value
scaletext = tk.StringVar()
scaletext.set('Delay: 0')
scale_label = tk.Label(root, textvariable=scaletext, bg='grey13', fg='white')
scale_bar = tk.Scale(root, orient='horizontal', length=150, from_=0.0, to=5, resolution=0.001, showvalue=0, sliderlength=20, bg='grey13', fg='white', relief='raised', bd='1', command=delay_value)
scale_bar.set(0.001)
scale_label.place(x=25, y=135)
scale_bar.place(x=25, y=155)
ch1 = tk.Checkbutton(root, text='Use Proxy', variable=proxyset, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
ch1.place(x=26, y=185)

def isascnum(s):
    if s.isdecimal() and s.isascii():
        return True
    return False

def apply():
    global alive_token
    if delayentry.get() != '':
        print('set delay: ' + str(delayentry.get()))
        delay_value(delayentry.get())
    if tokenentry.get() != '':
        if int(len(backup_token)) < int(tokenentry.get()):
            print('設定されたtokenの数はロードされた数より多いです')
            return
        print('set token range: ' + str(tokenentry.get()))
        tokenscale.set('Tokenrange: ' + str(tokenentry.get()))
        alive_token = []
        i = 0
        for token in backup_token:
            print(token)
            alive_token.append(token)
            i = i + 1
            if i >= int(tokenentry.get()):
                break
        print(alive_token)
        print('set tokens')
tokenscale = tk.StringVar()
tokenscale.set('Tokenrange: 0')
token_label2 = tk.Label(root, textvariable=tokenscale, bg='grey13', fg='white', font=('', 11, 'bold'))
token_label2.place(x=23, y=206)
delaylabel2 = tk.Label(text='Set Delay', bg='grey13', fg='white', font=('', 8, 'bold'))
delaylabel2.place(x=26, y=225)
delayentry = tk.Entry(width=25)
delayentry.place(x=26, y=245)
apply1 = tk.Button(root, text='Apply', bg='SlateBlue2', relief='raised', width=6, height=1, justify=tk.CENTER, command=apply)
apply1.place(x=150, y=215)
tokenlabel2 = tk.Label(text='Set Range', bg='grey13', fg='white', font=('', 8, 'bold'))
tokenlabel2.place(x=26, y=265)
tokenentry = tk.Entry(width=25)
tokenentry.place(x=26, y=285)
labelframe2 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Onliner/Status')
labelframe2.place(x=230, y=10)
onliner1 = tk.Button(root, text='Onliner', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER)
onliner1.place(x=245, y=40)
status1 = tk.Button(root, text='ChangeStatus', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER)
status1.place(x=245, y=70)
statuslore1 = tk.Button(root, text='ChangeStatusLore', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER)
statuslore1.place(x=245, y=100)
statuslore2 = tk.Button(root, text='StatusLoreList', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER)
statuslore2.place(x=245, y=130)

def button6():
    threading.Thread(target=joiner).start()

def joiner():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    r7 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        if tokens == []:
            print('Token file is not load?')
            return
        print('Not token checked, token file is loaded')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if invitetext.get() == '':
        messagebox.showerror('Error', 'Type invitelink')
        return
    invite = invitetext.get()
    r5 = urllib.parse.urlparse(invite).path.split('/')[-1]
    print(r5)
    if memberbypass.get():
        if serveridtext.get() == '':
            messagebox.showerror('Error', 'Type serverid')
            return
        r6 = serveridtext.get()
        r7 = True
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.joiner.start(r1, r2, r3, r4, r5, r6, r7, loop)
    print('Joined!')

def button7():
    threading.Thread(target=leaver).start()

def leaver():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        if tokens == []:
            print('Token file is not load?')
            return
        print('Not token checked, token file is loaded')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if serveridtext.get() == '':
        messagebox.showerror('Error', 'Type serverid')
        return
    r5 = serveridtext.get()
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.leaver.start(r1, r2, r3, r4, r5, loop)
    print('Leaved!')
labelframe3 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Join/Leave')
labelframe3.place(x=450, y=10)
joiner1 = tk.Button(root, text='Joiner', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button6)
joiner1.place(x=466, y=40)
leaver1 = tk.Button(root, text='Leaver', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button7)
leaver1.place(x=466, y=70)
invitelabel = tk.Label(text='InviteLink', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
invitelabel.place(x=465, y=97)
invitetext = tk.Entry(width=25)
invitetext.place(x=466, y=120)
serveridlabel = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serveridlabel.place(x=465, y=140)
serveridtext = tk.Entry(width=25)
serveridtext.place(x=466, y=163)
memberbypass = tk.BooleanVar()
memberbypass.set('False')
memberbypass1 = tk.Checkbutton(root, text='VerifyBypass', variable=memberbypass, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
memberbypass1.place(x=465, y=210)
labelframe4 = tk.LabelFrame(root, width=200, height=400, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Spammer')
labelframe4.place(x=670, y=10)

def button8():
    threading.Thread(target=openspammer).start()

def openspammer():
    works = 1
    root2 = tk.Tk()
    root2.title('Spammer')
    root2.geometry('200x150')
    root2.configure(bg='grey13')

    def buttons1():
        threading.Thread(target=startspam).start()

    def startspam():
        r1 = None
        r2 = []
        r3 = []
        r4 = None
        r5 = None
        r6 = None
        r7 = None
        r8 = None
        r9 = None
        r10 = None
        if delay == None:
            messagebox.showerror('Error', 'Delay set')
            return
        r1 = delay
        if alive_token == []:
            messagebox.showerror('Error', 'Please load the token')
            return
        r2 = alive_token
        if proxyset.get():
            if alive_proxies == []:
                messagebox.showerror('Error', 'Please load the proxies')
                return
            r3 = alive_proxies
            r4 = proxytype
        else:
            r4 = False
        if allping.get():
            if serveridtext2.get() == '':
                messagebox.showerror('Error', 'Type serverid')
                return
            r5 = True
            r6 = serveridtext2.get()
        else:
            r5 = False
        if allspam.get():
            if serveridtext2.get() == '':
                messagebox.showerror('Error', 'Type serverid')
                return
            r7 = True
            r6 = serveridtext2.get()
        else:
            if channeltext2.get() == '':
                messagebox.showerror('Error', 'Type channelid')
                return
            r7 = False
            r8 = channeltext2.get()
        if spamcontent.get('1.0', 'end') == '':
            messagebox.showerror('Error', 'Type spammessage')
            return
        r9 = spamcontent.get('1.0', 'end')
        if randomstring.get():
            r10 = True
        else:
            r10 = False
        if mention == None:
            messagebox.showerror('Error', 'Mention set')
            return
        r11 = mention
        if timelock.get():
            r12 = True
        else:
            r12 = False
        loop = asyncio.new_event_loop()
        old.gui.raidtool.spamtool.spammer.spammer.start(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, loop)

    def buttons2():
        threading.Thread(target=endspam).start()

    def endspam():
        old.gui.raidtool.spamtool.spammer.spammer.req_stop()

    def buttons3():
        root2.destroy()
    startspam1 = tk.Button(root2, text='Stable Spam', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons1)
    startspam1.place(x=10, y=10)
    endspam1 = tk.Button(root2, text='EndSpam', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons2)
    endspam1.place(x=10, y=40)
    endspam1 = tk.Button(root2, text='Close', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons3)
    endspam1.place(x=10, y=70)
    root2.mainloop()

def allping2():
    print('allping')

def allspam2():
    print('allspam')

def randomstring2():
    print('randomstring')
joiner1 = tk.Button(root, text='Spammer', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button8)
joiner1.place(x=686, y=40)
serveridlabel2 = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serveridlabel2.place(x=686, y=65)
serveridtext2 = tk.Entry(width=25)
serveridtext2.place(x=686, y=85)
channellabel2 = tk.Label(text='ChannelID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
channellabel2.place(x=686, y=105)
channeltext2 = tk.Entry(width=25)
channeltext2.place(x=686, y=125)
allping = tk.BooleanVar()
allping.set('False')
allping1 = tk.Checkbutton(root, text='All Ping', variable=allping, command=allping2, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
allping1.place(x=686, y=150)
allspam = tk.BooleanVar()
allspam.set('False')
allspam1 = tk.Checkbutton(root, text='Spam to All Channel', variable=allspam, command=allspam2, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
allspam1.place(x=686, y=175)
randomstring = tk.BooleanVar()
randomstring.set('False')
randomstring1 = tk.Checkbutton(root, text='Random String', variable=randomstring, command=randomstring2, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
randomstring1.place(x=686, y=200)
timelock = tk.BooleanVar()
timelock.set('True')
timelock1 = tk.Checkbutton(root, text='RateLimitFixer', variable=timelock, bg='SlateBlue2', fg='grey13', font=('Questrial', 9), relief='raised', width=19)
timelock1.place(x=686, y=225)

def mention_value(value):
    global mention
    scaletext2.set('Mention: ' + value)
    mention = value
scaletext2 = tk.StringVar()
scaletext2.set('Mention: 20')
mention = 20
scale_label2 = tk.Label(root, textvariable=scaletext2, bg='grey13', fg='white')
scale_bar2 = tk.Scale(root, orient='horizontal', length=150, from_=1, to=50, resolution=1, showvalue=0, sliderlength=20, bg='grey13', fg='white', relief='raised', bd='1', command=mention_value)
scale_bar2.set(0)
scale_label2.place(x=686, y=245)
scale_bar2.place(x=686, y=265)
spamcontentlabel = tk.Label(text='SpamMessage', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
spamcontentlabel.place(x=686, y=290)
spamcontent = tk.Text(root, width=22, height=6)
spamcontent.place(x=686, y=310)
spamcontent.insert('1.0', '')
labelframe5 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Nick/Avator')
labelframe5.place(x=10, y=320)

def button9():
    threading.Thread(target=nick).start()

def nick():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if serveridtext3.get() == '':
        messagebox.showerror('Error', 'Type serverid')
        return
    r5 = serveridtext3.get()
    if nicktext1.get() == '':
        messagebox.showerror('Error', 'Type nickname')
        return
    r6 = nicktext1.get()
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.nick.start(r1, r2, r3, r4, r5, r6, loop)

def button10():
    threading.Thread(target=avator).start()

def avator():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if avatortext.get() == '':
        messagebox.showerror('Error', 'Type avator url')
        return
    r5 = avatortext.get()
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.avator.start(r1, r2, r3, r4, r5, loop)
nick1 = tk.Button(root, text='ChangeNick', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button9)
nick1.place(x=25, y=348)
avator1 = tk.Button(root, text='ChangeAvator', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button10)
avator1.place(x=25, y=378)
avatorlabel = tk.Label(text='Avator URL', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
avatorlabel.place(x=25, y=410)
avatortext = tk.Entry(width=25)
avatortext.place(x=25, y=430)
serveridlabel3 = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serveridlabel3.place(x=25, y=450)
serveridtext3 = tk.Entry(width=25)
serveridtext3.place(x=25, y=472)
nicklabel1 = tk.Label(text='Nickname', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
nicklabel1.place(x=25, y=495)
nicktext1 = tk.Entry(width=25)
nicktext1.place(x=25, y=515)
labelframe6 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Friend/DM')
labelframe6.place(x=230, y=320)

def button11():
    threading.Thread(target=friend).start()

def friend():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if usertext.get() == '':
        messagebox.showerror('Error', 'Type username')
        return
    r5 = usertext.get()
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.friend.start(r1, r2, r3, r4, r5, loop)

def button12():
    threading.Thread(target=dm).start()

def dm():
    root3 = tk.Tk()
    root3.title('DMSpammer')
    root3.geometry('200x150')
    root3.configure(bg='grey13')

    def buttons1():
        threading.Thread(target=startspam).start()

    def startspam():
        r1 = None
        r2 = []
        r3 = []
        r4 = None
        r5 = None
        r6 = None
        if delay == None:
            messagebox.showerror('Error', 'Delay set')
            return
        r1 = delay
        if alive_token == []:
            messagebox.showerror('Error', 'Please load the token')
            return
        r2 = alive_token
        if proxyset.get():
            if alive_proxies == []:
                messagebox.showerror('Error', 'Please load the proxies')
                return
            r3 = alive_proxies
            r4 = proxytype
        else:
            r4 = False
        if useridtext.get() == '':
            messagebox.showerror('Error', 'Type userid')
            return
        r5 = useridtext.get()
        if spamcontent2.get('1.0', 'end') == '':
            messagebox.showerror('Error', 'Type spamcontent')
            return
        r6 = spamcontent2.get('1.0', 'end')
        loop = None
        loop = asyncio.new_event_loop()
        old.gui.raidtool.spamtool.dm.start(r1, r2, r3, r4, r5, r6, loop)

    def buttons2():
        threading.Thread(target=endspam).start()

    def endspam():
        old.gui.raidtool.spamtool.dm.req_stop()

    def buttons3():
        root3.destroy()
    startspam1 = tk.Button(root3, text='StartSpam', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons1)
    startspam1.place(x=10, y=10)
    endspam1 = tk.Button(root3, text='EndSpam', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons2)
    endspam1.place(x=10, y=40)
    endspam1 = tk.Button(root3, text='Close', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=buttons3)
    endspam1.place(x=10, y=70)
    root3.mainloop()
friend1 = tk.Button(root, text='FriendSend', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button11)
friend1.place(x=246, y=348)
nick1 = tk.Button(root, text='DMSpammer', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button12)
nick1.place(x=246, y=381)
userlabel = tk.Label(text='User (user#0000)', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
userlabel.place(x=246, y=410)
usertext = tk.Entry(width=25)
usertext.place(x=246, y=430)
useridlabel = tk.Label(text='UserID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
useridlabel.place(x=246, y=450)
useridtext = tk.Entry(width=25)
useridtext.place(x=246, y=470)
spamcontentlabel1 = tk.Label(text='SpamMessage', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
spamcontentlabel1.place(x=246, y=490)
spamcontent2 = tk.Text(root, width=22, height=5)
spamcontent2.place(x=246, y=510)
labelframe6 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='VoiceSpammer')
labelframe6.place(x=450, y=320)

def startvoicespam():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    r7 = None
    r8 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if servertext.get() == '':
        messagebox.showerror('Error', 'Type serverid')
        return
    r3 = servertext.get()
    if channeltext3.get() == '':
        messagebox.showerror('Error', 'Type channelid')
        return
    r4 = channeltext3.get()
    try:
        ffmpeg = os.path.join(os.getcwd(), 'ffmpeg.exe')
        r5 = ffmpeg
    except:
        print('Error load ffmpeg')
        r5 = ffmpeg_click()
    if voicempfile == '':
        messagebox.showerror('Error', 'Select voicemp file')
        return
    r6 = voicempfile
    loop = None
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.vc.start(r1, r2, r3, r4, r5, r6, loop)

def ffmpeg_click():
    print('Auto loaded')
    fTyp = [('', '*')]
    iFile = os.path.abspath(os.path.dirname(__file__))
    ffmpegfile = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile)
    print('[+] Select FFMPEG: ' + str(ffmpegfile))
    return ffmpegfile

def voicefile_click():
    global voicempfile
    fTyp = [('', '*')]
    iFile = os.path.abspath(os.path.dirname(__file__))
    voicempfile = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile)
    print('[+] Select voicefile : ' + str(voicempfile))
    messagebox.showinfo('Success', 'Load File: ' + str(voicempfile))
voice1 = tk.Button(root, text='VoiceSpammer', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=startvoicespam)
voice1.place(x=465, y=350)
channellabel3 = tk.Label(text='Voice Channel ID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
channellabel3.place(x=465, y=380)
channeltext3 = tk.Entry(width=25)
channeltext3.place(x=465, y=400)
serverlabel = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serverlabel.place(x=465, y=420)
servertext = tk.Entry(width=25)
servertext.place(x=465, y=440)
ffmpeg = tk.Button(root, text='None', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER)
ffmpeg.place(x=465, y=470)
voicemp = tk.Button(root, text='VoiceFile mp3', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=voicefile_click)
voicemp.place(x=465, y=500)
labelframe6 = tk.LabelFrame(root, width=200, height=200, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Reaction')
labelframe6.place(x=670, y=420)

def button13():
    threading.Thread(target=reaction).start()

def reaction():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    r7 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if channeltext4.get() == '':
        messagebox.showerror('Error', 'Type channelid')
        return
    r5 = channeltext4.get()
    if messagetext.get() == '':
        messagebox.showerror('Error', 'Type messageid')
        return
    r6 = messagetext.get()
    if emojitext.get() == '':
        messagebox.showerror('Error', 'Type emoji')
        return
    r7 = emojitext.get()
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.reaction.start(r1, r2, r3, r4, r5, r6, r7, loop)
reaction1 = tk.Button(root, text='AddReaction', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button13)
reaction1.place(x=685, y=450)
channellabel4 = tk.Label(text='ChannelID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
channellabel4.place(x=685, y=480)
channeltext4 = tk.Entry(width=25)
channeltext4.place(x=685, y=500)
messagelabel = tk.Label(text='MessageID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
messagelabel.place(x=685, y=520)
messagetext = tk.Entry(width=25)
messagetext.place(x=685, y=540)
emojilabel = tk.Label(text='Emoji', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
emojilabel.place(x=685, y=560)
emojitext = tk.Entry(width=25)
emojitext.place(x=685, y=580)
labelframe9 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='ReportSpam')
labelframe9.place(x=890, y=10)

def button14():
    threading.Thread(target=report).start()

def report():
    print('report')
    for i in lb.curselection():
        content = lb.get(i)
        content2 = i
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    r7 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if servertext2.get() == '':
        messagebox.showerror('Error', 'Type serverid')
        return
    r5 = servertext2.get()
    if channeltext6.get() == '':
        messagebox.showerror('Error', 'Type channelid')
        return
    r6 = channeltext6.get()
    if messagetext3.get() == '':
        messagebox.showerror('Error', 'Type messageid')
        return
    r7 = messagetext3.get()
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.report.start(r1, r2, r3, r4, r5, r6, r7, content, content2, loop)
    print('Ended Report!')
report1 = tk.Button(root, text='ReportSpam', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=button14)
report1.place(x=905, y=40)
serverlabel5 = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serverlabel5.place(x=905, y=70)
servertext2 = tk.Entry(width=25)
servertext2.place(x=905, y=90)
channellabel6 = tk.Label(text='ChannelID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
channellabel6.place(x=905, y=110)
channeltext6 = tk.Entry(width=25)
channeltext6.place(x=905, y=130)
messagelabel3 = tk.Label(text='MessageID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
messagelabel3.place(x=905, y=150)
messagetext3 = tk.Entry(width=25)
messagetext3.place(x=905, y=170)
messagelabel4 = tk.Label(text='ReportType', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
messagelabel4.place(x=905, y=190)
currencies = ['Illegal Content', 'Harrassment', 'Spam or Phishing Links', 'Self harm', 'NSFW Content']
v = tk.StringVar(value=currencies)
lb = tk.Listbox(root, listvariable=v, selectmode='SINGLE', height=5)
lb.place(x=905, y=215)
labelframe10 = tk.LabelFrame(root, width=200, height=300, fg='white', font=('Questrial', 16, 'bold'), bg='grey13', bd=4, text='Btn Pusher')
labelframe10.place(x=890, y=320)

def ticket():
    threading.Thread(target=ticket2).start()

def ticket2():
    r1 = None
    r2 = []
    r3 = []
    r4 = None
    r5 = None
    r6 = None
    r7 = None
    if delay == None:
        messagebox.showerror('Error', 'Delay set')
        return
    r1 = delay
    if alive_token == []:
        messagebox.showerror('Error', 'Please load the token')
        return
    r2 = alive_token
    if proxyset.get():
        if alive_proxies == []:
            messagebox.showerror('Error', 'Please load the proxies')
            return
        r3 = alive_proxies
        r4 = proxytype
    else:
        r4 = False
    if serveridtext4.get() == '':
        messagebox.showerror('Error', 'Type serverid')
        return
    r5 = serveridtext4.get()
    if channeltext5.get() == '':
        messagebox.showerror('Error', 'Type channelid')
        return
    r6 = channeltext5.get()
    if messagetext2.get() == '':
        messagebox.showerror('Error', 'Type messageid')
        return
    r7 = messagetext2.get()
    loop = asyncio.new_event_loop()
    old.gui.raidtool.spamtool.ticket.start(r1, r2, r3, r4, r5, r6, r7, loop)
ticket1 = tk.Button(root, text='Send', bg='SlateBlue2', relief='raised', width=22, height=1, justify=tk.CENTER, command=ticket)
ticket1.place(x=905, y=350)
serveridlabel4 = tk.Label(text='ServerID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
serveridlabel4.place(x=905, y=380)
serveridtext4 = tk.Entry(width=25)
serveridtext4.place(x=905, y=400)
channellabel5 = tk.Label(text='ChannelID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
channellabel5.place(x=905, y=420)
channeltext5 = tk.Entry(width=25)
channeltext5.place(x=905, y=440)
messagelabel2 = tk.Label(text='MessageID', bg='grey13', fg='white', font=('Questrial', 10, 'bold'))
messagelabel2.place(x=905, y=460)
messagetext2 = tk.Entry(width=25)
messagetext2.place(x=905, y=480)
root.title('SussyRaider status: ' + str(statussussy) + ' thread: ' + str(threading.active_count()))
root.mainloop()
