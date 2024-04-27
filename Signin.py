from tkinter import *
from tkinter import messagebox
import ast


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

##    print(r.keys())
##    print(r.values())
##login user succesfully
    if username in r.keys() and password==r[username]:
        inter=Toplevel(root)
        inter.title('Mail')
        inter.geometry('925x500+300+200')
        inter.configure(bg="#fff")
        inter.resizable(False, False)

        pic = PhotoImage(file='bgimg.png')
        Label(inter, image=pic, border=0, bg='white').place(x=0, y=0)

        frame = Frame(inter, width=700, height=350, bg='white')
        frame.place(x=105, y=80)

        heading = Label(frame, text='Send Your Mail', fg='#57a1f8', bg='white',
                        font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=230, y=0)

        # Email address input
        email = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        email.place(x=50, y=50)
        email.insert(0, 'Enter Mail Address')
        Frame(frame, width=250, height=2, bg='black').place(x=50, y=70)

        # Subject input
        subject = Entry(frame, width=60, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        subject.place(x=50, y=80)
        subject.insert(0, 'Enter Subject')
        Frame(frame, width=475, height=2, bg='black').place(x=50, y=100)

        # Body input
        body = Text(frame, width=60, height=10, fg='black', border=1, bg='white', font=('Microsoft Yahei UI Light', 11))
        body.place(x=50, y=110)
        body.insert('1.0', 'Enter Body')

        def send_mail():
            # You can put your mail sending logic here
            messagebox.showinfo("Send Mail", "Sent")

        def sent_mail():
            messagebox.showinfo("Sent Mail", "View")

        def received_mail():
            messagebox.showinfo("Received Mail", "Received")

        # Send button
        send_button = Button(frame, text="Send Mail", command=send_mail, fg='white', bg='#57a1f8',
                             font=('Microsoft Yahei UI Light', 11))
        send_button.place(x=600, y=300)

        sent_button = Button(frame, text="Sent Mail", command=sent_mail, fg='white', bg='#57a1f8',
                             font=('Microsoft Yahei UI Light', 11))
        sent_button.place(x=600, y=30)

        sent_button = Button(frame, text="Received Mail", command=received_mail, fg='white', bg='#57a1f8',
                             font=('Microsoft Yahei UI Light', 11))
        sent_button.place(x=570, y=70)

        inter.mainloop()


##login failed
    else:
        messagebox.showerror('Invalid', 'invalid username or password')

#############################################################################

def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()

        if password==confirm_password:
            try:
                file=open('datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt', 'w')
                w=file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully sign up')

            except:
                file=open('datasheet.txt', 'w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both password should match")


    def sign():
        window.destroy()


    img = PhotoImage(file='signup.png')
    Label(window, image=img, border=0, bg='white').place(x=0, y=0)

    frame=Frame(window, width=350, height=390, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=115, y=5)

    ##fill username
    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0, 'Username')
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)



    #fill password
    def on_enter(e):
        code.delete(0, 'end')
        code.config(show='*')
    def on_leave(e):
        if code.get()=='':
            code.insert(0, 'Password')
    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)



    ##confirm password
    def on_enter(e):
        confirm_code.delete(0, 'end')
        confirm_code.config(show='*')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0, 'Confirm Your Password')
    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Your Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text='Already have an account?', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
    label.place(x=80, y=340)

    signin = Button(frame, width=6, text='sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=225, y=340)


    window.mainloop()

#############################################################################

bg_image = PhotoImage(file='login.png')
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0)

frame = Frame(root, width=350, height=350, bg='#fff')
frame.place(x=480, y=70)
heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft  YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=10)


##Login
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


##Password
def on_enter(e):
    code.delete(0, 'end')
    code.config(show='*')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=115, y=270)


#signup
sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=235, y=270)




root.mainloop()