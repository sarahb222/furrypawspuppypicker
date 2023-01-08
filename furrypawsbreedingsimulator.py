# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:38:34 2023

@author: Sarah
"""
import tkinter as tk
from tkinter import *
import pyperclip

female_entry_arr = []
male_entry_arr = []
saveHolder1 = {}
saveHolder2 = {}
avgHolder = []
sortedDogs = []
total_HH = 0
total_hh = 0
total_dogs = 0
max_HH = 0
max_hh = 0
dogComparisonHolder = {}
firstPref = "Min hh"
secondPref = "Min HH"
thirdPref = "Max hh"
fourthPref = "Max HH"
otherGender = "Female"
selected = None


class Dog:
    def __init__(self, number, size, stats, health, HHCount, hhCount, cMinHH, cMaxHH, cMinhh, cMaxhh):
        self.number = number
        self.size = size
        self.stats = stats
        self.health = health
        self.HHCount = HHCount
        self.hhCount = hhCount
        self.cMinHH = cMinHH
        self.cMaxHH = cMaxHH
        self.cMinhh = cMinhh
        self.cMaxhh = cMaxhh


def copyCallBack(i):
    global sortedDogs
    global otherGender
    
    pyperclip.copy(otherGender + " " + str(sortedDogs[i].number) + " " + sortedDogs[i].size + " " + 
                   sortedDogs[i].stats[0] + " " + sortedDogs[i].stats[1] + 
                   " HH: " + str(sortedDogs[i].cMinHH) + "/" + str(sortedDogs[i].cMaxHH) + " hh: " + 
                    str(sortedDogs[i].cMinhh) + "/" + str(sortedDogs[i].cMaxhh))


def updateTopCounts():
    global total_HH
    global total_h
    global total_dogs
    global max_HH
    global max_hh
    global avgHolder
    
    
    avgHolder[0].configure(text=str(round(total_HH/total_dogs,2)))
    avgHolder[1].configure(text=str(round(total_hh/total_dogs,2)))
    avgHolder[2].configure(text=str(max_HH))
    avgHolder[3].configure(text=str(max_hh))


def countSearch(pref, dog):
    if pref == "Min hh":
        return dog.cMinhh
    elif pref == "Min HH":
        return dog.cMinHH
    elif pref == "Max hh":
        return dog.cMaxhh
    else: return dog.cMaxHH
    

def compareDogs(currDog, unsortedDogList, num, sex):
    global sortedDogs
    global dogComparisonHolder
    sortedDogs = []
    global otherGender
    
    for r in range(0,20):
        for s in range(0, 8):
            label = tk.Label(root, text="")
            label.grid(row=r+1, column = s+6, sticky = W, pady = 2)
            dogComparisonHolder[(r,s)].configure(text="")
            
    if sex == "F":
        gender = "Female"
        otherGender = "Male"
    else:
        gender = "Male"
        otherGender = "Female"
        
    dogComparisonHolder[(0,0)].configure(width = 9, text=gender + " " + str(num+1))
    dogComparisonHolder[(0,1)].configure(width = 5,text=currDog.size)
    dogComparisonHolder[(0,2)].configure(width = 7,text=currDog.stats[0])
    dogComparisonHolder[(0,3)].configure(width = 7,text=currDog.stats[1])
    dogComparisonHolder[(0,4)].configure(width = 7,text="Min HH")
    dogComparisonHolder[(0,5)].configure(width = 7,text="Max HH")
    dogComparisonHolder[(0,6)].configure(width = 7,text="Min hh")
    dogComparisonHolder[(0,7)].configure(width = 7,text="Max hh")
    
    #compare the unsorted dogs to the current dog
    for i in range(len(unsortedDogList)):
        for j in range(0, 24):
            if currDog.health[j] == unsortedDogList[i].health[j] and currDog.health[j] == "HH":
                unsortedDogList[i].cMaxHH = unsortedDogList[i].cMaxHH + 1
                unsortedDogList[i].cMinHH = unsortedDogList[i].cMinHH + 1
            elif currDog.health[j] == unsortedDogList[i].health[j] and currDog.health[j] == "hh":
                unsortedDogList[i].cMaxhh = unsortedDogList[i].cMaxhh + 1
                unsortedDogList[i].cMinhh = unsortedDogList[i].cMinhh + 1
            elif (currDog.health[j] == "HH" and unsortedDogList[i].health[j] != "hh") or (unsortedDogList[i].health[j] == "HH" and currDog.health[j] != "hh"):
                unsortedDogList[i].cMaxHH = unsortedDogList[i].cMaxHH + 1
            elif (currDog.health[j] == "hh" and unsortedDogList[i].health[j] != "HH") or (unsortedDogList[i].health[j] == "hh" and currDog.health[j] != "HH"):
                unsortedDogList[i].cMaxhh = unsortedDogList[i].cMaxhh + 1
            elif (currDog.health[j] == "Hh" or currDog.health[j] == "hH") and (unsortedDogList[i].health[j] == "Hh" or unsortedDogList[i].health[j] == "hH"):
                unsortedDogList[i].cMaxHH = unsortedDogList[i].cMaxHH + 1
                unsortedDogList[i].cMaxhh = unsortedDogList[i].cMaxhh + 1
                
      
    
    #sort the dogs
    i=0
    while(i < len(unsortedDogList)):
        indexOfBest = i
        for j in range(i+1, len(unsortedDogList)):
            if(firstPref.get() != "Min hh" and firstPref.get() != "Max hh" and countSearch(firstPref.get(), unsortedDogList[j]) > countSearch(firstPref.get(), unsortedDogList[indexOfBest])):
                 indexOfBest = j
            elif((firstPref.get() == "Min hh" or firstPref.get() == "Max hh") and countSearch(firstPref.get(), unsortedDogList[j]) < countSearch(firstPref.get(), unsortedDogList[indexOfBest])):
                 indexOfBest = j
            elif(countSearch(firstPref.get(), unsortedDogList[j]) == countSearch(firstPref.get(), unsortedDogList[indexOfBest])):
                if(secondPref.get() != "Min hh" and secondPref.get() != "Max hh" and countSearch(secondPref.get(), unsortedDogList[j]) > countSearch(secondPref.get(), unsortedDogList[indexOfBest])):
                    indexOfBest = j
                elif((secondPref.get() == "Min hh" or secondPref.get() == "Max hh") and countSearch(secondPref.get(), unsortedDogList[j]) < countSearch(secondPref.get(), unsortedDogList[indexOfBest])):
                     indexOfBest = j
                elif(countSearch(secondPref.get(), unsortedDogList[j]) == countSearch(secondPref.get(), unsortedDogList[indexOfBest])):
                    if(thirdPref.get() != "Min hh" and thirdPref.get() != "Max hh" and countSearch(thirdPref.get(), unsortedDogList[j]) > countSearch(thirdPref.get(), unsortedDogList[indexOfBest])):
                        indexOfBest = j
                    elif((thirdPref.get() == "Min hh" or thirdPref.get() == "Max hh") and countSearch(thirdPref.get(), unsortedDogList[j]) < countSearch(thirdPref.get(), unsortedDogList[indexOfBest])):
                         indexOfBest = j
                    elif(countSearch(thirdPref.get(), unsortedDogList[j]) == countSearch(thirdPref.get(), unsortedDogList[indexOfBest])):
                        if(fourthPref.get() != "Min hh" and fourthPref.get() != "Max hh" and countSearch(fourthPref.get(), unsortedDogList[j]) > countSearch(fourthPref.get(), unsortedDogList[indexOfBest])):
                            indexOfBest = j
                        elif((fourthPref.get() == "Min hh" or fourthPref.get() == "Max hh") and countSearch(fourthPref.get(), unsortedDogList[j]) < countSearch(fourthPref.get(), unsortedDogList[indexOfBest])):
                             indexOfBest = j
        temp = unsortedDogList.pop(indexOfBest)
        sortedDogs.append(temp)  
        i = 0
        
    s=0
    for s in range(0,len(sortedDogs)):
        dogComparisonHolder[(s+1,0)].configure(width = 9, text=otherGender + " " + str(sortedDogs[s].number))
        dogComparisonHolder[(s+1,1)].configure(width = 5,text=sortedDogs[s].size)
        dogComparisonHolder[(s+1,2)].configure(width = 7,text=sortedDogs[s].stats[0])
        dogComparisonHolder[(s+1,3)].configure(width = 7,text=sortedDogs[s].stats[1])
        dogComparisonHolder[(s+1,4)].configure(width = 7,text=sortedDogs[s].cMinHH)
        dogComparisonHolder[(s+1,5)].configure(width = 7,text=sortedDogs[s].cMaxHH)
        dogComparisonHolder[(s+1,6)].configure(width = 7,text=sortedDogs[s].cMinhh)
        dogComparisonHolder[(s+1,7)].configure(width = 7,text=sortedDogs[s].cMaxhh)

def createDogList(num, test):
    global total_HH
    global total_hh
    global total_dogs
    global max_HH
    global max_hh
    
    temp = []
    
    if(len(test) == 41):
            test = test[14:]
    
    if(len(test) == 27):
        temp_health = []
        temp_HH = 0
        temp_hh = 0
        
        for j in range(3,27):
            temp_health.append(test[j])
            if test[j] == "HH":
                temp_HH = temp_HH + 1
            elif test[j] == "hh":
                temp_hh = temp_hh +1
                
        temp_dog = Dog(num+1, test[0], [test[1], test[2]], temp_health, 
                      temp_HH, temp_hh, 0, 0, 0, 0)
        if temp_HH > max_HH:
            max_HH = temp_HH
        if temp_hh > max_hh:
            max_hh = temp_hh
        total_dogs = total_dogs + 1
        total_HH = total_HH + temp_HH
        total_hh = total_hh + temp_hh
        
        return temp_dog
    
    return temp
    

def selectCallBack(i, sex):
    global female_entry_arr
    global male_entry_arr
    global total_HH
    global total_hh
    global total_dogs
    global max_HH
    global max_hh
    
    total_HH = 0
    total_hh = 0
    total_dogs = 0
    max_HH = 0
    max_hh = 0
    
    if sex == "F":
        temp_entry = female_entry_arr[i].get().split()
    else:
        temp_entry = male_entry_arr[i].get().split()
        
    if(len(temp_entry) == 41):
            temp_entry = temp_entry[14:]
        
    if(len(temp_entry) == 27):
        temp_health = []
        temp_HH = 0
        temp_hh = 0
        for j in range(3,27):
            temp_health.append(temp_entry[j])
            if temp_entry[j] == "HH":
                temp_HH = temp_HH + 1
            elif temp_entry[j] == "hh":
                temp_hh = temp_hh +1
                
        currDog = Dog(i, temp_entry[0], [temp_entry[1], temp_entry[2]], temp_health, 
                      temp_HH, temp_hh, 0, 0, 0, 0)
        
        unsortedDogList = [] #list of all dogs to compare with curr dog
        for j in range(0,20):
            if sex == "F":  
                tempDog = createDogList(j, male_entry_arr[j].get().split())
                if tempDog != []:
                    unsortedDogList.append(tempDog)
                createDogList(j, female_entry_arr[j].get().split())
            else:
                tempDog = createDogList(j, female_entry_arr[j].get().split())
                if tempDog != []:
                    unsortedDogList.append(tempDog)
                createDogList(j, male_entry_arr[j].get().split())
                
        ##need to print up the max HH and average HH etc
        updateTopCounts()
        compareDogs(currDog, unsortedDogList, i, sex)
        
    


def resetCallBack():
    global female_entry_arr
    global male_entry_arr
    
    for i in range(0,20):
        female_entry_arr[i].delete(0, 'end')
        male_entry_arr[i].delete(0, 'end')

def saveCallBack(i):
    global saveHolder1
    global saveHolder2
    global female_entry_arr
    global male_entry_arr
    
    if(i == 1):
        for r in range(0,20):
            saveHolder1[(0,r)]=female_entry_arr[r].get()
        for r in range(20,40):
            saveHolder1[(0,r)]=male_entry_arr[r-20].get()
    else:
        for r in range(0,20):
            saveHolder2[(0,r)]=female_entry_arr[r].get()
        for r in range(20,40):
            saveHolder2[(0,r)]=male_entry_arr[r-20].get()
     
def loadCallBack(i):
    global saveHolder1
    global saveHolder2
    global female_entry_arr
    global male_entry_arr
    
    resetCallBack()
    
    if(i==1):
        for r in range(0,20):
            female_entry_arr[r].insert(0, saveHolder1[(0,r)])
        for r in range(20,40):
            male_entry_arr[r-20].insert(0, saveHolder1[(0,r)])
    else:
        for r in range(0,20):
            female_entry_arr[r].insert(0, saveHolder2[(0,r)])
        for r in range(20,40):
            male_entry_arr[r-20].insert(0, saveHolder2[(0,r)])
    

def popup(event):
    global selected
    try:
        menu.tk_popup(event.x_root,event.y_root) # Pop the menu up in the given coordinates
        selected = event.widget
    finally:
        menu.grab_release() # Release it once an option is selected

def paste():
    clipboard = root.clipboard_get() # Get the copied item from system clipboard
    selected.insert('end',clipboard) # Insert the item into the entry widget

def copy():
    inp = selected.get() # Get the text inside entry widget
    root.clipboard_clear() # Clear the tkinter clipboard
    root.clipboard_append(inp) # Append to system clipboard

##### MAIN #####
root= tk.Tk()
root.title("Unofficial Furry Paws Breeding Simulator")

#print the female and male labels on the left hand side and create the entry labels
for i in range(0,20):
    tempButt = tk.Button(root, width = 7, text ="Female " + str(i+1))
    tempButt.grid(row = i+2, column = 0, sticky = W, pady = 2)
    tempButt.configure(command=lambda num=i, sex="F": selectCallBack(num, sex))
    
    tempButt = tk.Button(root, width = 7, text ="Male " + str(i+1))
    tempButt.grid(row = i+2, column = 3, sticky = W, pady = 2)
    tempButt.configure(command=lambda num=i, sex="M": selectCallBack(num, sex))
    
    female_entry_arr.append(tk.Entry(root))
    female_entry_arr[i].grid(row = i+2, column = 1, columnspan=2, sticky = W, pady = 2)
    female_entry_arr[i].bind('<Button-3>',popup) # Bind a func to right click
    
    male_entry_arr.append(tk.Entry(root))
    male_entry_arr[i].grid(row = i+2, column = 4, columnspan=2, sticky = W, pady = 2)
    male_entry_arr[i].bind('<Button-3>',popup) # Bind a func to right click
    
    
#save buttons 1 and 2
save1 = tk.Button(root, width = 7, text ="Save 1")
save1.grid(row = 0, column = 4, sticky = W, pady = 2)
save1.configure(command=lambda widget=1: saveCallBack(widget))
save2 = tk.Button(root, width = 7, text ="Save 2")
save2.grid(row = 0, column = 5, sticky = W, pady = 2)
save2.configure(command=lambda widget=2: saveCallBack(widget))

#Load buttons 1 and 2
load1 = tk.Button(root, width = 7, text ="Load 1")
load1.grid(row = 1, column = 4, sticky = W, pady = 2)
load1.configure(command=lambda widget=1: loadCallBack(widget))
load2 = tk.Button(root, width = 7, text ="Load 2")
load2.grid(row = 1, column = 5, sticky = W, pady = 2)
load2.configure(command=lambda widget=2: loadCallBack(widget))

#button user presses to reset to blank
reset = tk.Button(root, width = 7, text ="Reset", command = resetCallBack)
reset.grid(row = 0, column = 13, sticky = W, pady = 2)
    
temp_text = Label(root, text = "Average HH: ")
temp_text.grid(row = 0, column = 0, sticky = W, pady = 2)
avgHolder.append(Label(root, text = ""))
avgHolder[0].grid(row = 0, column = 1, sticky = W, pady = 2)

temp_text = Label(root, text = "Average hh: ")
temp_text.grid(row = 1, column = 0, sticky = W, pady = 2)
avgHolder.append(Label(root, text = ""))
avgHolder[1].grid(row = 1, column = 1, sticky = W, pady = 2)

temp_text = Label(root, text = "               Max HH: ")
temp_text.grid(row = 0, column = 2, sticky = W, pady = 2)
avgHolder.append(Label(root, text = ""))
avgHolder[2].grid(row = 0, column = 3, sticky = W, pady = 2)

temp_text = Label(root, text = "               Max hh: ")
temp_text.grid(row = 1, column = 2, sticky = W, pady = 2)
avgHolder.append(Label(root, text = ""))
avgHolder[3].grid(row = 1, column = 3, sticky = W, pady = 2)

for r in range(0,21):
    for s in range(0, 8):
        label = tk.Label(root, text="")
        label.grid(row=r+1, column = s+6, sticky = W, pady = 2)
        dogComparisonHolder[(r,s)] = label

        
#set first preference
firstPref = StringVar()
firstPref.set("Min hh")

firstPrefDrop = OptionMenu(root, firstPref,"Min hh", "Min HH", "Max hh", "Max HH")
firstPrefDrop.config(width = 7)
firstPrefDrop.grid(row = 0, column = 6, sticky = W, pady = 2)

#set second preference
secondPref = StringVar()
secondPref.set("Min HH")

secondPrefDrop = OptionMenu(root, secondPref,"Min hh", "Min HH", "Max hh", "Max HH")
secondPrefDrop.config(width = 7)
secondPrefDrop.grid(row = 0, column = 7, sticky = W, pady = 2)

#set third preference
thirdPref = StringVar()
thirdPref.set("Max hh")

thirdPrefDrop = OptionMenu(root, thirdPref,"Min hh", "Min HH", "Max hh", "Max HH")
thirdPrefDrop.config(width = 7)
thirdPrefDrop.grid(row = 0, column = 8, sticky = W, pady = 2)

#set fourth preference
fourthPref = StringVar()
fourthPref.set("Max HH")

fourthPrefDrop = OptionMenu(root, fourthPref,"Min hh", "Min HH", "Max hh", "Max HH")
fourthPrefDrop.config(width = 7)
fourthPrefDrop.grid(row = 0, column = 9, sticky = W, pady = 2)

for r in range(0,20):
    tempButt = tk.Button(root, text ="Copy")
    tempButt.grid(row = r+2, column = 14, sticky = W, pady = 2)
    tempButt.configure(command=lambda widget=r: copyCallBack(widget))
    
menu = Menu(root,tearoff=0) # Create a menu
menu.add_command(label='Copy',command=copy) # Create labels and commands
menu.add_command(label='Paste',command=paste)

root.mainloop()