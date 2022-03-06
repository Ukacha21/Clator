from tkinter import *

class Main():

    res = ""

    def write(self, i, *args):
        if i == "c":
            self.res = ""
            numLabel.config(text=self.res)
            mainLabel.config(text="start typing...")
        elif i == "b":
            self.res = self.res[0:-1]
            numLabel.config(text=self.res)
        else:
            try:
                self.res = str(self.res+i)
                numLabel.config(text=self.res)
                mainLabel.config(text="")

                #print(self.res)
            except:
                mainLabel.config(text="an error happened\n(●'◡'●)")


    def equal(self, *args):
        try:
            fres = eval(str(self.res))
            mainLabel.config(text="the result is:")
            numLabel.config(text=fres)
            #print(fres)
            self.res = ""
        except SyntaxError:
            mainLabel.config(text="an error happened\n(●'◡'●)")
            self.res = ""
            numLabel.config(text=self.res)
            
    
    def run(self):
        global root
        global mainframe
        global mainLabel
        global numLabel
        root = Tk()
        #root.iconbitmap("logo.ico")
        root.title("Clator")
        root.geometry("365x500")
        root.resizable(False, False)
        #root.attributes("-transparentcolor", "#446877")
        root.attributes("-alpha", 0.95)

        mainframe = Frame(root, width=365, height=500, bg="#446877")
        mainLabel = Label(root, text="start typing...", font=("arial italic", 11), bg="#446877", fg="white")
        numLabel = Label(root, font=("Segoe ui variable", 16), text="", bg="#446877", fg="white")
        mainframe.pack()
        mainLabel.place(x=0, y=0)
        numLabel.place(y=90, anchor="w")



        one = Button(root, bd=0, text="1", font=("Segoe ui variable", 16),  width=8, height=4, bg="#19a597", command=lambda: self.write("1") )
        two = Button(root, bd=0, text="2", font=("Segoe ui variable", 16),  width=8, height=4, bg="#19a597", command=lambda: self.write("2"))
        three = Button(root, bd=0, text="3", font=("Segoe ui variable", 16),  width=8, height=4, bg="#19a597", command=lambda: self.write("3"))
        four = Button(root, bd=0, text="4", font=("Segoe ui variable", 16),  width=8, height=4, bg="#19a597", command=lambda: self.write("4"))
        five = Button(root, bd=0, text="5", font=("Segoe ui variable", 16),  width=8, height=4,bg="#19a597", command=lambda: self.write("5"))
        six = Button(root, bd=0, text="6", font=("Segoe ui variable", 16),  width=8, height=4,bg="#19a597", command=lambda: self.write("6"))
        seven = Button(root, bd=0, text="7", font=("Segoe ui variable", 16),  width=8, height=4, bg="#19a597", command=lambda: self.write("7"))
        eight = Button(root, bd=0, text="8", font=("Segoe ui variable", 16),  width=8, height=4,bg="#19a597", command=lambda: self.write("8"))
        nine = Button(root, bd=0, text="9", font=("Segoe ui variable", 16),  width=8, height=4,bg="#19a597", command=lambda: self.write("9"))
        
        zero = Button(root, bd=0, text="0", font=("Segoe ui variable", 16),  width=8, height=4, bg="#56a9d8", command=lambda: self.write("0"))

        equal = Button(root, bd=0, text="=", font=("Segoe ui variable", 17), width=18, height=4, bg="#2b69ad", fg="white", command=lambda: self.equal())
        

        plus = Button(root, bd=0, text="+", font=("Segoe ui variable", 16), width=4, height=2, bg="#56a9d8", fg="white", command=lambda: self.write("+"))
        minus = Button(root, bd=0, text="-", font=("Segoe ui variable", 16), width=4, height=2, bg="#56a9d8", fg="white", command=lambda: self.write("-"))
        multiply = Button(root, bd=0, text="*", font=("Segoe ui variable", 16), width=4, height=2, bg="#56a9d8", fg="white", command=lambda: self.write("*"))
        divide = Button(root, bd=0, text="/", font=("Segoe ui variable", 16), width=4, height=2, bg="#56a9d8", fg="white", command=lambda: self.write("/"))
        
        wipeall = Button(root, bd=0, text="C", font=("Segoe ui variable", 16), width=4, height=4, bg="#56a9d8", fg="white", command=lambda: self.write("c"))
        back = Button(root, bd=0, text="<<", font=("Segoe ui variable", 16), width=4, height=2, bg="#56a9d8", fg="white", command=lambda: self.write("b"))
        
        
        one.place(x=1, y=100)
        two.place(x=104, y=100)
        three.place(x=207, y=100)

        four.place(x=1, y=203)
        five.place(x=104, y=203)
        six.place(x=207, y=203)

        seven.place(x=1, y=306)
        eight.place(x=104, y=306)
        nine.place(x=207, y=306)

        zero.place(x=1, y=409)

        equal.place(x=104, y=409)

        plus.place(x=310, y=156)
        minus.place(x=310, y=219)
        multiply.place(x=310, y=282)
        divide.place(x=310, y=345)

        wipeall.place(x=310, y=408)
        back.place(x=310, y=100)

        return root.mainloop()

Main().run()