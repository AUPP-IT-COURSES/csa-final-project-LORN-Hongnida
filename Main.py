from tkinter import *
from tkinter import ttk
from convert_data import convert_tuples_to_dicts, find, convert_Atuples_to_dicts
import mysql.connector
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from io import BytesIO
from tkinter.ttk import Treeview, Style
# from click import style

conn = mysql.connector.connect(host='localhost', username='root', password='Nida85203014', database='ehms(python)')
my_cursor = conn.cursor()

my_cursor.execute("SELECT * FROM admin")
a_data = my_cursor.fetchall()

my_cursor.execute("SELECT * FROM patients")
p_data = my_cursor.fetchall()

my_cursor.execute("SELECT * FROM doctors")
d_data = my_cursor.fetchall()

A_Data = convert_Atuples_to_dicts(a_data)
P_Data = convert_tuples_to_dicts(p_data)
D_Data = convert_tuples_to_dicts(d_data)


window = Tk()
window.geometry('800x600')
window.title("E-Healthcare Management System")
# window.configure(bg="black")

header_color = '#278b7a'
bg_color = '#e2f7f3'

login_admin_icon = PhotoImage(file='WS_Admin-01.png')
login1_admin_icon = PhotoImage(file='admin-01.png')
login_doctor_icon = PhotoImage(file="WS_Doctor-01.png")
login1_doctor_icon = PhotoImage(file="Doctor-01.png")
login_patient_icon = PhotoImage(file="WS_Patient-01.png")
login1_patient_icon = PhotoImage(file="Patient-01.png")
locked_icon = PhotoImage(file="locked.png")
unlock_icon = PhotoImage(file="unlocked.png")


    
def welcomePage():

    def login(button_text):
        welcome_page_fm.destroy()
        # window.update()
        LogIn(button_text)
    def signup_page():
        welcome_page_fm.destroy()
        SignUp()
    # def Doctor_page():
    #     welcome_page_fm.destroy()
    #     # window.update()
    #     adminLogin()
    # def Patient_page():
    #     welcome_page_fm.destroy()
    #     # window.update()
    #     adminLogin()
    
    welcome_page_fm = Frame(window, highlightbackground=header_color, 
                                highlightthickness=3, bg=bg_color)

    heading_lb = Label(welcome_page_fm, text="Welcome to\nE-Healthcare Management System", 
                        bg=header_color, fg="white", font=("Bold", 18))
    heading_lb.place(x=0, y=0, width=700)

    login_btn = Button(welcome_page_fm, text="Admin Login", bg=header_color, fg='white', bd=0, font=15, command=lambda:login("admin"))
    login_btn.place(x=250, y=140, width=300)
    doctor_login_btn = Button(welcome_page_fm, text="Doctor Login", bg=header_color, fg='white', bd=0, font=15, command=lambda: login("doctor"))
    doctor_login_btn.place(x=250, y=240, width=300)
    patient_login_btn = Button(welcome_page_fm, text="Patient Login", bg=header_color, fg='white', bd=0, font=15, command=lambda: login("patient"))
    patient_login_btn.place(x=250, y=340, width=300)

    login_img = Button(welcome_page_fm, image=login_admin_icon, bd=0)
    login_img.place(x=150, y=100)
    doctor_login_img = Button(welcome_page_fm, image=login_doctor_icon, bd=0)
    doctor_login_img.place(x=150, y=200)
    patient_login_img = Button(welcome_page_fm, image=login_patient_icon, bd=0)
    patient_login_img.place(x=150, y=300)

    signup_lb = Label(welcome_page_fm, text="Don't have an acc? ", bg=bg_color,fg=header_color, bd=0, font=12)
    signup_lb.place(x=460, y=450)

    signup_btn = Button(welcome_page_fm, text="Sign up!", bg=header_color,fg=bg_color, bd=0, font=12, command=signup_page)
    signup_btn.place(x=600, y=445)

    welcome_page_fm.pack(pady=30)
        # welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=700, height=500)

