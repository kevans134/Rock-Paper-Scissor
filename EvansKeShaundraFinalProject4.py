from tkinter import*
from PIL import ImageTk, Image
from random import randint
from tkinter import ttk


root = Tk()
root.title("Rock, Paper, Scissors")
root.iconbitmap('C:/Users/KeShaundra/PycharmProjects/pythonProject/Images/icon.jpg')
root.geometry("500x600")
#change background color
root.config(bg='blue')
def open():
    top = Toplevel()
    top.geometry("500x600")
    top.config(bg='blue')
    lbl= Label(top, text="Will you like to start the game?").pack()

    rock = PhotoImage(file="C:/Users/KeShaundra/PycharmProjects/pythonProject/Images/rock.jpg")
    paper = PhotoImage(file="C:/Users/KeShaundra/PycharmProjects/pythonProject/Images/paper.jpg")
    scissors = PhotoImage(file="C:/Users/KeShaundra/PycharmProjects\pythonProject/Images/scissors.jpg")
    # Adding Images to a list
    image_list = [rock, paper, scissors]
    # Setting random number between 0 and 2
    pick_number = randint(0, 2)

    image_label = Label(root, image=image_list[pick_number], bd=0)
    image_label.pack(pady=20)

    # creat spin function
    def spin():
        pick_number = randint(0, 2)
        image_label.config(image=image_list[pick_number])

    def user_choice():
        user_choice = ttk.Combobox(top, value=("Rock", "Paper", "Scissors"))
        user_choice.current(0)
        user_choice.pack(pady=10)

    def win_lose_label():
        win_lose_label = Label(top, text="", font=("Helvetica", 18))
        win_lose_label.pack(pady=50)

    # 0 = rock 1= paper 2= scissors
    if user_choice.get() == "rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "scissors":
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="Its A Tie! Try Again...")
        elif pick_number == 1:
            win_lose_label.config(text="Paper beats rock")
        elif pick_number == 2:
            win_lose_label.config(text="Rock beats scissors")

    if user_choice_value == 1:
        if pick_number == 1:
            win_lose_label.config(text="Its A Tie! Try Again...")
        elif pick_number == 0:
            win_lose_label.config(text="Paper beats rock")
        elif pick_number == 2:
            win_lose_label.config(text="Scissor beats paper! You lose...")

    if user_choice_value == 2:
        if pick_number == 2:
            win_lose_label.config(text="Its A Tie! Try Again...")
        elif pick_number == 0:
            win_lose_label.config(text="Rock beats scissor")
        elif pick_number == 1:
            win_lose_label.config(text="Scissors beats Paper! You Win!!")

    # create spin button
    spin_button = Button(top, text="spin!", command=spin)
    spin_button.pack(pady=10)

    # creating exit button
    button_quit = Button(top, text="Exit Program", command=root.quit)
    button_quit.pack()


btn = Button(top,text="Open second window",command=open, bg='red').pack()







root.mainloop()