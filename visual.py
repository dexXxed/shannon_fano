from tkinter import *
from tkinter import messagebox
from script import *


def show_message():
    lst = processing(message.get())
    h = 0
    l = 0
    temp = ''
    for c in lst:
        temp += str(c) + '\n'
        h += c.get_freq() * log2(c.get_freq())
        l += c.get_freq() * len(c.get_code())
    h = abs(h)
    messagebox.showinfo("GUI для алгоритма Шеннона-Фано", temp)
    try:
        messagebox.showinfo("GUI для алгоритма Шеннона-Фано",
                            "H_max = {}\nh = {}\nl_cp = {}\nK_c.c. = {}\nK_o.э. = {}".format(
                                log2(len(lst)), h, l, log2(len(lst)) / l, h / 1))
    except ZeroDivisionError:
        messagebox.showinfo("GUI для алгоритма Шеннона-Фано",
                            "H_max = {}\nh = {}\nl_cp = {}\nK_c.c. = ∞\nK_o.э. = ∞".format(
                                log2(len(lst)), h, l))


root = Tk()
root.title("GUI для алгоритма Шеннона-Фано")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Обработать", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
