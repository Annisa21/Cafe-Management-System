from tkinter import*
import tkinter.messagebox
import random
import time;
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Billing System")
root.configure(background='black')

Tops = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
Tops.pack(side = TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 440, height = 650, bd = 8, relief = "raise")
f2.pack(side = RIGHT)

f1a = Frame(f1, width = 900, height = 330, bd = 8, relief = "raise")
f1a.pack(side = TOP)
f2a = Frame(f1, width = 900, height = 320, bd = 6, relief = "raise")
f2a.pack(side = BOTTOM)

ft2 = Frame(f2, width = 440, height = 450, bd = 12, relief = "raise")
ft2.pack(side = TOP)
fb2 = Frame(f2, width = 440, height = 250, bd = 16, relief = "raise")
fb2.pack(side = BOTTOM)

f1aa = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1aa.pack(side = LEFT)
f1ab = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1ab.pack(side = RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd = 14, relief = "raise")
f2aa.pack(side = LEFT)
f2ab = Frame(f2a, width = 450, height = 330, bd = 14, relief = "raise")
f2ab.pack(side = RIGHT)

Tops.configure(background = 'black')
f1.configure(background = 'black')
f2.configure(background = 'black')

lblInfo = Label(Tops, font = ('arial', 70, 'bold'), text="  Cafe Management Systems   ", bd = 10)
lblInfo.grid(row = 0, column = 0)
#=================================================Method=============================================
def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Ice_Latta.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Ice_Cappuccino.get())

    Item9=float(E_CoffeeCake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())

    PriceofDrinks = (Item1* 12000) + (Item2 * 15000) + (Item3 * 15500) \
                    + (Item4 * 19000) + (Item5 * 15000) + (Item6 * 18000) + (Item7 * 18000) + (Item8 * 17000)

    PriceofCakes = (Item9 * 12000) + (Item10 * 15000) + (Item11 * 18000) \
                   + (Item12 * 18000) + (Item13 * 20000) + (Item14 * 22000) + (Item15 * 22000) + (Item16 * 20000)

    DrinksPrice = "Rp.", str('%.2f'%(PriceofDrinks))
    CakesPrice = "Rp.", str('%.2f'%(PriceofCakes))
    CostofDrinks.set(DrinksPrice)
    CostofCakes.set(CakesPrice)
    SC = "Rp.", str('%.2f'%(2))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rp.", str('%.2f'%(PriceofDrinks + PriceofCakes))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rp.", str('%.2f'%(PriceofDrinks + PriceofCakes + 2))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 2) * 0.15)
    TC = "Rp.", str('%.2f'%(PriceofDrinks + PriceofCakes + 2 + TT))
    TotalCost.set(TC)


