from tkinter import *
import tkinter.messagebox
from multiprocessing import Process, Queue

from collections import deque

message_queue = Queue()

tk = Tk()
tk.title("Tic Tac Toe")
tk2 = Tk()
tk2.title("Tic tac toe 2")



pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    message_queue.put(buttons)
    return 0


def btnClickCheck():
    buttons = message_queue.get()
    nr = buttons
    if buttons<=9 and buttons>=1:
        if buttons==1:
            buttons = button1
        elif buttons == 2:
            buttons = button2
        elif buttons== 3:
            buttons = button3
        elif buttons == 4:
            buttons=button4
        elif buttons == 5:
            buttons = button5
        elif buttons == 6:
            buttons = button6
        elif buttons == 7:
            buttons = button7
        elif buttons == 8:
            buttons = button8
        elif buttons == 9:
            buttons = button9
        else: return 0
        global bclick, flag, player2_name, player1_name, playerb, pa
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            flag += 1
        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        if nr <= 9 and nr >= 1:
            if nr == 1:
                buttons = button12
            elif nr == 2:
                buttons = button22
            elif nr == 3:
                buttons = button32
            elif nr == 4:
                buttons = button42
            elif nr == 5:
                buttons = button52
            elif nr == 6:
                buttons = button62
            elif nr == 7:
                buttons = button72
            elif nr == 8:
                buttons = button82
            elif nr == 9:
                buttons = button92
            else:
                return 0
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            bclick = False
            playerb = p2.get() + " Wins!"
            pa = p1.get() + " Wins!"
            checkForWin()
            flag += 1
        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


buttons = StringVar()

label = Label(tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(1), btnClickCheck()])
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(2), btnClickCheck()])
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(3), btnClickCheck()])
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(4), btnClickCheck()])
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(5), btnClickCheck()])
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(6), btnClickCheck()])
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(7), btnClickCheck()])
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(8), btnClickCheck()])
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(9), btnClickCheck()])
button9.grid(row=5, column=2)






label2 = Label(tk2, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label2.grid(row=2, column=0)

button12 = Button(tk2, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(1), btnClickCheck()])
button12.grid(row=3, column=0)

button22 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(2), btnClickCheck()])
button22.grid(row=3, column=1)

button32 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(3), btnClickCheck()])
button32.grid(row=3, column=2)

button42 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(4), btnClickCheck()])
button42.grid(row=4, column=0)

button52 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(5), btnClickCheck()])
button52.grid(row=4, column=1)

button62 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(6), btnClickCheck()])
button62.grid(row=4, column=2)

button72 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(7), btnClickCheck()])
button72.grid(row=5, column=0)

button82 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(8), btnClickCheck()])
button82.grid(row=5, column=1)

button92 = Button(tk2, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: [btnClick(9), btnClickCheck()])
button92.grid(row=5, column=2)


joc1 = Process(target=tk.mainloop(), args=(message_queue,))
joc2 = Process(target=tk2.mainloop(), args=(message_queue,))

joc1.start()
joc2.start()

joc1.join()
joc2.join()

