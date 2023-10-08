from tkinter import *

# Screen dimensions and title
root = Tk()
root.geometry("1385x320")
root.title("Keyboard")

# Screen frame
key = Frame(root)
key.pack()

# Input field
txt = StringVar()
uinp = Entry(key, state="readonly", width = 170, relief=SUNKEN, textvariable=txt)
uinp.grid(rowspan=1, columnspan=100)
uinp.pack()

# Global variables
is_shift = False
is_symbol = False
is_number = False
inp = " "

# Functions 
def press(num):
    global inp
    inp += str(num)
    uinp.set(inp)

def backspace():
    global inp
    inp = inp[:-1]
    uinp.set(inp)


def shift():
    global is_shift
    is_shift = not is_shift
#    display()

def clear():
    global inp
    inp = " "
    uinp.set(inp)

def display():
    # If SHIFT+SYM enabled
    if (is_symbol and is_shift):
        # First row
        PgUp = Button(key, text='PgUp', width=6, command=lambda: press('J'))
        PgUp.grid(row=1, column=1, ipadx=6, ipady=10)

        Pause = Button(key, text='Pause', width=6, command=lambda: press('J'))
        Pause.grid(row=1, column=2, ipadx=6, ipady=10)

        Home = Button(key, text='Home', width=6, command=lambda: press('J'))
        Home.grid(row=1, column=3, ipadx=6, ipady=10)

        Home2 = Button(key, text='Home', width=6, command=lambda: press('J'))
        Home2.grid(row=1, column=4, ipadx=6, ipady=10)

        Esc = Button(key, text='Esc', width=6, command=lambda: press('J'))
        Esc.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        PgDn = Button(key, text='PgDn', width=6, command=lambda: press('J'))
        PgDn.grid(row=2, column=1, ipadx=6, ipady=10)

        Up = Button(key, text='Up', width=6, command=lambda: press('J'))
        Up.grid(row=2, column=2, ipadx=6, ipady=10)

        Alt = Button(key, text='J', width=6, command=lambda: press('J'))
        Alt.grid(row=2, column=3, ipadx=6, ipady=10)

        Ctrl = Button(key, text='J', width=6, command=lambda: press('J'))
        Ctrl.grid(row=2, column=4, ipadx=6, ipady=10)

        Insert = Button(key, text='J', width=6, command=lambda: press('J'))
        Insert.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        Left = Button(key, text='J', width=6, command=lambda: press('J'))
        Left.grid(row=3, column=1, ipadx=6, ipady=10)

        Down = Button(key, text='J', width=6, command=lambda: press('J'))
        Down.grid(row=3, column=2, ipadx=6, ipady=10)

        Right = Button(key, text='J', width=6, command=lambda: press('J'))
        Right.grid(row=3, column=3, ipadx=6, ipady=10)

        Backspace = Button(key, text='J', width=6, command=lambda: press('J'))
        Backspace.grid(row=3, column=4, ipadx=6, ipady=10)

        Delete = Button(key, text='J', width=6, command=lambda: press('J'))
        Delete.grid(row=3, column=5, ipadx=6, ipady=10)

    # If SHIFT+NUM enabled
    elif(is_shift and is_number):
        # First row
        pound = Button(key, text='#', width=6, command=lambda: press('#'))
        pound.grid(row=1, column=1, ipadx=6, ipady=10)

        dollar = Button(key, text='$', width=6, command=lambda: press('$'))
        dollar.grid(row=1, column=2, ipadx=6, ipady=10)

        equals = Button(key, text='=', width=6, command=lambda: press('='))
        equals.grid(row=1, column=3, ipadx=6, ipady=10)

        plus = Button(key, text='+', width=6, command=lambda: press('+'))
        plus.grid(row=1, column=4, ipadx=6, ipady=10)

        blank = Button(key, text=' ', width=6, command=lambda: press(''))
        blank.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        power = Button(key, text='^', width=6, command=lambda: press('^'))
        power.grid(row=2, column=1, ipadx=6, ipady=10)

        tilde = Button(key, text='~', width=6, command=lambda: press('~'))
        tilde.grid(row=2, column=2, ipadx=6, ipady=10)

        line = Button(key, text='|', width=6, command=lambda: press('|'))
        line.grid(row=2, column=3, ipadx=6, ipady=10)

        percent = Button(key, text='%', width=6, command=lambda: press('%'))
        percent.grid(row=2, column=4, ipadx=6, ipady=10)

        backslash = Button(key, text='\\', width=6, command=lambda: press('\\'))
        backslash.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        rightcurl = Button(key, text='}', width=6, command=lambda: press('}'))
        rightcurl.grid(row=3, column=1, ipadx=6, ipady=10)

        rightsq = Button(key, text=']', width=6, command=lambda: press(']'))
        rightsq.grid(row=3, column=2, ipadx=6, ipady=10)

        rightbra = Button(key, text=')', width=6, command=lambda: press(')'))
        rightbra.grid(row=3, column=3, ipadx=6, ipady=10)

        greaterthan = Button(key, text='>', width=6, command=lambda: press('>'))
        greaterthan.grid(row=3, column=4, ipadx=6, ipady=10)

        backtick = Button(key, text='`', width=6, command=lambda: press('`'))
        backtick.grid(row=3, column=5, ipadx=6, ipady=10)

    # If SYM enabled
    elif(is_symbol):
        # First row
        semicolon = Button(key, text=';', width=6, command=lambda: press(';'))
        semicolon.grid(row=1, column=1, ipadx=6, ipady=10)

        colon = Button(key, text=':', width=6, command=lambda: press(':'))
        colon.grid(row=1, column=2, ipadx=6, ipady=10)

        asterisk = Button(key, text='*', width=6, command=lambda: press('*'))
        asterisk.grid(row=1, column=3, ipadx=6, ipady=10)

        ampersand = Button(key, text='&', width=6, command=lambda: press('&'))
        ampersand.grid(row=1, column=4, ipadx=6, ipady=10)

        question = Button(key, text='?', width=6, command=lambda: press('?'))
        question.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        underscore = Button(key, text='_', width=6, command=lambda: press('_'))
        underscore.grid(row=2, column=1, ipadx=6, ipady=10)

        at = Button(key, text='@', width=6, command=lambda: press('@'))
        at.grid(row=2, column=2, ipadx=6, ipady=10)

        hyphen = Button(key, text='-', width=6, command=lambda: press('-'))
        hyphen.grid(row=2, column=3, ipadx=6, ipady=10)

        exclaim = Button(key, text='!', width=6, command=lambda: press('!'))
        exclaim.grid(row=2, column=4, ipadx=6, ipady=10)

        slash = Button(key, text='/', width=6, command=lambda: press('/'))
        slash.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        leftcurl = Button(key, text='{', width=6, command=lambda: press('{'))
        leftcurl.grid(row=3, column=1, ipadx=6, ipady=10)

        leftsq = Button(key, text='[', width=6, command=lambda: press('['))
        leftsq.grid(row=3, column=2, ipadx=6, ipady=10)

        leftbra = Button(key, text='(', width=6, command=lambda: press('('))
        leftbra.grid(row=3, column=3, ipadx=6, ipady=10)

        lessthan = Button(key, text='<', width=6, command=lambda: press('<'))
        lessthan.grid(row=3, column=4, ipadx=6, ipady=10)

        doublequot = Button(key, text='\"', width=6, command=lambda: press('\"'))
        doublequot.grid(row=3, column=5, ipadx=6, ipady=10)

    # If NUM enabled
    elif(is_number):
        # First row
        star = Button(key, text='*', width=6, command=lambda: press('*'))
        star.grid(row=1, column=1, ipadx=6, ipady=10)

        num7 = Button(key, text='7', width=6, command=lambda: press('7'))
        num7.grid(row=1, column=2, ipadx=6, ipady=10)

        num8 = Button(key, text='8', width=6, command=lambda: press('8'))
        num8.grid(row=1, column=3, ipadx=6, ipady=10)

        num9 = Button(key, text='9', width=6, command=lambda: press('9'))
        num9.grid(row=1, column=4, ipadx=6, ipady=10)

        dash = Button(key, text='-', width=6, command=lambda: press('-'))
        dash.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        slash2 = Button(key, text='/', width=6, command=lambda: press('/'))
        slash2.grid(row=2, column=1, ipadx=6, ipady=10)

        num4 = Button(key, text='4', width=6, command=lambda: press('4'))
        num4.grid(row=2, column=2, ipadx=6, ipady=10)

        num5 = Button(key, text='5', width=6, command=lambda: press('5'))
        num5.grid(row=2, column=3, ipadx=6, ipady=10)

        num6 = Button(key, text='6', width=6, command=lambda: press('6'))
        num6.grid(row=2, column=4, ipadx=6, ipady=10)

        add = Button(key, text='+', width=6, command=lambda: press('+'))
        add.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        num0 = Button(key, text='0', width=6, command=lambda: press('0'))
        num0.grid(row=3, column=1, ipadx=6, ipady=10)

        num1 = Button(key, text='1', width=6, command=lambda: press('1'))
        num1.grid(row=3, column=2, ipadx=6, ipady=10)

        num2 = Button(key, text='2', width=6, command=lambda: press('2'))
        num2.grid(row=3, column=3, ipadx=6, ipady=10)

        num3 = Button(key, text='3', width=6, command=lambda: press('3'))
        num3.grid(row=3, column=4, ipadx=6, ipady=10)

        dot = Button(key, text='.', width=6, command=lambda: press('.'))
        dot.grid(row=3, column=5, ipadx=6, ipady=10)

    # If only SHIFT enabled
    elif (is_shift):
        # First row
        J = Button(key, text='J', width=6, command=lambda: press('J'))
        J.grid(row=1, column=1, ipadx=6, ipady=10)
        
        M = Button(key, text='M', width=6, command=lambda: press('M'))
        M.grid(row=1, column=2, ipadx=6, ipady=10)
        
        B = Button(key, text='B', width=6, command=lambda: press('B'))
        B.grid(row=1, column=3, ipadx=6, ipady=10)
        
        accent = Button(key, text='´', width=6, command=lambda: press('´'))
        accent.grid(row=1, column=4, ipadx=6, ipady=10)
        
        tab_button = Button(key, text='Tab', width=6, command=lambda: press('\t'))
        tab_button.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        V = Button(key, text='V', width=6, command=lambda: press('V'))
        V.grid(row=2, column=1, ipadx=6, ipady=10)

        C = Button(key, text='C', width=6, command=lambda: press('C'))
        C.grid(row=2, column=2, ipadx=6, ipady=10)

        L = Button(key, text='L', width=6, command=lambda: press('L'))
        L.grid(row=2, column=3, ipadx=6, ipady=10)

        Z = Button(key, text='Z', width=6, command=lambda: press('Z'))
        Z.grid(row=2, column=4, ipadx=6, ipady=10)

        Q = Button(key, text='Q', width=6, command=lambda: press('Q'))
        Q.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        X = Button(key, text='X', width=6, command=lambda: press('X'))
        X.grid(row=3, column=1, ipadx=6, ipady=10)

        G = Button(key, text='G', width=6, command=lambda: press('G'))
        G.grid(row=3, column=2, ipadx=6, ipady=10)

        K = Button(key, text='K', width=6, command=lambda: press('K'))
        K.grid(row=3, column=3, ipadx=6, ipady=10)

        app = Button(key, text='App', width=6, command=lambda: press('app'))
        app.grid(row=3, column=4, ipadx=6, ipady=10)

        meta = Button(key, text='Meta', width=6, command=lambda: press('meta'))
        meta.grid(row=3, column=5, ipadx=6, ipady=10)

    else:
        # First row
        P = Button(key, text='P', width=6, command=lambda: press('P'))
        P.grid(row=1, column=1, ipadx=6, ipady=10)

        W = Button(key, text='W', width=6, command=lambda: press('W'))
        W.grid(row=1, column=2, ipadx=6, ipady=10)

        R = Button(key, text='R', width=6, command=lambda: press('R'))
        R.grid(row=1, column=3, ipadx=6, ipady=10)

        A = Button(key, text='A', width=6, command=lambda: press('A'))
        A.grid(row=1, column=4, ipadx=6, ipady=10)

        F = Button(key, text='F', width=6, command=lambda: press('F'))
        F.grid(row=1, column=5, ipadx=6, ipady=10)

        # Second row
        D = Button(key, text='D', width=6, command=lambda: press('D'))
        D.grid(row=2, column=1, ipadx=6, ipady=10)


        T = Button(key, text='T', width=6, command=lambda: press('T'))
        T.grid(row=2, column=2, ipadx=6, ipady=10)

        H = Button(key, text='H', width=6, command=lambda: press('H'))
        H.grid(row=2, column=3, ipadx=6, ipady=10)

        E = Button(key, text='E', width=6, command=lambda: press('E'))
        E.grid(row=2, column=4, ipadx=6, ipady=10)

        O = Button(key, text='O', width=6, command=lambda: press('O'))
        O.grid(row=2, column=5, ipadx=6, ipady=10)

        # Third row
        Y = Button(key, text='Y', width=6, command=lambda: press('Y'))
        Y.grid(row=3, column=1, ipadx=6, ipady=10)

        S = Button(key, text='S', width=6, command=lambda: press('S'))
        S.grid(row=3, column=2, ipadx=6, ipady=10)

        N = Button(key, text='J', width=6, command=lambda: press('N'))
        N.grid(row=3, column=3, ipadx=6, ipady=10)

        I = Button(key, text='J', width=6, command=lambda: press('I'))
        I.grid(row=3, column=4, ipadx=6, ipady=10)

        U = Button(key, text='J', width=6, command=lambda: press('U'))
        U.grid(row=3, column=5, ipadx=6, ipady=10)



root.mainloop()