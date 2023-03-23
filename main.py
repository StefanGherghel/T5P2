import os
import tkinter as tk
from multiprocessing import Process, Queue
# from queue import Queue
from collections import deque
from multiprocessing import Process, Queue
# from queue import Queue
from collections import deque


class Parser:
    pass

Parser
message_queue = Queue()
# message_queue.put(deque([]))


def procesare_impare(message_queue,integer_list_text):
    result = integer_list_text.get("1.0", tk.END)
    result = [int(item) for item in result.split(',')]
    integer_list_text = result
    for i in integer_list_text:
        if i % 2 == 1:
            integer_list_text.remove(i)
    print(result)


def task_creator(int_list, message_queue):
    all_messages = message_queue.get()
    try:
        # message = all_messages.pop()
        if 'filtrare' in all_messages:
            filtrare = Process(target=procesare_impare, args=(message_queue,int_list))
            filtrare.start()
            filtrare.join()
            all_messages = all_messages.replace('filtrare', '')
        message_queue.put(all_messages)
    except IndexError:
        print("Task1: Empty message queue")


class Parser:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    A = None
    B = None

    def __init__(self, gui):
        self.gui = gui
        self.gui.title('Exemplul 1 cu Tkinter')

        self.gui.geometry("600x100")

        self.integer_list_lbl = tk.Label(master=self.gui,text="List of integers:")
        self.todo0_lbl = tk.Label(master=self.gui, text="TODO_0: Add a Text field to display the result")
        self.todo1_lbl = tk.Label(master=self.gui, text="TODO_1: Add a button for each operation")

        self.add_list_btn = tk.Button(master=self.gui, text="Add list", command=self.add_list)
        self.add_list_btn_impare = tk.Button(master=self.gui, text="Filtrare impare", command=self.filtrare_impare)

        self.integer_list_text = tk.Text(self.gui, width=50, height=1)
        self.integer_list_text.insert(tk.END, str(list(range(1, 16)))[1:-1])

    # alignment on the grid
        self.integer_list_lbl.grid(row=0, column=0)
        self.todo0_lbl.grid(row=1, column=1)
        self.todo1_lbl.grid(row=2, column=1)
        self.integer_list_text.grid(row=0, column=1)
        self.add_list_btn.grid(row=0, column=2)
        self.add_list_btn_impare.grid(row=1, column=2)
        self.gui.mainloop()

    def add_list(self):
        result = self.integer_list_text.get("1.0", tk.END)
        result = result.strip().replace(' ', '')
        result = [int(item) for item in result.split(',')]
        self.integer_list = result
        print(result)
    def filtrare_impare(self):
        message_queue.put("filtrare")
        process0 = Process(target=task_creator, args=(self.integer_list_text,message_queue))
        process0.start()
        process0.join()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Exemplul 1 cu Tkinter')
    app = Parser(root)      # am pornit ecranul grafic


