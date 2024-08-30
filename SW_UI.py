from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil


root = Tk()
root.geometry("1320x660")
root.title("R3ND3R UI")
root.config(background="black")
#root.config(background="C:\Users\SHREYASH S BHATKAR\Pictures\Saved Pictures\bakugo.jpg")
#bg = PhotoImage(file = "C:\Users\SHREYASH S BHATKAR\Pictures\Saved Pictures\bakugo.jpg")

def open_file():
    file = filedialog.askopenfilename()
    os.startfile(file)
    messagebox.showinfo('Render your Model', file+" Model rendered successfully.")


def delete_file():
    file = filedialog.askopenfilename()
    os.remove(file)
    messagebox.showinfo('Delete your Model', file+"Model deletion successful.")


def rename_file():
    global filename, file, f1, path
    file = filedialog.askopenfilename()
    path = os.path.abspath(file)
    f1 = Frame(root, background="grey")
    f1.grid(row=6, column=2)
    Label(f1, text="Enter the Model(File) Name").grid(row=0, column=1, padx=10, pady=10)
    filename = Entry(f1)
    filename.grid(row=1, column=1, padx=10, pady=10)
    Button(f1, text='Rename your Model', command=change_name).grid(row=2, column=1, padx=10, pady=10)
    Button(f1, text='Cancel?', command=f1.destroy).grid(row=2, column=2)
    f1.mainloop()



def change_name():
    newName = filename.get()
    dir = os.path.dirname(path)
    renamed = os.path.join(dir,newName)
    os.rename(path, renamed)
    f1.destroy()
    messagebox.showinfo('Rename your Model', file + "Model to be renamed successfully.")


def deletefolder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    messagebox.showinfo('Confirmation', "Folder Deleted!")


def create_folder():
    global name_entry, dir, f
    dir = filedialog.askdirectory()
    f = Frame(root, background="white")
    f.grid(row=6,column=0)
    Label(f, text="Enter the Folder Name",bg='white',font="bold").grid(row=0, column=0,padx=10,pady=10)
    name_entry = Entry(f,bd=4,width=25,relief=SUNKEN)
    name_entry.grid(row=1, column=0,padx=10,pady=10)
    Button(f, text='Create Folder',font="bold",bg='dark green',fg='white', command=makeFolder).grid(row=2, column=0,padx=10,pady=10)
    Button(f, text='Cancel',font="bold",bg='red2',fg='white', command=f.destroy).grid(row=2, column=1)
    f.mainloop()


def makeFolder():
    name = name_entry.get()
    os.chdir(dir)
    os.makedirs(name)
    f.destroy()
    messagebox.showinfo('Create Folder', " Folder Created Successfully")


def rename_folder():
    global dir, folder_name, f1,path
    dir = filedialog.askdirectory()
    path = os.path.abspath(dir)
    f1 = Frame(root, background="grey")
    f1.grid(row=6, column=2)
    Label(f1, text="Enter the Folder Name").grid(row=0, column=1, padx=10, pady=10)
    folder_name = Entry(f1)
    folder_name.grid(row=1, column=1, padx=10, pady=10)
    Button(f1, text='Rename Folder', command=change_folder).grid(row=2, column=1, padx=10, pady=10)
    Button(f1, text='Cancel', command=f1.destroy).grid(row=2, column=2)
    f1.mainloop()


def change_folder():
    newName = folder_name.get()
    dir = os.path.dirname(path)
    renamed = os.path.join(dir,newName)
    os.rename(path, renamed)
    f1.destroy()
    messagebox.showinfo('Rename Folder', path + " Renamed Successfully")


def view_folder():
    dir = filedialog.askdirectory()
    f1=Frame(root)
    f1.grid(row=5, column=2)
    listbox = Listbox(f1,width=30)
    listbox.grid(row=0,column=0)
    files = os.listdir(dir)
    for name in files:
        listbox.insert('end', name)
    exit_button = Button(f1, text='Okay', bg='dark green',fg='white',font="bold", command=f1.destroy)
    exit_button.grid(row=1, column=0)


