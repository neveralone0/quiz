from asyncore import write
from operator import le
from random import randint, random, shuffle
from textwrap import fill
from tkinter import font, scrolledtext
import random
from unicodedata import name
from attr import has
from tkinter import *
from tkinter import messagebox


lines = []
randoms = []
answer_code = []
questions = []
emails = []
passwords = []
temp_mail = str()
name_exist = False


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


window=Tk()

main = Frame(window)
sign_in = Frame(window)
sign_up = Frame(window)
quiz = Frame(window)


def change_to_main():
    main.pack(fill='both', expand=1)

change_to_main()

def change_to_signin():
    sign_in.pack(fill='both', expand=1)
    sign_up.pack_forget()
    quiz.pack_forget()
    main.place_forget()


def change_to_signup():
    sign_up.pack(fill='both', expand=1)
    sign_in.pack_forget()
    quiz.pack_forget()
    main.place_forget()


def change_to_quiz():
    quiz.pack(fill='both', expand=1)
    sign_in.pack_forget()
    sign_up.pack_forget()
    main.pack_forget()


def logging_in():
    global username
    username = input_name_signin.get()

    mail = open("/home/ali/Desktop/python_projects/quiz/accounts.txt", "r")
    temp_mail = mail.readlines()[0::3]
    mail.close()

    for i in range(len(temp_mail)):
        temp_mail[i] = temp_mail[i][0: len(temp_mail[i]) - 1]

    for i in range(len(temp_mail)):
        if username == temp_mail[i]:
            print('email ok!')
            pass_check = open("/home/ali/Desktop/python_projects/quiz/accounts.txt", "r")
            pass_temp = str(pass_check.readlines()[i * 3 + 1:i * 3 + 2:])
            print(pass_temp)
            pass_temp = pass_temp[2:len(pass_temp) - 4]
            print(pass_temp)
            if (pass_temp == input_pass_signin.get()):
                print('logged in!')
                change_to_quiz()
                break
            else:
                messagebox.showinfo("info", "wrong password!")
                break
    else:
        messagebox.showinfo("info", "user not found!")


def siggning_up():
    em_temp = input_email.get()
    em_temp = em_temp[len(em_temp) - 10:len(em_temp)]
    check_email = em_temp == '@gmail.com'

    pass_temp = len(input_pass.get())

    pass_temp_alpha = input_pass.get().isalpha()
    pass_temp_digit = input_pass.get().isdigit()
    pass_check_len = (pass_temp >= 8)
    pass_lower = input_pass.get().islower()
    pass_upper = input_pass.get().isupper()
    pass_ascci = input_pass.get().isascii()

    user_temp = input_name.get()
    user_temp = user_temp[0:1]
    user_first_num = str(user_temp).isdigit()
    user_check_num = input_name.get().isdigit()
    user_ascii = input_name.get().isascii()

    name_symbol = input_name.get()
    chars = ['@', '/', '"', "'", '=', '_', '+']
    has_all = any([char in name_symbol for char in chars])

    user_all_upper = input_name.get().isupper()
    user_all_lower = input_name.get().isupper()

    if check_email:
        if not pass_temp_alpha:
            if not pass_temp_digit:
                if pass_check_len:
                    if not pass_lower:
                        if not pass_upper:
                            if pass_ascci:
                                if not user_first_num:
                                    if not user_check_num:
                                        if not user_check_num:
                                            if user_ascii:
                                                if not has_all:
                                                    if not user_all_upper:
                                                        if not user_all_lower:

                                                            mail = open(
                                                                "/home/ali/Desktop/python_projects/quiz/accounts.txt",
                                                                "r")
                                                            temp_mail = mail.readlines()[0::3]
                                                            mail.close()

                                                            for i in range(len(temp_mail)):
                                                                temp_mail[i] = temp_mail[i][0: len(temp_mail[i]) - 1]

                                                            for i in range(len(temp_mail)):
                                                                if (input_name.get() == temp_mail[i]):
                                                                    name_exist = True
                                                                    break
                                                            else:
                                                                name_exist = False

                                                            if (not name_exist):
                                                                file = open(
                                                                    "/home/ali/Desktop/python_projects/quiz/accounts.txt",
                                                                    "a")
                                                                file.write(input_name.get() + "\n")
                                                                file.write(input_pass.get() + "\n")
                                                                file.write(input_email.get() + "\n")
                                                                file.close()
                                                                print('all done')
                                                                change_to_signin()

                                                        else:
                                                            messagebox.showinfo("info", "user is all lowercase")
                                                    else:
                                                        messagebox.showinfo("info", "user is all uppercase")
                                                else:
                                                    messagebox.showinfo("info", "you cant use @#$+=_/")
                                            else:
                                                messagebox.showinfo("info", "user has none english character")
                                        else:
                                            messagebox.showinfo("info", "user cant be all num")
                                    else:
                                        messagebox.showinfo("info", "user cant be all nummber")
                                else:
                                    messagebox.showinfo("info", "user first character cant be nummber")
                            else:
                                messagebox.showinfo("info", "password has none english")
                        else:
                            messagebox.showinfo("info", "password is all upper")
                    else:
                        messagebox.showinfo("info", "password is all lower")
                else:
                    messagebox.showinfo("info", "password has less than 8 char")
            else:
                messagebox.showinfo("info", "password has no alpha")
        else:
            messagebox.showinfo("info", "password has no digit")
    else:
        messagebox.showinfo("info", "invalid email!")


