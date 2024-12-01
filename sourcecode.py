from customtkinter import *
from tkinter import messagebox
import keyboard

app=CTk()
app.title('Binary2Pynumber -By Anes Hammouche V1.0')
app.iconbitmap('data/img/high_icon.ico')
app.geometry("800x600")
app.resizable(False,False)
title=CTkLabel(app,text="Binary2Pynumber",font=("Roman",65),text_color="white")
title.pack()
sub_title=CTkLabel(app,text="By Anes Hammouche",font=("Showcard Gothic",20),text_color="#ea3b38")
sub_title.pack()
gide=CTkLabel(app,text='"Convert your binary number to real number"',font=("Lucida Console",20),text_color="white")
gide.pack(pady=20)
ent=CTkEntry(app,width=500,height=40,placeholder_text="Enter the binary number",font=("Lucida Console",20))
ent.pack(pady=22)
out=CTkTextbox(app,width=780,height=260,font=("Showcard Gothic",20))
out.place(x=10,y=320)
def error():
    messagebox.showerror("Input Error", "Please enter only 0 or 1.")

filterr=[2,3,4,5,6,7,8,9]
out_des='''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
'''
def convert():
    try:
        bina=ent.get()
    except:
        error()
    if all(char in "01" for char in bina):
       try:
         out.configure(state="normal")
         converted=int(bina,2)
         text=str(converted)
         out.delete(0.0,"end")
         out.insert("0.0",text=out_des+'\n'+'Your number is:'+text)
         out.configure(state="disabled")
       except:
            error()            

    else:
        error()
        




  
    





bn=CTkButton(app,text="Convert!",font=("Lucida Console",20),fg_color="#38eabc",hover_color="#23c299",height=50,command=convert)
bn.place(x=350,y=260)



keyboard.add_hotkey("enter",convert)



app.mainloop()