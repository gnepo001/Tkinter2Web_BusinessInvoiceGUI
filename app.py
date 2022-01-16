import tkinter as tk
from tkinter import ttk

variables = dict()

root = tk.Tk()
root.title("Shipping Statement")

drf = ttk.Frame(root)
drf.grid(padx=10,sticky=(tk.E+tk.W))

# Shipping Frame
shippingFrame = ttk.LabelFrame(drf,text="Shipping Information")
shippingFrame.grid(row=0,column=0)

ttk.Label(shippingFrame,text="Date").grid(row=0,column=0)
ttk.Label(shippingFrame,text="From").grid(row=0,column=1)
ttk.Label(shippingFrame,text="To").grid(row=0,column=2)

variables['Date'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['Date']).grid(row=1,column=0)
variables['From'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['From']).grid(row=1,column=1)
variables['To'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['To']).grid(row=1,column=2)

#Informatinon Frame
infoFrame = ttk.LabelFrame(drf,text="Info")
infoFrame.grid(row=1,column=0)

ttk.Label(infoFrame,text="Boxes").grid(row=0,column=0)
ttk.Label(infoFrame,text="Charge").grid(row=0,column=1)

variables['Boxes'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Boxes']).grid(row=1,column=0)
variables['Charge'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Charge']).grid(row=1,column=1)

###
ttk.Button(text="Clear").grid(row=2,column=0)
ttk.Button(text="Add").grid(row=2,column=1)

root.mainloop()
