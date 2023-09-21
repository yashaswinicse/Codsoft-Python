import tkinter
import tkinter as tk
cal=" "

def click(symbol):
   global cal
   cal += str(symbol)
   result.delete(1.0, "end")
   result.insert(1.0,cal)

def evaluate():
    global cal
    try:
        res = str(eval(cal))
        cal = " "
        result.delete(1.0,"end")
        result.insert(1.0,res)
    except:
        clear()
        result.insert(1.0,"Error")

def clear():
    global cal
    cal = " "
    result.delete(1.0,"end")
   
root= tk.Tk()
root.title("CALCULATOR")
root.config(bg="black")
root.geometry("350x310")
result = tk.Text(root,height= 2,width=22, font=("Arial",22),bg="darkgrey")
result.grid(columnspan = 5)

btn0 = tk.Button(root,text= '0',command=lambda: click(0),width=5,font=("Times Roman",16))
btn0.grid(row=5,column=0,pady=3)
btn = tk.Button(root,text=".",command=lambda: click("."),width=5,font=("Times Roman",16))
btn.grid(row=5,column=1,pady=3)
btn_equals = tk.Button(root,text= '=',command= evaluate,width=5,font=("Times Roman",16))
btn_equals.grid(row=5,column=2,pady=3)
btn1 = tk.Button(root,text= '1',command=lambda: click(1),width=5,font=("Times Roman",16))
btn1.grid(row=4,column=0,pady=3)
btn2 = tk.Button(root,text= '2',command=lambda: click(2),width=5,font=("Times Roman",16))
btn2.grid(row=4,column=1,pady=3)
btn3 = tk.Button(root,text= '3',command=lambda: click(3),width=5,font=("Times Roman",16))
btn3.grid(row=4,column=2,pady=3)
btn4 = tk.Button(root,text= '4',command=lambda: click(4),width=5,font=("Times Roman",16))
btn4.grid(row=3,column=0,pady=3)
btn5 = tk.Button(root,text= '5',command=lambda: click(5),width=5,font=("Times Roman",16))
btn5.grid(row=3,column=1,pady=3)
btn6 = tk.Button(root,text= '6',command=lambda: click(6),width=5,font=("Times Roman",16))
btn6.grid(row=3,column=2,pady=3)
btn7 = tk.Button(root,text= '7',command=lambda: click(7),width=5,font=("Times Roman",16))
btn7.grid(row=2,column=0,pady=3)
btn8 = tk.Button(root,text= '8',command=lambda: click(8),width=5,font=("Times Roman",16))
btn8.grid(row=2,column=1,pady=3)
btn9 = tk.Button(root,text= '9',command=lambda: click(9),width=5,font=("Times Roman",16))
btn9.grid(row=2,column=2,pady=3)
div = tk.Button(root,text= '/',command=lambda: click('/'),width=5,font=("Times Roman",16))
div.grid(row=2,column=4,pady=3)
mul = tk.Button(root,text= '*',command=lambda: click('*'),width=5,font=("Times Roman",16))
mul.grid(row=3,column=4,pady=3)
min = tk.Button(root,text= '-',command=lambda: click('-'),width=5,font=("Times Roman",16))
min.grid(row=4,column=4,pady=3)
sum = tk.Button(root,text= '+',command=lambda: click('+'),width=5,font=("Times Roman",16))
sum.grid(row=5,column=4,pady=3)
btn_clear= tk.Button(root,text= 'Clear',command= clear,width=15,font=("Times Roman",16))
btn_clear.grid(row=6,column=0,columnspan=4,pady=3)

root.mainloop()