def LogIn(button_text):
    def welcome_page():
        login_fm.destroy()
        welcomePage()
    def remove_highlight_warning(entry):
        if entry['highlightbackground'] != header_color:
            if entry.get() != '':
                entry.config(highlightbackground=header_color)
    def check_validation(button_text):
        username = username_en.get()
        email = email_en.get()
        pw = password_en.get()
        
        if username == '':
            message_box("⚠️ Username is required!")
            username_en.config(highlightbackground="red")
        elif email == '':
            message_box("⚠️ Email is required!")
            email_en.config(highlightbackground="red")
        elif pw == '':
            message_box("⚠️ Password is required!")
            password_en.config(highlightbackground="red")
        else:
            if button_text == "admin":
                found = find(A_Data, username, email, pw)
                ID = len(A_Data)
            elif button_text == "doctor":
                found = find(D_Data, username, email, pw)
                ID = len(D_Data)
            elif button_text == "patient":
                found = find(P_Data, username, email, pw)
                print(P_Data['Email'])
                ID = len(P_Data) 
        
            if found == "email":
                message_box(f"⚠️ This email doesn't belong to any {found} account.")
                email_en.config(highlightbackground="red")
            elif found == "username":
                message_box(f"⚠️ Incorrect username or password.")
                username_en.config(highlightbackground="red")
                password_en.config(highlightbackground="red")
            else:
                login_fm.destroy()
                dashboard(button_text, ID)
            
    
    login_fm = Frame(window, highlightbackground=header_color, 
                                    highlightthickness=3, bg=bg_color)

    heading_lb = Label(login_fm, text="Admin Portal", 
                            bg=header_color, fg="white", font=("Bold", 18))
    heading_lb.place(x=0, y=0, width=700, height=50)

    return_btn = Button(login_fm, text="←", bg=bg_color, fg=header_color, bd=0, font=("Bold", 20), command=welcome_page)
    return_btn.place(x=20, y=55)
    
    login_img = Label(login_fm, image=login1_admin_icon, bd=0)
    login_img.place(x=95, y=100)


    login_btn = Button(login_fm, text="Login", bg=header_color, fg='white', bd=0, font=("Bold", 15), command=lambda:check_validation(button_text))
    login_btn.place(x=60, y=270, width=210)
    forget_pw_btn = Button(login_fm, text="⚠️\nForget Password", bg=bg_color,fg=header_color, bd=0, font=12)
    forget_pw_btn.place(x=60, y=320, width=210)

    username_lb = Label(login_fm, text="Username", bg=bg_color,fg=header_color, font=("Bold", 18))
    username_lb.place(x=420, y=100)
    username_en = Entry(login_fm, highlightbackground=header_color, 
                                    highlightthickness=1)
    username_en.place(x=350, y=150, width=250, height=30)
    username_en.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=username_en))

    email_lb = Label(login_fm, text="Email", bg=bg_color,fg=header_color, font=("Bold", 18))
    email_lb.place(x=445, y=200)
    email_en = Entry(login_fm, highlightbackground=header_color, 
                                    highlightthickness=1)
    email_en.place(x=350, y=250, width=250, height=30)
    email_en.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=email_en))


    password_lb = Label(login_fm, text="Password", bg=bg_color,fg=header_color, font=("Bold", 18))
    password_lb.place(x=420, y=300)
    password_en = Entry(login_fm, highlightbackground=header_color, 
                                    highlightthickness=1, show="*")
    password_en.place(x=350, y=350, width=250, height=30)
    password_en.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=password_en))


    def show_hide():
        if password_en["show"] == "*":
            password_en.config(show='')
            show_hide_btn.config(image=unlock_icon)
        else:
            password_en.config(show='*')
            show_hide_btn.config(image=locked_icon)

    show_hide_btn = Button(login_fm, image=locked_icon, bd=0, command=show_hide)
    show_hide_btn.place(x=610, y=340)


    login_fm.pack(pady=30)
    # welcome_page_fm.pack_propagate(False)
    login_fm.configure(width=700, height=500)

    if button_text == "admin":
        heading_lb.config(text="Admin Portal")
        login_img.config(image=login1_admin_icon)
    elif button_text == "doctor":
        heading_lb.config(text="Doctor Portal")
        login_img.config(image=login1_doctor_icon)
    elif button_text == "patient":
        heading_lb.config(text="Patient Portal")
        login_img.config(image=login1_patient_icon)

    