def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() +'\t\t'+ DataofOrder.get() +"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost Of Items\n\n")
    txtReceipt.insert(END, 'Latta: \t\t\t\t\t' + E_Latta.get() + "\n")
    txtReceipt.insert(END, 'Espresso: \t\t\t\t\t' + E_Espresso.get() + "\n")
    txtReceipt.insert(END, 'Ice Latta: \t\t\t\t\t' + E_Ice_Latta.get() + "\n")
    txtReceipt.insert(END, 'Vale Coffee: \t\t\t\t\t' + E_Vale_Coffee.get() + "\n")
    txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'African Coffee: \t\t\t\t\t' + E_African_Coffee.get() + "\n")
    txtReceipt.insert(END, 'American Coffee: \t\t\t\t\t' + E_American_Coffee.get() + "\n")
    txtReceipt.insert(END, 'Ice Cappuccino: \t\t\t\t\t' + E_Ice_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake: \t\t\t\t\t' + E_CoffeeCake.get() + "\n")
    txtReceipt.insert(END, 'Red Velvet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get() + "\n")
    txtReceipt.insert(END, 'Black Forest Cake: \t\t\t\t\t' + E_Black_Forest_Cake.get() + "\n")
    txtReceipt.insert(END, 'Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake: \t\t\t\t\t' + E_Lagos_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Kilburn Chocolate Cake: \t\t\t\t\t' + E_Kilburn_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Carlton Hill Chocolate Cake: \t\t\t\t\t' + E_Carlton_Hill_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Queen Park Chocolate Cake: \t\t\t\t\t' + E_Queen_Park_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Cost of Drinks:\t\t' + CostofDrinks.get() + '\tTax Paid:\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes:\t\t' + CostofCakes.get() + '\tSub Total:\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t' + ServiceCharge.get() + '\tTotal Cost:\t\t' + TotalCost.get() + "\n")


def qExit():
    qExit = tkinter.messagebox.askyesno("Quit System", "Do you want quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latta.set("0")
    E_Espresso.set("0")
    E_Ice_Latta.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Ice_Cappuccino.set("0")


    E_CoffeeCake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")
#========================================================================

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
#==========================================Variable====================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DataofOrder =StringVar()
Receipt_Ref = StringVar()
PaidTax =StringVar()
SubTotal =StringVar()
TotalCost =StringVar()
CostofCakes =StringVar()
CostofDrinks =StringVar()
ServiceCharge =StringVar()

E_Latta = StringVar()
E_Espresso= StringVar()
E_Ice_Latta= StringVar()
E_Vale_Coffee= StringVar()
E_Cappuccino= StringVar()
E_African_Coffee= StringVar()
E_American_Coffee= StringVar()
E_Ice_Cappuccino= StringVar()


E_CoffeeCake= StringVar()
E_Red_Velvet_Cake= StringVar()
E_Black_Forest_Cake= StringVar()
E_Boston_Cream_Cake= StringVar()
E_Lagos_Chocolate_Cake= StringVar()
E_Kilburn_Chocolate_Cake= StringVar()
E_Carlton_Hill_Chocolate_Cake= StringVar()
E_Queen_Park_Chocolate_Cake= StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Ice_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Ice_Cappuccino.set("0")


E_CoffeeCake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")



DataofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Drinks=====================================
Latta = Checkbutton(f1aa, text = "Latta\t", variable = var1, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 0, sticky =W)
Espresso = Checkbutton(f1aa, text = "Espresso\t", variable = var2, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Ice_Latta = Checkbutton(f1aa, text = "Ice Latta\t", variable = var3, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Vale_Coffee = Checkbutton(f1aa, text = "Vale Coffee\t", variable = var4, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Cappuccino = Checkbutton(f1aa, text = "Cappuccino\t", variable = var5, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
African_Coffee = Checkbutton(f1aa, text = "African Coffee\t", variable = var6, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
American_Coffee = Checkbutton(f1aa, text = "American Coffee\t", variable = var7, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Ice_Cappuccino = Checkbutton(f1aa, text = "Ice Cappuccino\t", variable = var8, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 7, sticky = W)

#===========================================Cakes======================================
CoffeeCake = Checkbutton(f1ab, text = "Coffee Cake", variable = var9,
                    font = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Red_Velvet_Cake = Checkbutton(f1ab, text = "red Velvet Cake", variable = var10, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Black_Forest_Cake = Checkbutton(f1ab, text = "Black Forest Cake", variable = var11, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Boston_Cream_Cake = Checkbutton(f1ab, text = "Boston Cream Cake", variable = var12, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text = "Lagos Chocolate Cake", variable = var13, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text = "Kilburn Chocolate Cake", variable = var14, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
Carlton_Hill_Cake = Checkbutton(f1ab, text = "Carlton Hill Chocolate Cake", variable = var15, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Queen_Park_Cake = Checkbutton(f1ab, text = "Queen's Park Chocolate Cake", variable = var16, onvalue = 1, offvalue = 0,
                    font = ('arial', 18, 'bold')).grid(row = 7, sticky = W)


#===========================================Enter Widget for Drinks======================================
txtLatta = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Latta)
txtLatta.grid(row = 0, column = 1)
txtEspresso = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable=E_Espresso)
txtEspresso.grid(row = 1, column = 1)
txtIce_Latta = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Ice_Latta)
txtIce_Latta.grid(row = 2, column = 1)
txtVale_Coffee = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Vale_Coffee)
txtVale_Coffee.grid(row = 3, column = 1)
txtCappuccino = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Cappuccino)
txtCappuccino.grid(row = 4, column = 1)
txtAfrican_Coffee = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_African_Coffee)
txtAfrican_Coffee.grid(row = 5, column = 1)
txtAmerican_Coffee = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_American_Coffee)
txtAmerican_Coffee.grid(row = 6, column = 1)
txtIce_Cappuccino = Entry(f1aa, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Ice_Cappuccino)
txtIce_Cappuccino.grid(row = 7, column = 1)
#===========================================Enter Widget for Cakes======================================
txtCoffeeCake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_CoffeeCake)
txtCoffeeCake.grid(row = 0, column = 1)
txtRed_Velvet_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Red_Velvet_Cake)
txtRed_Velvet_Cake.grid(row = 1, column = 1)
txtBlack_Forest_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Black_Forest_Cake)
txtBlack_Forest_Cake.grid(row = 2, column = 1)
txtBoston_Cream_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Boston_Cream_Cake)
txtBoston_Cream_Cake.grid(row = 3, column = 1)
txtLagos_Chocolate_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Lagos_Chocolate_Cake)
txtLagos_Chocolate_Cake.grid(row = 4, column = 1)
txtKilburn_Chocolate_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Kilburn_Chocolate_Cake)
txtKilburn_Chocolate_Cake.grid(row = 5, column = 1)
txtCarlton_Hill_Chocolate_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Carlton_Hill_Chocolate_Cake)
txtCarlton_Hill_Chocolate_Cake.grid(row = 6, column = 1)
txtQueen_Park_Chocolate_Cake = Entry(f1ab, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left',textvariable=E_Queen_Park_Chocolate_Cake)
txtQueen_Park_Chocolate_Cake.grid(row = 7, column = 1)
#================================================Information========================================================
lblReceipt = Label(ft2, font = ('arial', 12, 'bold'), text = "Receipt", bd = 2, anchor = 'w')
lblReceipt.grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, width = 59, height = 22, bg = "white", bd = 8, font = ('arial', 11, 'bold'))
txtReceipt.grid(row = 1, column = 0)
#====================================================Cost Items Information===================================================
lblCostofDrinks = Label(f2aa, font = ('arial', 16, 'bold'), text ="Cost of Drinks", bd = 8)
lblCostofDrinks.grid(row =2, column = 0)
txtCostofDrinks = Entry(f2aa, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable = CostofDrinks)
txtCostofDrinks.grid(row = 2, column = 1)

