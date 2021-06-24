# Programmer - python_scripts (Abhijith Warrier)

# A PYTHON GUI TO CONVERT USER-INPUT TEXT INTO HAND WRITTEN CHARACTERS FORMAT USING pywhatkit LIBRARY
#
# PyWhatKit is a Python library with various helpful features. It is an easy to use library which does not requires
# you to do some additional setup.
#
# The module can be installed using the command - pip install pywhatkit

# Importing necessary packages
import pywhatkit
import tkinter as tk
from tkinter import *
from datetime import datetime as dt
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk


# Defining CreateWidgets() function to create necessary tkinter widgets
# FOR BUTTON BACKGROUND COLOR USE bg ARGUMENT IN WINDOWS AND highlightbackground ARGUMENT IN MAC
def CreateWidgets():
    saveImageLabel = Label(root, text='PNG NAME : ', font=('', 15, 'bold'), bg='cyan4')
    saveImageLabel.grid(row=0, column=0, padx=5, pady=5)

    saveImageEntry = Entry(root, width=20, textvariable=imageName, bg='darkgrey')
    saveImageEntry.grid(row=0, column=1, padx=5, pady=5)

    imageBrowseButton = Button(root, text='Browse', width=10, command=imageBrowse, highlightbackground='yellow')
    imageBrowseButton.grid(row=0, column=2, padx=5, pady=5)

    textLabel = Label(root, text='FILE TEXT : ', font=('', 15, 'bold'), bg='cyan4')
    textLabel.grid(row=1, column=0, padx=5, pady=5)

    root.textEntry = Text(root, width=70, height=30, bg='darkgrey')
    root.textEntry.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    clearTextButton = Button(root, text='Clear', width=10, command=textClear, highlightbackground='red')
    clearTextButton.grid(row=3, column=0, padx=5, pady=5)

    imageSaveButton = Button(root, text='Convert', width=10, command=textConvert, highlightbackground='green')
    imageSaveButton.grid(row=3, column=2, padx=5, pady=5)

    hwLabel = Label(root, text='TEXT CONVERTED TO HANDWRITING', font=('',15, 'bold'), bg='cyan4')
    hwLabel.grid(row=0, column=3, padx=5, pady=5, columnspan=2)

    root.imageLabel = Label(root, bg="cyan4", relief="groove", font=('', 109), width=9)
    root.imageLabel.grid(row=2, column=3, padx=5, pady=5, columnspan=2)


# Defining the Browse() to save the file
def imageBrowse():
    # Fetching the user-input filename and destination path using asksaveasfilename
    # Setting the initialdir and filetypes arguments are optional.
    i_name = filedialog.asksaveasfilename(initialdir='YOUR DESIRED PATH',
                                          filetypes=(('PNG File (*.png)','*.png'),
                                                     ('All File')))
    # Setting the fileName tkinter variable to the file_name value
    imageName.set(i_name)


# Defining the textClear() to clear the contents of the fileTextEntry
def textClear():
    # Clearing the contents of the fileTextEntry using the delete()
    root.fileTextEntry.delete('1.0', END)


# Defining textConvert() to write the contents of TextEntry to the HandWritten Image Format
def textConvert():
    # Getting the imagename with the path using the get() and storing it in the file_name_path
    image_name_path = imageName.get()
    # Checking if the user has entered image name and destination
    if len(image_name_path) == 0:
        image_path = 'YOUR DESIRED PATH'
        image_name_path = image_path + str(dt.now().strftime('%d%m%Y %H%M'))+'.png'

    # Getting the contents of the fileTextEntry using the get() and storing in fileContent
    textContent = root.textEntry.get('1.0', END)
    # Converting the entered text to hand written characters using the text_to_handwriting() method of pywhatkit.
    # Parameters that are set: string (required) - Text To Be Converted, save_to (optional) - Setting it to
    # user-selected path or the default path, rgb (optional) - Color of the handwritten character in rgb format
    pywhatkit.text_to_handwriting(textContent, save_to=image_name_path, rgb=[0,0,255])
    # Displaying message
    messagebox.showinfo('SUCCESS!','FILE SAVED')

    # Opening the saved image using the open() of Image class which takes the saved image as the argument
    imageView = Image.open(image_name_path)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((600, 398), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.imageLabel.config(image=imageDisplay, width=600, text='')
    # Keeping a reference
    root.imageLabel.photo = imageDisplay


# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, background color and disabling the resizing property
root.title('PyTextToHandWriting')
root.geometry('1140x560')
root.resizable(False, False)
root.configure(background='cyan4')

# Creating tkinter variable
imageName = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
