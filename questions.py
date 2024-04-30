import tkinter as tk 
from tkinter import StringVar

root = tk.Tk()
root.title("Welcome to quiz Game")
root.geometry('450x450')

sample_text = tk.Text(root, height = 10)
font_tuple = ("Ariel", 20, "bold")
sample_text.configure(font = font_tuple)
root.mainloop()

questions = ["100 + 1 = ?", "500 + 2 = ?", "3 - 3 = ?", "4 + 4 = ?","50 + 55 = ?",]
options = [['10', '101', '2', '22', '2'],['502', '4', '9', '11', '6'],
            ['6', '0', '36', '78', '500'],['13', '8', '4', '88', '80'],['5', '105', '13', '35', '10']]

#padx and pady are space between button widgjets and between the borders of the windows 
frame = tk.Frame(padx=10, pady=10,bg='#fff')
sample_text = tk.Label(frame, height=5, width=28,bg='#ddd',font=("Ariel", 20, "bold"),length= 10)
#StringVar value of widgets entry/label
v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

#radiobutton is multiple choice #lambda creates anonymous functions 
option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=("Ariel", 20, "bold"), command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=("Ariel", 20, "bold"), command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=("Ariel", 20, "bold"), command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=("Ariel", 20, "bold"), command = lambda : checkAnswer(option4))


button_next = tk.Button(frame, text= 'Next',bg ='Green',font=("Ariel", 20, "bold"), command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
sample_text.grid(row=0, column=0)
#stick w can indicate the direction of the widget so it starts off centered than you change direction, in this case west for W
option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option3.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)

index = 0 
correct = 0

#putting buttons in a disabled state 
def disableButtons(state):
    option1['state'] = state 
    option2['state'] = state 
    option3['state'] = state 
    option4['state'] = state 

#radio allows the user to pick from set options 
def checkAnswer(radio):
    global correct, index

    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')
#global index is a function created outside of a function 
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart the quiz':
        correct = 0
        index = 0
        sample_text['bg'] = 'orange' 
        button_next['text'] = 'next'

    if index == len(options):
        sample_text['text'] = str(correct) + " / " + str(len(options))
        button_next['text'] = 'Restart the quiz'
        if correct >= len(options)/2:
            sample_text['bg'] = 'green' 
        else:
            sample_text['bg'] = 'red'



    disableButtons('normal')
    opts = options[index]
    option1['text'] = opts[0]
    option2['text'] = opts[1]
    option3['text'] = opts[2]
    option4['text'] = opts[3]
    v1.set(opts[0])
    v2.set(opts[1])
    v3.set(opts[2])
    v4.set(opts[3])

    if index == len(options) -1:
        button_next['text'] = 'check the results'



    root.mainloop()