def show_msg():
    global score
    score = 0

    if (v0.get() == 0):
        score += 1
    if (v1.get() == 4):
        score += 1
    if (v2.get() == 8):
        score += 1
    if (v3.get() == 12):
        score += 1

    if (score == 4):
        write_scores()
        messagebox.showinfo("score", "all done!")
    elif (score == 3):
        write_scores()
        messagebox.showinfo("score", "3 correct!")
    elif (score == 2):
        write_scores()
        messagebox.showinfo("score", "2 correct!")
    elif (score == 1):
        write_scores()
        messagebox.showinfo("score", "1 correct!")
    elif (score == 0):
        write_scores()
        messagebox.showinfo("score", "all wrong!")


def write_scores():
    file = open("/home/ali/Desktop/python_projects/quiz/score.txt", "a")
    file.write(username + "\n")
    file.write(str(score) + "\n")
    file.close()
    print('write done')


# quiz ui

lbl=Label(quiz, text="wellcome to quiz", fg='red', font=("Helvetica", 16))
lbl.place(x=120, y=10)


q1=Label(quiz, text=lines[0], fg='blue', font=("Helvetica", 16))
q1.place(x=120, y=60)


v0=IntVar()
v0.set(0)
shuffle1 = random.sample(range(0, 4), 4)
r1=Radiobutton(quiz, text=questions[shuffle1[0]], variable=v0,value=shuffle1[0])
r1.place(x=20,y=90)
r2=Radiobutton(quiz, text=questions[shuffle1[1]], variable=v0,value=shuffle1[1])
r2.place(x=20, y=120)
r3=Radiobutton(quiz, text=questions[shuffle1[2]], variable=v0,value=shuffle1[2])
r3.place(x=20,y=150)
r4=Radiobutton(quiz, text=questions[shuffle1[3]], variable=v0,value=shuffle1[3])
r4.place(x=20, y=180)


q2=Label(quiz, text=lines[1], fg='red', font=("Helvetica", 16))
q2.place(x=120, y=260)
v1=IntVar()
v1.set(1)
shuffle2 = random.sample(range(4, 8), 4)
r5=Radiobutton(quiz, text=questions[shuffle2[0]], variable=v1,value=shuffle2[0])
r5.place(x=20,y=290)
r6=Radiobutton(quiz, text=questions[shuffle2[1]], variable=v1,value=shuffle2[1])
r6.place(x=20, y=320)
r7=Radiobutton(quiz, text=questions[shuffle2[2]], variable=v1,value=shuffle2[2])
r7.place(x=20,y=350)
r8=Radiobutton(quiz, text=questions[shuffle2[3]], variable=v1,value=shuffle2[3])
r8.place(x=20, y=380)



