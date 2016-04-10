#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from commands import *

lst = [(u"kontrol", ifStatement),
       (u"alta geç", newLine),
       (u"küçüktür", lessThan),
       (u"büyük eşittir", bigEqual),
       (u"büyüktür", greaterThan),
       (u"küçük eşittir", lowEqual),
       (u"boşluk", getSpace),
       (u"yazdır", getPrint),
       (u"rastgele sayı", randomNum),
       (u"paragraf", getTab)]

listen = True

def callFSetI(indx, i):
    global lst
    lst[indx][1]()
    return (i+1)

def callback(recognizer, audio):
    global listen, lst
    try:
        if listen:
            # a = recognizer.recognize_google(audio, language="tr")
            a = recognizer.recognize_google(audio, language="tr")
            words = a.lower().split()
            lstt = [s for s, f in lst]
            i = 0
            while i < len(words):
                if words[i] not in lstt:
                    if (words[i] == lst[1][0].split()[0]):
                        if (len(words) > i + 1) and (words[i+1] == lst[1][0].split()[1]):
                            i = callFSetI(1, i)
                        else:
                            standard_write(words[i])
                    elif (words[i] == lst[3][0].split()[0]):
                        if (len(words) > i + 1) and (words[i+1] == lst[3][0].split()[1]):
                            i = callFSetI(3, i)
                        else:
                            standard_write(words[i])
                    elif (words[i] == lst[5][0].split()[0]):
                        if (len(words) > i + 1) and (words[i+1] == lst[5][0].split()[1]):
                            i = callFSetI(5, i)
                        else:
                            standard_write(words[i])
                    elif (words[i] == lst[8][0].split()[0]):
                        if (len(words) > i + 1) and (words[i+1] == lst[8][0].split()[1]):
                            i = callFSetI(8, i)
                        else:
                            standard_write(words[i])
                    else:
                        standard_write(words[i])
                else:
                    # print words[i]
                    if words[i] == lst[0][0]:
                        lst[0][1]()
                    elif words[i] == lst[2][0]:
                        lst[2][1]()
                    elif words[i] == lst[4][0]:
                        lst[4][1]()
                    elif words[i] == lst[6][0]:
                        lst[6][1]()
                    elif words[i] == lst[7][0]:
                        lst[7][1]()
                    elif words[i] == lst[9][0]:
                        lst[9][1]()
                i += 1
        else:
            listen = False
    except sr.UnknownValueError:
        print("waiting for a command...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.5
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)


# Tkinter starts here
textPad.quit()
textPad.bind('<F12>', stopKey)
textPad.bind('<F11>', startKey)

# Modifications on editor
root.wm_attributes("-alpha", 0.8)  # opacity
root.resizable(False, True)  # editor enine buyumez, boyuna buyur
root.wm_protocol("WM_DELETE_WINDOW", Tk)  # kapatmayi engeller

# Editor menus here
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_command)
help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About...", command=about_command)
textPad.pack()
root.mainloop()

import time
for _ in range(50):
    time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening() # calling this function requests that the background listener stop listening
while True:
    time.sleep(0.1)