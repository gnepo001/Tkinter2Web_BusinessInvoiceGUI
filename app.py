import tkinter as tk
from tkinter import ttk
import helperFunctions as helperFunc


formTitles = ['Date','Driver ID','From', "To", "Boxes","Charge"]
variables = dict()

#main window
root = tk.Tk()
root.title("Shipping Statement")
root.geometry("420x350+500+300")

# Main Frame 
drf = ttk.Frame(root)
drf.grid(padx=10,sticky=(tk.E+tk.W))

#Top Right Date Frame
dateFrame = ttk.LabelFrame(drf)
dateFrame.grid(row=0,column=0)

variables['Date'] = tk.StringVar()
ttk.Label(dateFrame,text=formTitles[0]).grid(row=0,column=0, sticky=(tk.E+tk.W))
ttk.Entry(dateFrame,textvariable=variables['Date']).grid(row=1,column=0)

variables['DriverID'] = tk.StringVar()
ttk.Label(dateFrame,text=formTitles[1]).grid(row=0,column=1)
ttk.Entry(dateFrame,textvariable=variables['DriverID']).grid(row=1,column=1)

# B2B Info Frame
shippingFrame = ttk.LabelFrame(drf,text="B2B Information")
shippingFrame.grid(row=1,column=0,pady=10)

ttk.Label(shippingFrame,text=formTitles[2]).grid(row=0,column=0)
ttk.Label(shippingFrame,text=formTitles[3]).grid(row=0,column=1)

variables['From'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['From']).grid(row=1,column=0)
variables['To'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['To']).grid(row=1,column=1)

#Shipment Frame
infoFrame = ttk.LabelFrame(drf,text="Shipment Info")
infoFrame.grid(row=2,column=0)

ttk.Label(infoFrame,text=formTitles[4]).grid(row=0,column=0)
ttk.Label(infoFrame,text=formTitles[5]).grid(row=0,column=1)

variables['Boxes'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Boxes']).grid(row=1,column=0)
variables['Charge'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Charge']).grid(row=1,column=1)

### Submit Form
btnFrame = ttk.Frame(root)
btnFrame.grid(row=3,column=0,pady=10)

#frame for shipment statement
statementDisplayFrame = ttk.LabelFrame(drf,text="Statement Information")
statementDisplayFrame.grid(row=4,column=0)

ttk.Button(btnFrame,text="Clear",command= lambda :helperFunc.reset_data(variables)).grid(row=0,column=0)
ttk.Button(btnFrame,text="Add",command=lambda : helperFunc.saveFile(variables,statementDisplayFrame)).grid(row=0,column=1)


root.mainloop()
