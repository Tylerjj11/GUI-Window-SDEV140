# course: SDEV 140
# author: Joy, Tyler
# date: 2021-9-28
# program: m06_Assn2_Ex3_Joy-Tyler.py
# purpose: Create GUI window for final project

from tkinter import *

main = Tk()
main.title('Master Cabling by Tyler Joy')
#Functions

#labels
companyLbl = Label(main, text="Master Cabling", font='Helvetica 18 bold')
nameLbl = Label(main, text="Full Name: ", font='Helvetica 12')
addressLbl = Label(main, text="Address: ", font='Helvetica 12')
zipLbl = Label(main, text="Zip Code: ", font='Helvetica 12')
emailLbl = Label(main, text="Email: ", font='Helvetica 12')
cableNeedLbl = Label(main, text="Cabling Needed", font='Helvetica 15 bold')
tpLbl = Label(main, text="Twisted Pair: ", font='Helvetica 12')
foLbl = Label(main, text="Fiber Optics: ", font='Helvetica 12')
coaxLbl = Label(main, text="Coax: ", font='Helvetica 12')
infoLbl = Label(main, text="Select 'Order' for a quote!", font='Helvetica 12')

#Text boxes (Entrys)
nameTxt = Entry(main, width=25)
addressTxt = Entry(main, width=25)
zipTxt = Entry(main, width=6)
emailTxt = Entry(main, width=25)
tpTxt = Entry(main, width=4)
foTxt = Entry(main, width=4)
coaxTxt = Entry(main, width=4)

#Buttons
orderBtn = Button(main, text="Order", height=3, width=14)
clearBtn = Button(main, text="Clear", height=3, width=14)
viewPriceBtn = Button(main, text="View Cable Prices", height=3, width=14)

#Layout
    #Labels
companyLbl.grid(row=0, column=1, columnspan=2)
nameLbl.grid(row=1, column=0)
addressLbl.grid(row=2, column=0)
zipLbl.grid(row=3, column=0, padx=35)
emailLbl.grid(row=4, column=0)
cableNeedLbl.grid(row=5, column=0)
tpLbl.grid(row=6, column=0)
foLbl.grid(row=7, column=0)
coaxLbl.grid(row=8, column=0)
infoLbl.grid(row=1, column=3, rowspan=2)

    #Text boxes
nameTxt.grid(row=1, column=2, sticky=W)
addressTxt.grid(row=2, column=2, sticky=W)
zipTxt.grid(row=3, column=2, sticky=W)
emailTxt.grid(row=4, column=2, sticky=W)
tpTxt.grid(row=6, column=2, sticky=W)
foTxt.grid(row=7, column=2, sticky=W)
coaxTxt.grid(row=8, column=2, sticky=W)

    #buttons
orderBtn.grid(row=3, column=3, rowspan=2)
clearBtn.grid(row=5, column=3, rowspan=2)
viewPriceBtn.grid(row=7, column=3, rowspan=2)

main.mainloop()
