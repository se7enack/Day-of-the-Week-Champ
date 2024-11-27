#!/usr/bin/env python3

from tkinter import *
from datetime import datetime
from random import randrange
from datetime import timedelta
import pygame
import time

startYear = 1974
endYear = 2024
count = 10

dates = []

options = [ 
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thursday', 
    'Friday',
    'Saturday',
    'Sunday'    
]

good = 'good.mp3'
bad = 'bad.mp3'
perfect = "perfect.mp3"


def playit(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


def randomDate(start, end):
    d1 = datetime.strptime(f'1/1/{startYear} 12:00 AM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime(f'12/31/{endYear} 11:59 PM', '%m/%d/%Y %I:%M %p')
    delta = d2 - d1
    intDelta = (delta.days * 24 * 60 * 60) + delta.seconds
    randomSecond = randrange(intDelta)
    x = d1 + timedelta(seconds=randomSecond)
    split = str(x).split(' ', 1)[0]
    date = datetime.strptime(split, '%Y-%m-%d').strftime('%-m/%-d/%Y')
    return date


def makeList():
    global dates
    dates.clear()
    for _ in range(count):
        dates.append(randomDate(startYear, endYear))


def gameover():
    time.sleep(1)
    if points == count:
        playit(perfect)
    myLabel.configure(text=f'\nG A M E\nO V E R\n\n{points} out of {count} correct!\n')

    
def destroy():
    root.destroy()
    start()


def getDay(dateString):
    dateObject = datetime.strptime(dateString, "%m/%d/%Y").date()
    dayNumber = dateObject.weekday()
    dayName = options[dayNumber]
    print(dayName)
    return dayName
    
        
def update():
    global x
    global points
    dayNum = options.index(clicked.get())
    reality = getDay(dates[x])
    picked = options[dayNum]
    print(f"reality:{reality} picked:{picked}")
    if reality == picked:
        points = points + 1
        playit(good)
    else:
        playit(bad)
    print(dates[x])
    if x + 1 >= count:
        gameover()
    else:
        x = x + 1
        myLabel.configure(text=f'{x+1} of {count}\n\nPick a Day-of-the-Week\n\nfor {dates[x]}\n')


def start():
    global x
    global myLabel
    global root
    global clicked
    global options
    global points
    points = 0
    x = 0
    makeList()
    root = Tk()
    root.title("Day-of-the-Week-Champ")
    root.geometry("250x200")
    myLabel = Label(root, text=f'{x+1} of {count}\n\nPick a Day-of-the-Week\n\nfor {dates[x]}\n')
    myLabel.pack()
    clicked = StringVar()
    clicked.set('Sunday')
    drop = OptionMenu(root, clicked, *options)
    drop.pack()
    Button(root, text=" Submit ", command=update).pack()
    Button(root, text=" Restart ", command=destroy).pack()
    root.mainloop()


start()
