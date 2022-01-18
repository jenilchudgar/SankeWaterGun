from PIL import Image as PIL_IMG
from PIL import ImageTk

from tkinter import messagebox
from tkinter import *

from random import randint

root = Tk()
root.title("Snake Water Gun")
root.iconphoto(True,PhotoImage(file="icon.png"))
root.geometry("400x250")

options = {
    1 : "Snake",
    2 : "Water",
    3 : "Gun"
}

# Functions

# Make Computer's Turn and Decide Winner
def computer_turn(user_move):
    global SCORE
    
    computer_move_num = randint(1,3)
    computer_move = options[computer_move_num]

    if (
        (computer_move_num == 1 and user_move == 3) or
        (computer_move_num == 2 and user_move == 1) or
        (computer_move_num == 3 and user_move == 2)
    ):
        messagebox.showinfo("Snake Water Gun",f"Congrats! You won! Computer chose {computer_move}.")
        SCORE += 1

    elif computer_move_num == user_move:
        messagebox.showinfo("Snake Water Gun",f"Oh! It is a draw! Computer also chose {computer_move}")

    else:
        messagebox.showinfo("Snake Water Gun",f"Alas! You Lost! Computer chose {computer_move}.")
    
    radio_value.set(0) if messagebox.askyesno("Snake Water Gun","You like to reset the game?") else None

# Radio Button Click
def click():
    print(options[radio_value.get()])
    
    computer_turn(radio_value.get())

global DEFAULT_FONT
global SCORE
DEFAULT_FONT = ("Calibri",15)
SCORE = 0

Label(root,text="Snake Water Gun",font=("Pacifico",20)).pack()

# Radio Button Frame
radio_btn_frame = LabelFrame(root,text="Choose One",font=DEFAULT_FONT)
radio_btn_frame.pack()

# Radio Button Variable
radio_value = IntVar(value=0)

# Radio Images
radio_1_img = ImageTk.PhotoImage(PIL_IMG.open("snake.jpg"))
radio_2_img = ImageTk.PhotoImage(PIL_IMG.open("water.png"))
radio_3_img = ImageTk.PhotoImage(PIL_IMG.open("gun.png"))

# Radio Buttons
radio_1 = Radiobutton(radio_btn_frame,image=radio_1_img,variable=radio_value,value=1,command=click)
radio_2 = Radiobutton(radio_btn_frame,image=radio_2_img,variable=radio_value,value=2,command=click)
radio_3 = Radiobutton(radio_btn_frame,image=radio_3_img,variable=radio_value,value=3,command=click)

# Grid the Radio Buttons
radio_1.grid(row=0,column=0,padx=10)
radio_2.grid(row=0,column=1,padx=10)
radio_3.grid(row=0,column=2,padx=10)

# Clear Button
clear_btn = Button(root,text="Clear Selection",font=DEFAULT_FONT,command=lambda: radio_value.set(0))

clear_btn.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()