def copy_move_file():
    global sourceText, destinationText, destination_location, f1
    f1 = Frame(root, width=350, height=300, background="lavender")
    f1.grid(row=5, column=0, columnspan=4)

    source_location = StringVar()
    destination_location = StringVar()

    link_Label = Label(f1, text="Select The File To Copy ", font="bold", bg='lavender')
    link_Label.grid(row=0, column=0, pady=5, padx=5)

    sourceText = Entry(f1, width=50, textvariable=source_location, font="12")
    sourceText.grid(row=0, column=1, pady=5, padx=5)
    source_browseButton = Button(f1, text="Browse",bg='cyan2', command=source_browse, width=15, font="bold")
    source_browseButton.grid(row=0, column=2, pady=5, padx=5)

    destinationLabel = Label(f1, text="Select The Destination", bg="lavender", font="bold")
    destinationLabel.grid(row=1, column=0, pady=5, padx=5)

    destinationText = Entry(f1, width=50, textvariable=destination_location, font=12)
    destinationText.grid(row=1, column=1, pady=5, padx=5)
    dest_browseButton = Button(f1, text="Browse", bg='cyan2', command=destination_browse, width=15, font="12")
    dest_browseButton.grid(row=1, column=2, pady=5, padx=5)

    copyButton = Button(f1, text="Copy File", bg='dark green',fg='white',command=copy_file, width=15, font=('bold',12))
    copyButton.grid(row=2, column=0, pady=10, padx=10)

    moveButton = Button(f1, text="Move File", bg='dark green',fg='white',command=move_file, width=15, font=('bold',12))
    moveButton.grid(row=2, column=1, pady=10, padx=10)

    cancelButton = Button(f1, text="Cancel",bg='red2',fg='white', command= f1.destroy, width=15, font=('bold',12))
    cancelButton.grid(row=2, column=2, pady=10, padx=10)


def source_browse():
    global files_list
    files_list = list(filedialog.askopenfilenames())
    sourceText.insert('1', files_list)


def destination_browse():
    destinationdirectory = filedialog.askdirectory()
    destinationText.insert('1', destinationdirectory)


def copy_file():
    dest_location = destination_location.get()
    for f in files_list:
        shutil.copy(f, dest_location)
    messagebox.showinfo('Copy Model',"Copied successfully")
    f1.destroy()


def move_file():
    dest_location = destination_location.get()
    for f in files_list:
        shutil.move(f, dest_location)
    messagebox.showinfo('Move Model',"Moved Model Successfully")
    f1.destroy()


lbl_heading = Label(root, text="Welcome to R3ND3R⛰",font=("italic",24),fg="#716DE5",bg='black')
lbl_heading.place(relx = 0.5,
                rely = 0.1,
                anchor = 'center')


open_btn = Button(root, text="Render Model⛰",command=open_file, width=15,font=('bold',14),bg="#6C4FC4")
open_btn.place(relx = 0.1,
                rely = 0.2,
                anchor = 'center')

delete_btn = Button(root, text="Delete Model⛰",command=delete_file, width=15,font=('bold',14),bg="#5782C7")
delete_btn.place(relx = 0.4,
                rely = 0.2,
                anchor = 'center')

rename_btn = Button(root, text="Rename Model⛰", command=rename_file, width=15,font=('bold',14),bg="#5782C7")
rename_btn.place(relx = 0.6,
                rely = 0.2,
                anchor = 'center')

copy_move_btn = Button(root, text="Copy/Move Model⛰", command=copy_move_file, width=18,font=('bold',14),bg="#6C4FC4")
copy_move_btn.place(relx = 0.9,
                rely = 0.2,
                anchor = 'center')
create_folder_btn = Button(root, text="Create Folder📂", command=create_folder, width=15,font=('bold',14),bg="#6C4FC4")
create_folder_btn.place(relx = 0.1,
                rely = 0.3,
                anchor = 'center')

deletefolder_btn = Button(root, text="Delete Folder♻", command=deletefolder, width=15,font=('bold',14),bg="#5782C7")
deletefolder_btn.place(relx = 0.4,
                rely = 0.3,
                anchor = 'center')

rename_folder_btn = Button(root, text="Rename Folder📂", command=rename_folder, width=15,font=('bold',14),bg="#5782C7")
rename_folder_btn.place(relx = 0.6,
                rely = 0.3,
                anchor = 'center')

view_btn = Button(root, text="View Folder Contents👀", command=view_folder, width=19,font=('bold',14),bg="#6C4FC4")
view_btn.place(relx = 0.9,
                rely = 0.3,
                anchor = 'center')

exit_btn = Button(root, text="Exit🔚", command=root.destroy, width=12,font=('bold',14),bg="#6C4FC4")
exit_btn.place(relx = 0.5,
                rely = 0.4,
                anchor = 'center')

root.mainloop()
