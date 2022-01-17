import tkinter as tk
from tkinter import ttk
import json

#resets varaibles on GUI after sumbiting
def reset_data(variables):
    for variable in variables.values():
        variable.set('')

#loops through all children of frame and destroys, if not duplicates would be displayed
def forget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#updates shipements shown on app for user to see
def update_statements(data,frame):
    for key, val in data.items():
        ttk.Label(frame,text=f"{key} {val['From']} {val['To']} {val['Boxes']} {val['Charge']}").grid()
   

def saveFile(variables,root):
    forget(root) #clears statement frame
    # dictionary Format for updating Json File
    new_dict = {
        variables['Date'].get():{
            "DriverID": variables['DriverID'].get(),
            "From": variables['From'].get(),
            "To":variables["To"].get(),
            "Boxes":variables["Boxes"].get(),
            "Charge":variables["Charge"].get(),
        }
    }
    #checks to see if file exist if not creates a json file
    try:
        #reads in json data
        with open("data.json",'r') as data_file:
            data = json.load(data_file)
            #updates new data and saves in json
            data.update(new_dict)
        with open("data.json",'w') as data_file:
            json.dump(data,data_file,indent=4)
        update_statements(data,root)
    except:
        #creates file with first json dump
        with open("data.json",'w') as data_file:
           json.dump(new_dict,data_file,indent=4)
        update_statements(new_dict,root)
    
    reset_data(variables)
