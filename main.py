import random
from tkinter import *
from tkinter import messagebox
import webbrowser
# ---------------------------- Link opener ------------------------------- #

def open_link():
    webbrowser.open(f'{website_entry}')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    nr_letters = 5
    nr_symbols = 4
    nr_numbers = 3

    '''
    nr_letters= int(input("How many letters would you like in your password? \n"))
    nr_symbols = int(input(f"How many symbols would you like? \n"))
    nr_numbers = int(input(f"How many numbers would you like? \n"))
    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    '''
    password_list=[]
    for char in range(1, nr_letters+1):
        random_char = random.choice(letters)
        password_list += random_char
    for char in range(1, nr_symbols+1):
        password_list += random.choice(symbols)
    for char in range(1, nr_numbers+1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list) #joins the letters of the list without seperation and converts into a string
    password_entry.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "wait ", message = "Looks empty, u sure ??")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details shared: \nEmail: {email}"
                                                              f"\nPassword: {password} \n Is it ok to save ?")



    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} || {email} || {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column =1)

#Labels
website_label = Label(text = "Website: ")
website_label.grid(row=1)
email_label = Label(text = "Email/Username: ")
email_label.grid(row=2)
password_label = Label(text = "Password: ")
password_label.grid(row=3)

#Entries
website_entry = Entry(width=28)
website_entry.grid(row=1, column =1, columnspan = 2)
website_entry.focus()
email_entry = Entry(width = 28)
email_entry.insert(0, "soumyo.ghosh24102003@gmail.com") #0 for populating the start, END for populating the end
email_entry.grid(row = 2, column =1, columnspan = 2)
password_entry = Entry(width = 21)

password_entry.grid(row = 3, column =1)


#buttons
generate_password_button = Button(text = "Generate Password", command= generate_password)
generate_password_button.grid(column =2, row =3)
add_button = Button(text = "add", width = 36, command= save)
add_button.grid(row =4, column = 1, columnspan=2)
go_to_link = Button(text = "Go to link", command=open_link)
go_to_link.grid(row=1, column = 2)







window.mainloop()