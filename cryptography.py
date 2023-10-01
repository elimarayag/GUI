from tkinter import *
from tkinter import messagebox

class CryptographyGUI(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Cryptography GUI")
        self.pack()

        self.label = Label(self, text = "Cryptography" , fg = "blue", font = ("Calibri 25 italic"))
        self.label.pack(padx = 50)
        self.label.pack(pady = 30)

        self.entry = Entry(self, font = ("Calibri 15 bold"))
        self.label.pack(padx = 50)
        self.entry.pack(pady = 30)

        self.variable = Variable()
        self.entry1 = Entry(self, font = ("Calibri 15 bold"), textvariable = self.variable)
        self.label.pack(padx = 50)
        self.entry1.pack(pady = 30)

        self.btn = Button(self, text = "Encrypt", fg = "red", font = ("Calibri 15"), command = self.encryption)
        self.label.pack(padx = 50)
        self.btn.pack(pady = 30)

        self.btn = Button(self, text = "Decrypt", fg = "red", font = ("Calibri 15"), command = self.decryption)
        self.label.pack(padx = 50)
        self.btn.pack(pady = 30)

    def encryption(self):
        try:
            content = self.entry.get()
            n = int(self.variable.get())
            code = ""
            for x in content:
                ordVal = ord(x) 
                cipherVal = ordVal + n
                if cipherVal > ord('z'):
                    cipherVal = ord('a') + n - \
                (ord('z') - ordVal + 1)
                code += chr(cipherVal) 
                print("ch: ", x)
                print("oc: ", ordVal)
                print("cV: ", cipherVal)
            print(code)

            messagebox.showinfo("Result", f"The encrypted message is: {code}") 
       
        except ValueError:
            messagebox.showerror("ERROR") 

    def decryption(self):
        try:
            content = self.entry.get()
            n = int(self.variable.get())
            text = ""
            for x in content:
                ordVal = ord(x)
                cipherVal = ordVal - n
                if cipherVal < ord('a'):
                    cipherVal = ord('z') - \
                (n - (ord('a') - ordVal + 1 ))
                text += chr(cipherVal)
                print("ch: ", x)
                print("oc: ", ordVal)
                print("cV: ", cipherVal)
            print(text)
            
            messagebox.showinfo("Result", f"The decrypted message is: {text}")
        except ValueError:
            messagebox.showerror("ERROR")
def main():

    CryptographyGUI().mainloop()
main()