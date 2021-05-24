from tkinter import *
from random import randint
from tkinter import ttk

# from click import command
root=Tk()
root.title("my first window")
# root.iconbitmap("c:/gui/comedy.ico")
label=Label(root,font=("arial",18),text="rock paper scissor",bg="yellow",fg="blue")
label.pack()
root.geometry("700x700+500+200")
# root.resizable(0,0)
# root.mainloop()


rock=PhotoImage(file="/home/subhangi/Desktop/stone.png")
paper=PhotoImage(file="/home/subhangi/Desktop/paper.png")
scissors=PhotoImage(file="/home/subhangi/Desktop/scissors.png")

# add image to a list

image_list=[rock,paper,scissors]
pick_number=randint(0,2)

# throw up an image when the program start

image_label=Label(root,image=image_list[pick_number],bd=0)
image_label.pack(pady=20)

# creat spin function
def spin():
    pick_number=randint(0,2)
    image_label.config(image_list[pick_number])

    def win():
        print ('You win!')

    def lose():
        print ('You lose!')
    while True:
        player_choice = input("What do you pick? (rock, paper, scissors")
        player_choice.strip()
        random_move = randint(0, 2)
        moves = ['rock', 'paper', 'scissors']
        computer_choice = [random_move]

        if player_choice == computer_choice:
            print ("Draw!")
        elif player_choice == 'rock' or computer_choice == 'scissors':
            win()
            print("ypur player choice is rock and computer choice is scissors,you win!")
        elif  player_choice== 'paper' or computer_choice == 'scissors':
            lose()
            print("ypur player choice is rock and computer choice is scissors,you lose!")
        elif player_choice == 'scissors' or computer_choice == 'paper':
            win()
            print("ypur player choice is rock and computer choice is scissors,you win!")
        elif player_choice == 'scissors' or computer_choice == 'rock':
            lose()
            print("ypur player choice is rock and computer choice is scissors,you lose!")
        elif player_choice == 'paper' or  computer_choice== 'rock':
            win()
            print("ypur player choice is rock and computer choice is scissors,you win!")
        elif player_choice=="rock"  or computer_choice =="paper" :
            lose()
            print("ypur player choice is rock and computer choice is scissors,you lose!")
        again = input('Do you want to play again? (y or n)').strip()
        if again == 'n':
            break
        if player_choice==0:
            if pick_number==0:
                win_lose_label.config(text="it's a tie!,spin again") 
            elif pick_number==1:
                win_lose_label.config(text="paper cover rock!you lose")
user_choice=ttk.Combobox(root,value=("rock","paper","scissors"))
user_choice.current(0)
user_choice.pack(pady=20)
# create spin button
spin_button=Button(root,text="spin !",command=spin)
spin_button.pack(pady=10)

# label for showing if you won or not

win_lose_label=Label(root,text="",font=("snell",28),bg="white")
win_lose_label.pack(pady=50)
def ex():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    exit()
exit_button=Button(root,text="exit",command=exit)
exit_button.pack(pady=20)

root.mainloop()