lblCostofCakes = Label(f2aa, font = ('arial', 16, 'bold'), text ="Cost of Cakes", bd = 8)
lblCostofCakes.grid(row = 3, column = 0)
txtCostofCakes = Entry(f2aa, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable = CostofCakes)
txtCostofCakes.grid(row = 3, column = 1)

lblServiceCharge = Label(f2aa, font = ('arial', 16, 'bold'), text ="Service Charge", bd = 8)
lblServiceCharge.grid(row = 4, column = 0)
txtServiceCharge = Entry(f2aa, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable =ServiceCharge)
txtServiceCharge.grid(row = 4, column = 1)

#=============================================Payment Information==========================================================
lblPaidText = Label(f2ab, font = ('arial', 16, 'bold'), text ="Paid Tax", bd = 8)
lblPaidText.grid(row = 2, column = 0)
txtPaidText = Entry(f2ab, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable = PaidTax)
txtPaidText.grid(row = 2, column = 1)

lblSubTotal = Label(f2ab, font = ('arial', 16, 'bold'), text ="Sub Total", bd = 8)
lblSubTotal.grid(row = 3, column = 0)
txtSubTotal = Entry(f2ab, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable = SubTotal)
txtSubTotal.grid(row = 3, column = 1)

lblTotalCost = Label(f2ab, font = ('arial', 16, 'bold'), text ="Total Cost", bd = 8)
lblTotalCost.grid(row = 4, column = 0)
txtTotalCost = Entry(f2ab, font = ('arial', 16, 'bold'), bd = 8,
                        insertwidth = 2, justify = 'left', textvariable = TotalCost)
txtTotalCost.grid(row = 4, column = 1)

#================================================Button========================================================
btnTotal = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5,
                  text = "Total", command = CostofItem).grid(row = 0, column = 0)
btnReceipt = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5,
                  text = "Receipt", command = Receipt).grid(row = 0, column = 1)
btnReset = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5,
                  text = "Reset", command = Reset).grid(row = 0, column = 2)
btnExit = Button(fb2, padx = 16, pady = 1, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5,
                  text = "Exit", command = qExit).grid(row = 0, column = 3)

root.mainloop()

