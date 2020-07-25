from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = 0

def btn0Click():
    global val
    val = val + "0"
    data.set(val)

def btn1Click():
    global val
    val= val +"1"
    data.set(val)

def btn2Click():
    global  val
    val = val + "2"
    data.set(val)

def btn3Click():
    global val
    val = val + "3"
    data.set(val)

def btn4Click():
     global val
     val = val + "4"
     data.set(val)

def btn5Click():
    global val
    val = val + "5"
    data.set(val)

def btn6Click():
    global val
    val = val + "6"
    data.set(val)

def btn7Click():
    global val
    val = val + "7"
    data.set(val)

def btn8Click():
    global val
    val = val + "8"
    data.set(val)

def btn9Click():
    global val
    val = val + "9"
    data.set(val)

def btnA():
    global val
    global A
    global operator
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btnS():
    global val
    global A
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btnM():
    global  val
    global A
    global operator
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btnMo():
    global val
    global A
    global operator
    A = int(val)
    operator = "%"
    val = val + "%"
    data.set(val)

def btnD():
    global  val
    global  A
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btnClear():
    global val
    global  A
    global  operator
    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A
    global  operator
    global val
    val2 = val
    if operator == "+":
        x = int(val2.split("+")[1])
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int(val2.split("-")[1])
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int(val2.split("*")[1])
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int(val2.split("/")[1])
        if x == 0:
            messagebox.showerror("Error","Division by 0 not support")
            A = ""
            val = ""
            data.set(val)
        else:
            c = int(A / x)
            data.set(c)
            val = str(c)
    elif operator == "%":
            x = int((val2.split("%")[1]))
            if x == 0:
                messagebox.showerror("Error", "Division by 0 not supported")
                A = ""
                val = ""
                data.set(val)
            else:
                c = int(A % x)
                data.set(c)
                val = str(c)

root = Tk()
root.title("Calculater")
root.geometry("260x430+1200+100")
root.resizable(0,0)


data = StringVar()

lbl = Label(root,textvariable=data,background="white",
      text="",anchor=SE,font=(None, 30)).pack(expand=True, fill="both")

btnrow1=Frame(root)
btnrow1.pack(expand= True,fill="both")
btnrow2=Frame(root)
btnrow2.pack(expand= True,fill="both")
btnrow3=Frame(root)
btnrow3.pack(expand= True,fill="both")
btnrow4=Frame(root)
btnrow4.pack(expand= True,fill="both")
# btnrow5=Frame(root, highlightbackground="orange", highlightcolor="orange", highlightthickness=2, bd=3)
# btnrow4.pack(expand= True,fill="both")

# frame = Frame(root, highlightbackground="orange", highlightcolor="orange", highlightthickness=4, bd=0)
# frame.grid(row=0, column=0)
btn1=Button(btnrow1,text="1",command=btn1Click, bg="#FBFCFC")
btn1.pack(side=LEFT,expand="True",fill="both")
btn2=Button(btnrow1,text="2",command=btn2Click, bg="#FBFCFC")
btn2.pack(side=LEFT,expand="True",fill="both")
btn3=Button(btnrow1,text="3",command=btn3Click, bg="#FBFCFC")
btn3.pack(side=LEFT,expand="True",fill="both")
btnplus=Button(btnrow1,text="+",command=btnA, bg="#07F0B6")
btnplus.pack(side=LEFT,expand="True",fill="both")


btn4=Button(btnrow2,text="4",command=btn4Click, bg="#FBFCFC")
btn4.pack(side=LEFT,expand="True",fill="both")
btn5=Button(btnrow2,text="5",command=btn5Click, bg="#FBFCFC")
btn5.pack(side=LEFT,expand="True",fill="both")
btn6=Button(btnrow2,text="6",command=btn6Click, bg="#FBFCFC")
btn6.pack(side=LEFT,expand="True",fill="both")
btnsub=Button(btnrow2,text="-",command=btnS, bg="#07F0B6")
btnsub.pack(side=LEFT,expand="True",fill="both")


btn7=Button(btnrow3,text="7",command=btn7Click, bg="#FBFCFC")
btn7.pack(side=LEFT,expand="True",fill="both")
btn8=Button(btnrow3,text="8",command=btn8Click, bg="#FBFCFC")
btn8.pack(side=LEFT,expand="True",fill="both")
btn9=Button(btnrow3,text="9",command=btn9Click, bg="#FBFCFC")
btn9.pack(side=LEFT,expand="True",fill="both")
btnmul=Button(btnrow3,text="*",command=btnM, bg="#07F0B6")
btnmul.pack(side=LEFT,expand="True",fill="both")


btn0=Button(btnrow4,text="0",command=btn0Click, bg="#FBFCFC")
btn0.pack(side=LEFT,expand="True",fill="both")
btneql=Button(btnrow4,text="=",command=result, bg="#FBFCFC")
btneql.pack(side=LEFT,expand="True",fill="both")
btnmod=Button(btnrow4,text="%",command=btnMo, bg="#FBFCFC")
btnmod.pack(side=LEFT,expand="True",fill="both")
btndiv=Button(btnrow4,text="/",command=btnD, bg="#07F0B6")
btndiv.pack(side=LEFT,expand="True",fill="both")
btnc=Button(root,text="C",command=btnClear, bg="#07F0B6")
btnc.pack(side=BOTTOM,expand="True",fill="both")

root.mainloop()