def message_box(message):
        message_box_fm = Frame(window, highlightbackground="red", highlightthickness=2, bg=bg_color)
        message_heading_lb = Label(message_box_fm, text="Login Failed!", 
                            bg='red', fg="white", font=("Bold", 15))
        message_heading_lb.place(x=0, y=0, width=400, height=25)

        close_btn = Button(message_box_fm, text="×", bd=0, font=("Bold", 16), bg=bg_color, fg=header_color, command=lambda: message_box_fm.destroy())
        close_btn.place(x=370, y = 0, height=25)

        message_lb = Label(message_box_fm, text=message, font=15, bg=bg_color)
        message_lb.pack(pady=80)

        message_box_fm.place(x = 200, y=200, width=400, height=200)
def SignUp():
    pic_path = StringVar()
    pic_path.set('')
    
    def check_validation():
        username = patient_name_en.get()
        email = patient_email_en.get()
        pw = password_en.get()
        re_pw = confirm_password_en.get()
        Id = len(D_Data)+1
        if username == '':
            message_box("⚠️ Username is required!")
            patient_name_en.config(highlightbackground="red")
        elif email == '':
            message_box("⚠️ Email is required!")
            patient_email_en.config(highlightbackground="red")
        elif pw == '':
            message_box("⚠️ Password is required!")
            password_en.config(highlightbackground="red")
        elif re_pw == '':
            message_box("⚠️ Confirm Your Password!")
            password_en.config(highlightbackground="red")
        elif pw != re_pw:
            message_box("⚠️ Password doesn't match!")
            password_en.config(highlightbackground="red")            
        else:
            add_d = ("INSERT INTO `ehms(python)`.`patients` (`ID`, `Username`, `Gender`, `Email`, `Password`,`Age`, `Department`, `Phone_Number` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
            val = (Id, username, '0', email, pw,'0', '0', '0') 
            my_cursor.execute(add_d, val)
            conn.commit()
            succeed_lb = Label(signup_fm, text="Sign Up Successful!. Login to use.", bg=bg_color,fg=header_color, font=("Bold", 10))
            succeed_lb.place(x=460, y=450)
    def open_pic():
        path = askopenfilename()

        if path:
            img = ImageTk.PhotoImage(Image.open(path).resize((120, 120)))
            pic_path.set(path)

            pfp_btn.config(image=img)
            pfp_btn.image = img
    def welcome_page():
        signup_fm.destroy()
        welcomePage()
        
    signup_fm = Frame(window, highlightbackground=header_color, 
                                        highlightthickness=3, bg=bg_color)

    signup_heading_lb = Label(signup_fm, text="Create A New Patient Account", 
                                bg=header_color, fg="white", font=("Bold", 18))
    signup_heading_lb.place(x=0, y=0, width=700, height=50)

    pfp_fm = Frame(signup_fm, highlightbackground=header_color, highlightthickness=3)
    pfp_fm.place(x=12.5, y=12.5, width=120, height=120)

    pfp_btn = Label(signup_fm, image=login_patient_icon, bd=0)
    pfp_btn.place(x=16, y=16, width=115, height=115)

    signup_lb = Label(signup_fm, text="Fill in the information in the form below", font=15, bg=bg_color, fg=header_color)
    signup_lb.place(x=200, y=80)

    patient_name_lb = Label(signup_fm, text="Your Full Name:", font=("bold", 15), bg=bg_color, fg=header_color)
    patient_name_lb.place(x=100, y=170)
    patient_name_en = Entry(signup_fm, highlightbackground=header_color, 
                                        highlightthickness=1)
    patient_name_en.place(x=350, y=170, width=250, height=30)

    patient_email_lb = Label(signup_fm, text="Your Email Address:", font=("bold", 15), bg=bg_color, fg=header_color)
    patient_email_lb.place(x=100, y=220)
    patient_email_en = Entry(signup_fm, highlightbackground=header_color, 
                                        highlightthickness=1)
    patient_email_en.place(x=350, y=220, width=250, height=30)

    password_lb = Label(signup_fm, text="New Password:", bg=bg_color,fg=header_color, font=("Bold", 15))
    password_lb.place(x=100, y=270)
    password_en = Entry(signup_fm, highlightbackground=header_color, 
                                        highlightthickness=1, show="*")
    password_en.place(x=350, y=270, width=250, height=30)

    def show_hide():
        if password_en["show"] == "*":
            password_en.config(show='')
            show_hide_btn.config(image=unlock_icon)
            
        else:
            password_en.config(show='*')
            show_hide.config(image=locked_icon)
    def re_show_hide():
        if confirm_password_en["show"] == "*":
            confirm_password_en.config(show='')
            re_show_hide_btn.config(image=unlock_icon)
        else:
            confirm_password_en.config(show='*')
            re_show_hide_btn.config(image=locked_icon)
    show_hide_btn = Button(signup_fm, image=locked_icon, bd=0, command=re_show_hide)
    show_hide_btn.place(x=610, y=310)

    re_show_hide_btn = Button(signup_fm, image=locked_icon, bd=0, command=show_hide)
    re_show_hide_btn.place(x=610, y=260)

    confirm_password_lb = Label(signup_fm, text="Confirm Password:", bg=bg_color,fg=header_color, font=("Bold", 15))
    confirm_password_lb.place(x=100, y=320)
    confirm_password_en = Entry(signup_fm, highlightbackground=header_color, 
                                        highlightthickness=1, show="*")
    confirm_password_en.place(x=350, y=320, width=250, height=30)
    
    signup_fm.pack(pady=30)
            # welcome_page_fm.pack_propagate(False)
    signup_fm.configure(width=700, height=500)
    # def add_acc(ID, username, gender, email, password, age, department, phone_number, pic_data):
    #     add_d = (f"INSERT INTO `ehms(python)`.`doctors` VALUES ('{ID}', '{username}', '{gender}', '{email}', '{password}', '{age}', '{department}', '{phone_number}', ?);", [pic_data])
    #     # val = (ID, username, email, password, 0, 0)
    #     my_cursor.execute(add_d)
    #     conn.commit()
    


    signup_btn = Button(signup_fm, text="Sign Up", bg=header_color,fg=bg_color, bd=0, font=12, command=lambda: check_validation())
    signup_btn.place(x=300, y=390, width=100, height=40)

    close_btn = Button(signup_fm, text="×", bd=0, font=("Bold", 20), bg=bg_color, fg=header_color, command=welcome_page)
    close_btn.place(x=644, y = 0, width=50, height=50)


def dashboard(button_text, ID):
    dashboard_fm = Frame(window, highlightbackground=header_color, 
                                                highlightthickness=3, bg=bg_color)
    nav_fm = Frame(dashboard_fm,highlightthickness=0, bg="#baece2")
    nav_fm.place(x=0, y=0, width=120, height=494)
    pages_fm = Frame(dashboard_fm,highlightthickness=0, bg=bg_color)
    pages_fm.place(x=120, y=0, width=574, height=494)

    
    
    
    view_data_fm = Frame(pages_fm,highlightthickness=0, bg=bg_color)
    view_data_fm.place(x=120, y=0, width=574, height=494)
    
    def displaytable(button_text):
        def go_to_home():    
            view_data_fm.destroy()
            home_page()
        if button_text == "VD":
            heading_lb = Label(view_data_fm, text="All Doctors Account", justify=CENTER, font=("Bold", 20), bg=bg_color, fg=header_color)
            heading_lb.place(y=100)
        elif button_text == "VP":
            heading_lb = Label(view_data_fm, text="All Patients Account", justify=CENTER, font=("Bold", 20), bg=bg_color, fg=header_color)
            heading_lb.place(y=100)

        tree = Treeview(pages_fm)
        tree['show'] = 'headings'

        s = ttk.Style(pages_fm)
        s.theme_use("clam")

        # s.configure(".", fonts=('Helvetica, 15'))
        # s.configure(tree.heading, foreground='blue', blackground="red", font=("Helvetica", 15, "Bold"))

        tree["columns"] = ["ID", "Username", "Gender", "Email", 'Password', 'Department']

        tree.column ("ID", width=50, minwidth=50, anchor=CENTER)
        tree.column ("Username", width=100, minwidth=100, anchor=CENTER)
        tree.column ("Gender", width=50, minwidth=100, anchor=CENTER)
        tree.column ("Email", width=150, minwidth=150, anchor=CENTER)
        tree.column ("Password", width=80, minwidth=80, anchor=CENTER)
        tree.column ("Department", width=100, minwidth=100, anchor=CENTER)

        tree.heading("ID", text="ID", anchor=CENTER)
        tree.heading("Username", text="Username", anchor=CENTER)
        tree.heading("Gender", text="Gender", anchor=CENTER)
        tree.heading("Email", text="Email", anchor=CENTER)
        tree.heading("Password", text="Password", anchor=CENTER)
        tree.heading("Department", text="Department", anchor=CENTER)
        i = 0

        if button_text == "VD":
            for ro in d_data:
                tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
            tree.place(x=40, y=200, width=500) 
        elif button_text == "VP":
            for ro in p_data:
                tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
            tree.place(x=40, y=200, width=500) 


        hsb = Scrollbar(pages_fm, orient="horizontal")

        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.place(x=40, y=420, width=500)

       
    def home_page():
        home_fm = Frame(pages_fm,highlightthickness=0, bg=bg_color)
        home_fm.place(x=120, y=0, width=574, height=494)

        home_img = Label(home_fm, image=login_admin_icon, bd=0)
        home_img.place(x=50, y=50)
        
        if button_text == "admin":
            home_img.config(image=login_admin_icon)
            name = {A_Data[ID-1]['Username']}
            for x in name:
                username = x
            name_lb = Label(home_fm, text=username, bd=0, font=("Bold", 23), bg=bg_color, fg=header_color)
            name_lb.place(x=400, y=150)
        elif button_text == "doctor":
            home_img.config(image=login_doctor_icon)
            name = {D_Data[ID-1]['Username']}
            for x in name:
                username = x
            name_lb = Label(home_fm, text=username, bd=0, font=("Bold", 23), bg=bg_color, fg=header_color)
            name_lb.place(x=400, y=150)
        elif button_text == "patient":
            home_img.config(image=login_patient_icon)
            name = {P_Data[ID-1]['Username']}
            for x in name:
                username = x
            name_lb = Label(home_fm, text=username, bd=0, font=("Bold", 23), bg=bg_color, fg=header_color)
            name_lb.place(x=100, y=150)

        elif button_text == "VD" or button_text == "VP":
            home_fm.destroy()
            displaytable()
        else:
            home_page()
        home_fm.pack(pady=30)
        # welcome_page_fm.pack_propagate(False)
        home_fm.configure(width=700, height=500)  


        
    dashboard_fm.pack(pady=30)
    # welcome_page_fm.pack_propagate(False)
    dashboard_fm.configure(width=700, height=500)  

    # view_doctor_fm = Frame(dashboard_fm, ) 

    home_btn = Button(nav_fm, text="Home", font=10, justify=CENTER, bg="#baece2", bd=0, command=home_page)
    home_btn.pack(pady=25)
    
    VD_btn = Button(nav_fm, text="View Doctors", font=10, justify=CENTER, bg="#baece2", bd=0, command=lambda:displaytable('VD'))
    VD_btn.pack(pady=25)

    VP_btn = Button(nav_fm, text="View Patients", font=10, justify=CENTER, bg="#baece2", bd=0, command=lambda:displaytable('VP'))
    VP_btn.pack(pady=25)

    RD_btn = Button(nav_fm, text="Remove Doctor", font=10, justify=CENTER, bg="#baece2", bd=0)
    RD_btn.pack(pady=25)

    RP_btn = Button(nav_fm, text="Remove Patient", font=10, justify=CENTER, bg="#baece2", bd=0)
    RP_btn.pack(pady=25)

    view_data_fm.pack(pady=30)
    # welcome_page_fm.pack_propagate(False)
    view_data_fm.configure(width=700, height=500)  

        
    
welcomePage()
window.mainloop()