q3=Label(quiz, text=lines[2], fg='red', font=("Helvetica", 16))
q3.place(x=120, y=460)
v2=IntVar()
v2.set(1)
shuffle3 = random.sample(range(8, 12), 4)
r9=Radiobutton(quiz, text=questions[shuffle3[0]], variable=v2,value=shuffle3[0])
r9.place(x=20,y=490)
r10=Radiobutton(quiz, text=questions[shuffle3[1]], variable=v2,value=shuffle3[1])
r10.place(x=20, y=520)
r11=Radiobutton(quiz, text=questions[shuffle3[2]], variable=v2,value=shuffle3[2])
r11.place(x=20,y=550)
r12=Radiobutton(quiz, text=questions[shuffle3[3]], variable=v2,value=shuffle3[3])
r12.place(x=20, y=580)



q4=Label(quiz, text=lines[3], fg='red', font=("Helvetica", 16))
q4.place(x=120, y=640)
v3=IntVar()
v3.set(1)
shuffle4 = random.sample(range(12, 16), 4)
r13=Radiobutton(quiz, text=questions[shuffle4[0]], variable=v3,value=shuffle4[0])
r13.place(x=20,y=670)
r14=Radiobutton(quiz, text=questions[shuffle4[1]], variable=v3,value=shuffle4[1])
r14.place(x=20, y=700)
r15=Radiobutton(quiz, text=questions[shuffle4[2]], variable=v3,value=shuffle4[2])
r15.place(x=20,y=730)
r16=Radiobutton(quiz, text=questions[shuffle4[3]], variable=v3,value=shuffle4[3])
r16.place(x=20, y=760)

# manu ui
sign_up_label=Label(sign_up, text="sign up panel", fg='red', font=("Helvetica", 16))
sign_up_label.place(x=120, y=0)

sign_in_label=Label(sign_in, text="sign in panel", fg='red', font=("Helvetica", 16))
sign_in_label.place(x=120, y=0)


username_label = Label(sign_in, text="username", fg='black', font=("Helvetica", 16))
username_label.place(x=50, y=40)

password_label = Label(sign_in, text="password", fg='black', font=("Helvetica", 16))
password_label.place(x=50, y=80)

input_name_signin = Entry(sign_in, bd=5)
input_name_signin.place(x=160, y=40)

input_pass_signin = Entry(sign_in, bd=5)
input_pass_signin.place(x=160, y=80)

username_label = Label(sign_up, text="username", fg='black', font=("Helvetica", 16))
username_label.place(x=50, y=40)
input_name = Entry(sign_up, bd=5)
input_name.place(x=160, y=40)

password_label = Label(sign_up, text="password", fg='black', font=("Helvetica", 16))
password_label.place(x=50, y=80)
input_pass = Entry(sign_up, bd=5)
input_pass.place(x=160, y=80)

# input ui

email_label = Label(sign_up, text="email", fg='black', font=("Helvetica", 16))
email_label.place(x=50, y=120)
input_email = Entry(sign_up, bd=5)
input_email.place(x=160, y=120)

submit_btn = Button(sign_up, text= "submit", command=siggning_up)
submit_btn.place(x=180, y=165)

submit_btn = Button(sign_in, text= "login", command=logging_in)
submit_btn.place(x=180, y=140)


# buttons ui

btn = Button(quiz, text= "end up", command=show_msg)
btn.place(x=200, y=800)

signin_btn = Button(main, text= "sign in", command=change_to_signin)
signin_btn.place(x=80, y=370)

signup_btn = Button(main, text= "sign up", command=change_to_signup)
signup_btn.place(x=180, y=370)


window.title('quiz')
window.geometry("400x855+10+10")
window.mainloop()