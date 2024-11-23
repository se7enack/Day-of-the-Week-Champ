#!/usr/bin/env python3

from tkinter import *
from datetime import datetime
from random import randrange
from datetime import timedelta
import pygame

startYear = 1981
endYear = 2024
count = 10

dates = []

options = [
    'Sunday', 
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thursday', 
    'Friday', 
    'Saturday'
]

magicDates = [
  3,
  28,
  14,
  4,
  9,
  6,
  11,
  8,
  5,
  10,
  7,
  12
]

good = 'good.mp3'
bad = 'bad.mp3'


def playit(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


def doMaths(monthNum, monthDay):
    specialDay = magicDates[monthNum-1]
    if monthDay == specialDay:
        x = 0
    elif monthDay < specialDay:
        x = 6 - ((specialDay - monthDay) %7)
    else:
        x = 7 - (monthDay - specialDay)
    y = yearVal(curYear)
    x = (((monthDay - specialDay)+y) %7) - leap
    return options[x]
    

def century(y):
    startdays = [0, 5, 3, 2]
    centurycounter = 0
    for i in range(17, 99):
        if y == i:
            return startdays[centurycounter]
        centurycounter = centurycounter + 1
        

def randomDate(start, end):
    d1 = datetime.strptime(f'1/1/{startYear} 12:00 AM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime(f'12/31/{endYear} 11:59 PM', '%m/%d/%Y %I:%M %p')
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    x = d1 + timedelta(seconds=random_second)
    split = str(x).split(' ', 1)[0]
    date = datetime.strptime(split, '%Y-%m-%d').strftime('%-m/%-d/%Y')
    return date


def makeList():
    global dates
    dates.clear()
    for i in range(count):
        try:
            dates.append(randomDate(startYear, endYear))
        except:
            exit(0)


def gameover():
    myLabel.configure(text=f'\n\nG A M E\nO V E R\n\n{points} out of {count} correct!\n')

    
def destroy():
    root.destroy()
    start()


def date():
    global leap
    global curMonth
    global curDay
    global curYear
    curYear = str(dates[x]).split('/', 2)[2]
    curDay = str(dates[x]).split('/', 2)[1]
    curMonth = str(dates[x]).split('/', 2)[0]
    leap = 0
    if (int(curYear) % 4 == 0) and (int(curMonth) < 3):
        leap = 1

        
def update():
    global x
    global points
    dayNum = options.index(clicked.get())
    date()
    reality = doMaths(int(curMonth), int(curDay))
    picked = options[dayNum]
    print(f"reality:{reality} picked:{picked}")
    if reality == picked:
        points = points+1
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
    date()
    clicked = StringVar()
    clicked.set('Sunday')
    drop = OptionMenu(root, clicked, *options)
    drop.pack()
    Button(root, text=" Submit ", command=update).pack()
    Button(root, text=" Restart ", command=destroy).pack()
    root.mainloop()


def yearVal(x):
    year = f"{x}"
    cen = int(year[:len(year)//2])
    dec = int(x) % 100
    c = century(cen)
    dotw = int(dec / 4 + dec + c) % 7
    return dotw


start()
