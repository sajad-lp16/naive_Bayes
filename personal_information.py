# Author : Negin pazoki jeyhoun abadi
# Student Number : 985223021


from tkinter import *

CONTACTS = {}

window = Tk()
window.geometry("600x550")
window.resizable(width=FALSE, height=FALSE)
window.title('Negin pazoki jeyhoun abadi')
selected = ''


def clear():
    lst_1.delete(0, END)


def iterate_list(data):
    for item in data:
        lst_1.insert(END, item)


def view_data():
    clear()
    global CONTACTS
    users = [tuple(i.values()) for i in CONTACTS.values()]
    iterate_list(users)


def search_user():
    clear()
    global CONTACTS
    users = [tuple(i.values()) for i in CONTACTS.values()]
    match = []
    data = [entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(),
            entry_5.get(), entry_6.get(), entry_7.get()]
    for user in users:
        if user[0] == data[0] or user[1] == data[1] or user[2] == data[2] or \
                user[3] == data[3] or user[4] == data[4] or user[5] == data[5] \
                or user[6] == data[6]:
            match.append(user)

    iterate_list(match)


def register():
    global CONTACTS
    CONTACTS[entry_6.get()] = {
        'name': entry_1.get(),
        'last_name': entry_2.get(),
        'code': entry_3.get(),
        'email': entry_4.get(),
        'address': entry_5.get(),
        'phone_number': entry_6.get(),
        'home_phone': entry_7.get(),
    }
    view_data()


def get_selected_row(event):
    global selected
    if len(lst_1.curselection()) > 0:
        index = lst_1.curselection()[0]
        selected = lst_1.get(index)

        entry_1.delete(0, END)
        entry_1.insert(END, selected[0])

        entry_2.delete(0, END)
        entry_2.insert(END, selected[1])

        entry_3.delete(0, END)
        entry_3.insert(END, selected[2])

        entry_4.delete(0, END)
        entry_4.insert(END, selected[3])

        entry_5.delete(0, END)
        entry_5.insert(END, selected[4])

        entry_6.delete(0, END)
        entry_6.insert(END, selected[5])

        entry_7.delete(0, END)
        entry_7.insert(END, selected[6])


def delete_user():
    global selected
    global CONTACTS
    del CONTACTS[selected[5]]
    view_data()


def update_user():
    global selected
    global CONTACTS
    CONTACTS[selected[5]] = {
        'name': entry_1.get(),
        'last_name': entry_2.get(),
        'code': entry_3.get(),
        'email': entry_4.get(),
        'address': entry_5.get(),
        'phone_number': entry_6.get(),
        'home_phone': entry_7.get(),
    }
    view_data()


def number_list():
    global CONTACTS
    users = [tuple(i.values()) for i in CONTACTS.values()]
    numbers = [user[5] for user in users]
    clear()
    iterate_list(numbers)


def address_list():
    global CONTACTS
    users = [tuple(i.values()) for i in CONTACTS.values()]
    numbers = [user[4] for user in users]
    clear()
    iterate_list(numbers)

def email_list():
    global CONTACTS
    users = [tuple(i.values()) for i in CONTACTS.values()]
    numbers = [user[3] for user in users]
    clear()
    iterate_list(numbers)


def exit_app():
    window.destroy()


# ============================== Labels  =======================================
name_label = Label(window, text="Name")
name_label.grid(row=0, column=0)

last_label = Label(window, text="Last Name")
last_label.grid(row=0, column=6)

code_label = Label(window, text="Code")
code_label.grid(row=2, column=0)

email_label = Label(window, text="Email")
email_label.grid(row=2, column=6)

address_label = Label(window, text="Address")
address_label.grid(row=4, column=0)

mobile_label = Label(window, text="Phone Number")
mobile_label.grid(row=6, column=0)

home_phone_label = Label(window, text="Home Phone")
home_phone_label.grid(row=6, column=6)

# ============================== Entries =======================================
entry_1 = Entry(window, bg='skyblue')
entry_1.grid(row=1, column=0, padx=5, ipady=3)

entry_2 = Entry(window, bg='skyblue')
entry_2.grid(row=1, column=6, ipady=3)

entry_3 = Entry(window, bg='skyblue')
entry_3.grid(row=3, column=0, padx=5, ipady=3)

entry_4 = Entry(window, bg='skyblue')
entry_4.grid(row=3, column=6, padx=5, ipady=3)

entry_5 = Entry(window, width=45, bg='skyblue')
entry_5.grid(row=5, column=0, columnspan=7, ipady=3)

entry_6 = Entry(window, bg='skyblue')
entry_6.grid(row=7, column=0, ipady=3)

entry_7 = Entry(window, bg='skyblue')
entry_7.grid(row=7, column=6, ipady=3)

# ============================== Buttons =======================================
button_1 = Button(window, text='Register', width=20, command=register)
button_1.grid(row=0, column=7, padx=30)

button_2 = Button(window, text='View', width=20, command=view_data)
button_2.grid(row=1, column=7)

button_3 = Button(window, text='Edit', width=20, command=update_user)
button_3.grid(row=2, column=7)

button_4 = Button(window, text='Search', width=20, command=search_user)
button_4.grid(row=3, column=7)

button_5 = Button(window, text='Delete', width=20, command=delete_user)
button_5.grid(row=4, column=7)

button_6 = Button(window, text='Number List', width=20, command=number_list)
button_6.grid(row=5, column=7)

button_7 = Button(window, text='Address List', width=20, command=address_list)
button_7.grid(row=6, column=7)

button_8 = Button(window, text='Email List', width=20, command=email_list)
button_8.grid(row=7, column=7)

button_9 = Button(window, text='Exit', width=20, command=exit_app)
button_9.grid(row=8, column=7)

# ============================== List    =======================================

lst_1 = Listbox(window, width=65, height=13)
lst_1.grid(row=9, column=0, columnspan=8, pady=20)
lst_1.bind("<<ListboxSelect>>", get_selected_row)

# ============================== Scroll  =======================================
scr1 = Scrollbar(window)
scr1.place(x=575, y=400)

# ============================== Configuration =================================
scr1.configure(command=lst_1.yview)
lst_1.configure(yscrollcommand=scr1.set)

# ==============================================================================


window.mainloop()
