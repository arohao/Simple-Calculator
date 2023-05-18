"""
Simple Calculator
arohao
May 17th, 2023

This python calculator uses tkinter to create a GUI, and can perform
basic functions: addition, subtraction, multiplication, and division.

"""


from tkinter import *

# Window and number display
tk = Tk()
dis = Entry(tk, width=35, borderwidth=2, state='readonly', readonlybackground="white")
dis.grid(row=0, column=0, columnspan=4)


# Methods
operationStorage = {}
op = True
error = False

def onPress(n):
    """
    :param n: int
    :return: void

    Each number n gets added to the display.


    """
    dis.configure(state='normal')

    global op
    if op:
        dis.delete(0,END)
        op = False

    global error
    if error:
        error = False
        clr()

    cur = dis.get()
    dis.delete(0,END)
    dis.insert(0, cur + str(n))
    dis.configure(state='readonly')

def add():
    """
    :param: void
    :return: void

    Command of the Addition button
    """
    if len(operationStorage) == 1:
        eq()

    operationStorage.update({"add": dis.get()})
    global op
    op = True

def sub():
    """
    :param: void
    :return: void

    Command of the Subtraction button
    """
    if len(operationStorage) == 1:
        eq()

    operationStorage.update({"sub": dis.get()})
    global op
    op = True

def mul():
    """
    :param: void
    :return: void

    Command of the Multiplication button
    """
    if len(operationStorage) == 1:
        eq()

    operationStorage.update({"mul": dis.get()})
    global op
    op = True

def div():
    """
    :param: void
    :return: void

    Command of the Division button
    """
    if len(operationStorage) == 1:
        eq()

    operationStorage.update({"div": dis.get()})
    global op
    op = True

def eq():
    """
    :param: void
    :return: void

    Displays the outcome of operations done to a number
    """
    dis.configure(state='normal')

    if not dis.get():
        err()
        return

    result = dis.get()

    try:
        result = float(result)
    except TypeError:
        err()
        return
    except ValueError:
        err()
        return

    if "add" in operationStorage:
        if not operationStorage["add"]:
            err()
            return

        try:
            result += float(operationStorage["add"])
        except TypeError:
            err()
            return
        except ValueError:
            err()
            return

    elif "sub" in operationStorage:
        if not operationStorage["sub"]:
            err()
            return

        try:
            result -= float(operationStorage["sub"])
            result *= -1
        except TypeError:
            err()
            return
        except ValueError:
            err()
            return

    elif "mul" in operationStorage:
        if not operationStorage["mul"]:
            err()
            return

        try:
            result *= float(operationStorage["mul"])
        except TypeError:
            err()
            return
        except ValueError:
            err()
            return

    elif "div" in operationStorage:
        if not operationStorage["div"] or result == 0:
            err()
            return

        try:
            result = float(operationStorage["div"]) / result
        except TypeError:
            err()
            return
        except ValueError:
            err()
            return

    if result % 1 == 0:
        result = int(result)

    dis.delete(0, END)
    dis.insert(0, str(result))

    dis.configure(state='readonly')
    operationStorage.clear()

def clr():
    """
    :param: void
    :return: void

    Clears the display and cache of operations
    """
    dis.configure(state='normal')

    if not dis.get():
        return

    if len(operationStorage) > 0:
        operationStorage.clear()

    dis.delete(0,END)

    global op
    op = True
    dis.configure(state='readonly')

def err():
    """
    :param: void
    :return: void

    Displays 'ERROR', runs clr()
    """

    clr()
    dis.configure(state='normal')
    dis.insert(0,"ERROR")
    dis.configure(state='readonly')

    global error
    error = True

def dot():
    """
    :param: void
    :return: void

    Period for decimal numbers
    """
    dis.configure(state='normal')
    cur = dis.get()

    global op
    if op:
        dis.delete(0, END)
        dis.insert(0, "0")
        op = False

    if not cur:
        dis.insert(0, "0.")
        return

    dis.insert(END,".")
    dis.configure(state='readonly')


# Button setup
buttons = []
row = 4
col = 2

for i in range(0,10): # This loop creates all the number buttons
    if (i-1)%3 == 0 and i != 0:
        row -= 1
        col = 2
    buttons.append(Button(tk, text=str(i),padx=20, pady=20, command= lambda i=i: onPress(i)))
    if i == 0:
        buttons[i].grid(row=4, column=1)
    else:
        buttons[i].grid(row=row,column=col)
        col -= 1

# Operation Buttons

addition = Button(tk, text="+", padx=20, pady=20, command= lambda: add())
addition.grid(row=4, column=3)

subtraction = Button(tk, text="-", padx=20, pady=20, command= lambda: sub())
subtraction.grid(row=3, column=3)

multiplication = Button(tk, text="x", padx=20, pady=20, command= lambda: mul())
multiplication.grid(row=2, column=3)

division = Button(tk, text="/", padx=20, pady=20, command= lambda: div())
division.grid(row=1, column=3)

equals = Button(tk, text="=", padx=20, pady=20, command=lambda:eq())
equals.grid(row=4,column=0)

clear = Button(tk, text="C", padx=20, pady=4, command= lambda: clr())
clear.grid(row=4,column=2, sticky=N)

period = Button(tk, text=".", padx=20, pady=4, command= lambda:dot())
period.grid(row=4,column=2, sticky=E+W+S)

tk.mainloop()