import tkinter as tk
from tkinter import ttk

variables = dict()

root = tk.Tk()
root.title("Shipping Statement")
root.geometry("420x350+500+300")
#root.maxsize(500,350)

# Main Frame 
drf = ttk.Frame(root)
drf.grid(padx=10,sticky=(tk.E+tk.W))

#Top Right Date Frame
dateFrame = ttk.LabelFrame(drf)
dateFrame.grid(row=0,column=0)

variables['Date'] = tk.StringVar()
ttk.Label(dateFrame,text="Date:").grid(row=0,column=0, sticky=(tk.E+tk.W))
ttk.Entry(dateFrame,textvariable=variables['Date']).grid(row=1,column=0)

variables['DriverID'] = tk.StringVar()
ttk.Label(dateFrame,text="Driver ID").grid(row=0,column=1)
ttk.Entry(dateFrame,textvariable=variables['DriverID']).grid(row=1,column=1)

# B2B Info Frame
shippingFrame = ttk.LabelFrame(drf,text="B2B Information")
shippingFrame.grid(row=1,column=0,pady=10)

ttk.Label(shippingFrame,text="From").grid(row=0,column=0)
ttk.Label(shippingFrame,text="To").grid(row=0,column=1)

variables['From'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['From']).grid(row=1,column=0)
variables['To'] = tk.StringVar()
ttk.Entry(shippingFrame,textvariable=variables['To']).grid(row=1,column=1)

#Shipment Frame
infoFrame = ttk.LabelFrame(drf,text="Shipment Info")
infoFrame.grid(row=2,column=0)

ttk.Label(infoFrame,text="Boxes").grid(row=0,column=0)
ttk.Label(infoFrame,text="Charge").grid(row=0,column=1)

variables['Boxes'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Boxes']).grid(row=1,column=0)
variables['Charge'] = tk.StringVar()
ttk.Entry(infoFrame,textvariable=variables['Charge']).grid(row=1,column=1)

### Submit Form
btnFrame = ttk.Frame(root)
btnFrame.grid(row=3,column=0)

ttk.Button(btnFrame,text="Clear").grid(row=3,column=0)
ttk.Button(btnFrame,text="Add").grid(row=3,column=1)

root.mainloop()
