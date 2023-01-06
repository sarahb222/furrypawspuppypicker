# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import *
import pyperclip

#globals
pup_text = []
pup_sex = []
entry_arr = []
check_arr = []
sortedPups = []
statPref = "Any"
firstPref = "Low hh"
secondPref = "High HH"
thirdPref = "Size la"
fourthPref = "Stat Pref"
labelHolder = {}
saveHolder1 = {}
saveHolder2 = {}

class Puppy:
    def __init__(self, number, sex, size, sizeCount, statCount, HHCount, hhCount):
        self.number = number
        self.sex = sex
        self.size = size
        self.sizeCount = sizeCount
        self.statCount = statCount
        self.HHCount = HHCount
        self.hhCount = hhCount


def countSearch(pref, pup):
    if pref == "Low hh" or pref == "High hh":
        return pup.hhCount
    elif pref == "High HH" or pref == "Low HH":
        return pup.HHCount
    elif pref == "Size la":
        return pup.sizeCount
    else: return pup.statCount
    

#analyze the puppy data, access via button
def analyzeCallBack():
    global sortedPups
    sortedPups = []
    allPups = [] #Store all the dogs' data for future use

    for i in range(0,12):
        #split the stats for analysis
        temp_entry = entry_arr[i].get().split()
        #store the gender
        if(len(temp_entry) == 27):
            temp_sex = "M"
            if pup_sex[i].get() == 1:
                temp_sex = "F  "
            
            #Score based on litter size, preference for la then L over l
            temp_sizeCount = 0
            if(temp_entry[0] == "ll"):
                temp_sizeCount = 0
            elif(temp_entry[0] == "lL" or temp_entry[0] == "Ll"):
                temp_sizeCount = 1
            elif(temp_entry[0] == "LL"):
                temp_sizeCount = 2
            elif(temp_entry[0] == "lla" or temp_entry[0] == "lal"):
                temp_sizeCount = 3
            elif(temp_entry[0] == "Lla" or temp_entry[0] == "laL"):
                temp_sizeCount = 4
            elif(temp_entry[0] == "lala"):
                temp_sizeCount = 5
            else:
                temp_sizeCount =-10
                
            #count the preferred stat
            temp_statBoosts = [temp_entry[1][:len(temp_entry[1])//2], temp_entry[1][len(temp_entry[1])//2:],
                              temp_entry[2][:len(temp_entry[2])//2], temp_entry[2][len(temp_entry[2])//2:]]
            temp_statCount = 0
            for j in range(0, 4):
                if(temp_statBoosts[j] == statPref.get()):
                    temp_statCount = temp_statCount + 1
                    
            #count the HH and hh stats
            temp_HHCount = 0
            temp_hhCount = 0
            for j in range(3,27):
                if(temp_entry[j] == "HH"):
                    temp_HHCount = temp_HHCount + 1
                elif(temp_entry[j] == "hh"):
                    temp_hhCount = temp_hhCount + 1
            
            allPups.append(Puppy(i+1, temp_sex, temp_entry[0], temp_sizeCount, temp_statCount, temp_HHCount, temp_hhCount))


    #sort the list by best puppy to worst puppy
    indexOfBest = 0
    i = 0
    while(i < len(allPups)):
        i = 0
        indexOfBest = i
        if len(allPups) > 1:
            for j in range(i+1, len(allPups)):
                if(firstPref.get() != "Low HH" and firstPref.get() != "Low hh" and countSearch(firstPref.get(), allPups[j]) > countSearch(firstPref.get(), allPups[indexOfBest])):
                    indexOfBest = j
                elif((firstPref.get() == "Low HH" or firstPref.get() == "Low hh") and countSearch(firstPref.get(), allPups[j]) < countSearch(firstPref.get(), allPups[indexOfBest])):
                    indexOfBest = j
                elif(countSearch(firstPref.get(), allPups[j]) == countSearch(firstPref.get(), allPups[indexOfBest])):
                    if(secondPref.get() != "Low HH" and secondPref.get() != "Low hh" and countSearch(secondPref.get(), allPups[j]) > countSearch(secondPref.get(), allPups[indexOfBest])):
                        indexOfBest = j
                    elif((secondPref.get() == "Low HH" or secondPref.get() == "Low hh") and countSearch(secondPref.get(), allPups[j]) < countSearch(secondPref.get(), allPups[indexOfBest])):
                        indexOfBest = j
                    elif(countSearch(secondPref.get(), allPups[j]) == countSearch(secondPref.get(), allPups[indexOfBest])):
                        if(thirdPref.get() != "Low HH" and thirdPref.get() != "Low hh" and countSearch(thirdPref.get(), allPups[j]) > countSearch(thirdPref.get(), allPups[indexOfBest])):
                            indexOfBest = j
                        elif((thirdPref.get() == "Low HH" or thirdPref.get() == "Low hh") and countSearch(thirdPref.get(), allPups[j]) < countSearch(thirdPref.get(), allPups[indexOfBest])):
                            indexOfBest = j
                        elif(countSearch(thirdPref.get(), allPups[j]) == countSearch(thirdPref.get(), allPups[indexOfBest])):
                            if(fourthPref.get() != "Low HH" and fourthPref.get() != "Low hh" and countSearch(fourthPref.get(), allPups[j]) > countSearch(fourthPref.get(), allPups[indexOfBest])):
                                indexOfBest = j
                            elif((fourthPref.get() == "Low HH" or fourthPref.get() == "Low hh") and countSearch(fourthPref.get(), allPups[j]) < countSearch(fourthPref.get(), allPups[indexOfBest])):
                                indexOfBest = j

        temp = allPups.pop(indexOfBest)
        sortedPups.append(temp)
        i = 0
        
        
    #print list of sorted pups
    temp_text = []
    
    global labelHolder
    
    for i in range(0, 12):
        labelHolder[(i,0)].configure(text="")
        labelHolder[(i,1)].configure(text="")
        labelHolder[(i,2)].configure(text="")
        labelHolder[(i,3)].configure(text="")
        labelHolder[(i,4)].configure(text="")
        labelHolder[(i,5)].configure(text="")
    
    for i in range(0, len(sortedPups)):
        
        labelHolder[(i,0)].configure(text=sortedPups[i].sex)
        labelHolder[(i,1)].configure(text=" Puppy " + str(sortedPups[i].number))
        labelHolder[(i,2)].configure(text=sortedPups[i].size)
        labelHolder[(i,3)].configure(text=statPref.get() + ": " + str(sortedPups[i].statCount))
        labelHolder[(i,4)].configure(text="HH: " + str(sortedPups[i].HHCount))
        labelHolder[(i,5)].configure(text="hh: " + str(sortedPups[i].hhCount))
        
        
    
def copyCallBack(i):
    global sortedPups
    pyperclip.copy(sortedPups[i].size + " " + statPref.get() + ": " + str(sortedPups[i].statCount) + 
                   " HH: " + str(sortedPups[i].HHCount) + " hh: " + str(sortedPups[i].hhCount))      
    
    
def resetCallBack():
    for i in range(0,12):
        entry_arr[i].delete(0, 'end')
        pup_sex[i].set(0)
        
        
def saveCallBack(i):
    global saveHolder1
    global saveHolder2
    global entry_arr
    global pup_sex
    
    if(i == 1):
        for r in range(0,12):
            saveHolder1[(0,r)]=entry_arr[r].get()
        for r in range(0,12):
            saveHolder1[(1,r)]=pup_sex[r].get()
    else:
        for r in range(0,12):
            saveHolder2[(0,r)]=entry_arr[r].get()
        for r in range(0,12):
            saveHolder2[(1,r)]=pup_sex[r].get()
     
def loadCallBack(i):
    global saveHolder1
    global saveHolder2
    global entry_arr
    global pup_sex
    
    resetCallBack()
    
    if(i==1):
        for r in range(0,12):
            entry_arr[r].insert(0, saveHolder1[(0,r)])
        for r in range(0,12):
            pup_sex[r].set(saveHolder1[(1,r)])
    else:
        for r in range(0,12):
            entry_arr[r].insert(0, saveHolder2[(0,r)])
        for r in range(0,12):
            pup_sex[r].set(saveHolder2[(1,r)])
    
    
##### MAIN #####
root= tk.Tk()
root.title("Unofficial Furry Paws Puppy Picker")

#print the puppy labels on the left hand side
for i in range(0,12):
    pup_text.append(Label(root, text = "Puppy " + str(i+1)))
    pup_text[i].grid(row = i, column = 0, sticky = W, pady = 2)
    
    pup_sex.append(tk.IntVar())
    check_arr.append(tk.Checkbutton(root, text="F", variable=pup_sex[i]))
    check_arr[i].grid(row = i, column = 1, sticky = W, pady = 2)
   

       
    
#store all entries in array
for i in range(0,12):
    entry_arr.append(tk.Entry(root))
    entry_arr[i].grid(row = i, column = 2, sticky = W, pady = 2)


#button user presses to analyze puppy data
analyze = tk.Button(root, width = 7, text ="Analyze", command = analyzeCallBack)
analyze.grid(row = 0, column = 3, sticky = W, pady = 2)

#set stat preference
statPref = StringVar()
statPref.set("Any")

statPrefDrop = OptionMenu(root, statPref,"Any", "agi", "cha", "int", "spd", "stm", "str")
statPrefDrop.config(width = 3)
statPrefDrop.grid(row = 1, column = 3, sticky = W, pady = 2)

#set first preference
firstPref = StringVar()
firstPref.set("Size la")

firstPrefDrop = OptionMenu(root, firstPref,"Low hh", "High HH", "Size la", "Stat Pref", "High hh", "Low HH")
firstPrefDrop.config(width = 7)
firstPrefDrop.grid(row = 2, column = 3, sticky = W, pady = 2)

#set second preference
secondPref = StringVar()
secondPref.set("Stat Pref")

secondPrefDrop = OptionMenu(root, secondPref,"Low hh", "High HH", "Size la", "Stat Pref", "High hh", "Low HH")
secondPrefDrop.config(width = 7)
secondPrefDrop.grid(row = 3, column = 3, sticky = W, pady = 2)

#set third preference
thirdPref = StringVar()
thirdPref.set("Low hh")

thirdPrefDrop = OptionMenu(root, thirdPref,"Low hh", "High HH", "Size la", "Stat Pref", "High hh", "Low HH")
thirdPrefDrop.config(width = 7)
thirdPrefDrop.grid(row = 4, column = 3, sticky = W, pady = 2)

#set fourth preference
fourthPref = StringVar()
fourthPref.set("High HH")

fourthPrefDrop = OptionMenu(root, fourthPref,"Low hh", "High HH", "Size la", "Stat Pref", "High hh", "Low HH")
fourthPrefDrop.config(width = 7)
fourthPrefDrop.grid(row = 5, column = 3, sticky = W, pady = 2)

#save buttons 1 and 2
save1 = tk.Button(root, width = 7, text ="Save 1")
save1.grid(row = 6, column = 3, sticky = W, pady = 2)
save1.configure(command=lambda widget=1: saveCallBack(widget))
save2 = tk.Button(root, width = 7, text ="Save 2")
save2.grid(row = 7, column = 3, sticky = W, pady = 2)
save2.configure(command=lambda widget=2: saveCallBack(widget))

#Load buttons 1 and 2
load1 = tk.Button(root, width = 7, text ="Load 1")
load1.grid(row = 8, column = 3, sticky = W, pady = 2)
load1.configure(command=lambda widget=1: loadCallBack(widget))
load2 = tk.Button(root, width = 7, text ="Load 2")
load2.grid(row = 9, column = 3, sticky = W, pady = 2)
load2.configure(command=lambda widget=2: loadCallBack(widget))


#button user presses to reset to blank
reset = tk.Button(root, width = 7, text ="Reset", command = resetCallBack)
reset.grid(row = 11, column = 3, sticky = W, pady = 2)


for r in range(0,12):
    for s in range(0, 6):
        label = tk.Label(root, text="")
        label.grid(row=r, column = s+4, sticky = W, pady = 2)
        labelHolder[(r,s)] = label

for r in range(0,12):
    tempButt = tk.Button(root, text ="Copy")
    tempButt.grid(row = r, column = 10, sticky = W, pady = 2)
    tempButt.configure(command=lambda widget=r: copyCallBack(widget))

root.mainloop()