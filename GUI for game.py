import Tkinter, tkFont
#today we are going to construct a Graphical Usre Interface(GUI)
root = Tkinter.Tk()
root.title('Alex\'s awesome counting software')

canvas = Tkinter.Canvas(root, height = 250, width = 600, relief = Tkinter.RAISED, bg = 'pink')
canvas.grid(row=0,column=0)

customFont = tkFont.Font(family='serif', size=20)
editor2= Tkinter.Text(width=20, height=4, font=customFont)
editor2.grid(row=2, column=2)

times_pressed = 0
def pressed(x):
    #deletes text box
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += x
    #recreates text box
    customFont = tkFont.Font(family='serif', size=20)
    editor= Tkinter.Text(width=20, height=4, font=customFont)
    editor.grid(row=2, column=1)
    #Adds the text to the box
    editor.insert(Tkinter.END, "Number of bunnies Areg has killed: ")
    editor.insert(Tkinter.END, times_pressed)
    editor.see(Tkinter.END)
    
    #disable changing the text box
    editor.config(state=Tkinter.DISABLED)
    #editor.config(state=Tkinter.NORMAL
    
button = Tkinter.Button(root, text ='North', width=10, height =5,command = lambda: pressed(1))
button.grid(row=1, column=0, pady = 100)

button = Tkinter.Button(root, text ='East',  width=10, height =5, command = lambda: pressed(2))
button.grid(row=1, column=1, pady = 100)

button = Tkinter.Button(root, text ='South',  width=10, height =5, command = lambda: pressed(3))
button.grid(row=1, column=2, pady = 100)

button = Tkinter.Button(root, text ='West',  width=10, height =5, command = lambda: pressed(4))
button.grid(row=1, column=3, pady = 100)
    
#radio = [0]*4 #create a list
#data = Tkinter.IntVar()
#for i in range(4):
   # radio[i] = Tkinter.Radiobutton(root, text=str(i),
  #                          variable=data, value=i)
 #   radio[i].grid(row=3,column=i)
#data.set(3)

root.mainloop()