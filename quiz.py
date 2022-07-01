from random import randint, random, shuffle
import random



lines = []
randoms = []
answer_code = []
questions = []

for i in range(4):
    
    rnd = random.sample(range(0, 10), 4)

    for i in range(4):
        f = open("/home/ali/Desktop/python_projects/quiz/question.txt", "r")
        temp = str(f.readlines()[rnd[i]:rnd[i]+1])
        f.close()
        answer_code.append(int((temp[len(temp)-6:len(temp)-4]))-1)
        lines.append(temp[2:len(temp)-6])

    


for i in range(4):
    for j in range(4):
        line_id = (int(answer_code[i])+j)
        # print(line_id)

        f = open("/home/ali/Desktop/python_projects/quiz/question.txt", "r")
        answer_temp = (str(f.readlines()[line_id:line_id+1]))


        questions.append(answer_temp[2:len(answer_temp)-4])
        f.close()


from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window=Tk()


lbl=Label(window, text="wellcome to quiz", fg='red', font=("Helvetica", 16))
lbl.place(x=120, y=10)


q1=Label(window, text=lines[0], fg='red', font=("Helvetica", 16))
q1.place(x=120, y=60)
v0=IntVar()
v0.set(0)
shuffle1 = random.sample(range(0, 4), 4)
r1=Radiobutton(window, text=questions[shuffle1[0]], variable=v0,value=shuffle1[0])
r1.place(x=20,y=90)
r2=Radiobutton(window, text=questions[shuffle1[1]], variable=v0,value=shuffle1[1])
r2.place(x=20, y=120)
r3=Radiobutton(window, text=questions[shuffle1[2]], variable=v0,value=shuffle1[2])
r3.place(x=20,y=150)
r4=Radiobutton(window, text=questions[shuffle1[3]], variable=v0,value=shuffle1[3])
r4.place(x=20, y=180)




q2=Label(window, text=lines[1], fg='red', font=("Helvetica", 16))
q2.place(x=120, y=260)
v1=IntVar()
v1.set(1)
shuffle2 = random.sample(range(4, 8), 4)
r5=Radiobutton(window, text=questions[shuffle2[0]], variable=v1,value=shuffle2[0])
r5.place(x=20,y=290)
r6=Radiobutton(window, text=questions[shuffle2[1]], variable=v1,value=shuffle2[1])
r6.place(x=20, y=320)
r7=Radiobutton(window, text=questions[shuffle2[2]], variable=v1,value=shuffle2[2])
r7.place(x=20,y=350)
r8=Radiobutton(window, text=questions[shuffle2[3]], variable=v1,value=shuffle2[3])
r8.place(x=20, y=380)



q3=Label(window, text=lines[2], fg='red', font=("Helvetica", 16))
q3.place(x=120, y=460)
v2=IntVar()
v2.set(1)
shuffle3 = random.sample(range(8, 12), 4)
r9=Radiobutton(window, text=questions[shuffle3[0]], variable=v2,value=shuffle3[0])
r9.place(x=20,y=490)
r10=Radiobutton(window, text=questions[shuffle3[1]], variable=v2,value=shuffle3[1])
r10.place(x=20, y=520)
r11=Radiobutton(window, text=questions[shuffle3[2]], variable=v2,value=shuffle3[2])
r11.place(x=20,y=550)
r12=Radiobutton(window, text=questions[shuffle3[3]], variable=v2,value=shuffle3[3])
r12.place(x=20, y=580)



q4=Label(window, text=lines[3], fg='red', font=("Helvetica", 16))
q4.place(x=120, y=640)
v3=IntVar()
v3.set(1)
shuffle4 = random.sample(range(12, 16), 4)
r13=Radiobutton(window, text=questions[shuffle4[0]], variable=v3,value=shuffle4[0])
r13.place(x=20,y=670)
r14=Radiobutton(window, text=questions[shuffle4[1]], variable=v3,value=shuffle4[1])
r14.place(x=20, y=700)
r15=Radiobutton(window, text=questions[shuffle4[2]], variable=v3,value=shuffle4[2])
r15.place(x=20,y=730)
r16=Radiobutton(window, text=questions[shuffle4[3]], variable=v3,value=shuffle4[3])
r16.place(x=20, y=760)


def show_msg():
    score = 0
    if(v0.get()==0):
        score+=1
    if(v1.get()==4):
        score+=1
    if(v2.get()==8):
        score+=1
    if(v3.get()==12):
        score+=1

    if(score==4):
        messagebox.showinfo("score","all done!")
    elif(score==3):
        messagebox.showinfo("score","3 correct!")
    elif(score==2):
        messagebox.showinfo("score","2 correct!")
    elif(score==1):
        messagebox.showinfo("score","1 correct!")
    elif(score==0):
        messagebox.showinfo("score","all wrong!")
    

btn = Button(window, text= "Click Here", command=show_msg)
btn.place(x=200, y=800)
# btn=Button(window, text="submit", fg='blue')


window.title('quiz')
window.geometry("400x855+10+10")
window.mainloop()

