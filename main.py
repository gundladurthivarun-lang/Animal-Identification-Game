from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Animal Identification Game")
root.geometry("500x500")

score = 0

animal_label = Label(root, text="Identify the animal")
animal_label.pack()

image = Image.open("images/lion.jpg")
image = image.resize((300, 300))

photo = ImageTk.PhotoImage(image)

image_label = Label(root, image=photo)
image_label.pack()

score_label = Label(root, text="Score: 0")
score_label.pack()


def check_answer(answer):
    global score

    if answer == "Lion":
        score += 1
        score_label.config(text="Score: " + str(score))


Button(root, text="Lion",
       command=lambda: check_answer("Lion")).pack()

Button(root, text="Tiger",
       command=lambda: check_answer("Tiger")).pack()

Button(root, text="Zebra",
       command=lambda: check_answer("Zebra")).pack()

Button(root, text="Elephant",
       command=lambda: check_answer("Elephant")).pack()

root.mainloop()
