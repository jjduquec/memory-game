import tkinter as tk  
from manage_data import gen_matrix_byNumbers, gen_matrix_byColors


class Game: 
    def __init__(self,root,matrix): 
        self.root=root  
        self.root.title("Memory Game")
        self.root.geometry("265x270")
        self.matrix=matrix 
        self.values=[]
        self.buttons=[] 

        for r in range(4):
          for c in range(3):  
            button=tk.Button(root,width=6,height=2,text="",)
            button.config(command=lambda current_button=button, value=matrix[r][c]: self.on_click(current_button,value) , bg="gray")
            button.grid(row=r,column=c,padx=5,pady=5)

    def on_click(self,button,value):
        button.config(state="disabled",text=value,bg="black",fg="white")
        self.buttons.append(button)
        self.values.append(value)
        if len(self.values)==2:  
            if self.values[0]!=self.values[1]:
                first_button, second_button = self.buttons
                first_button.config(bg="red")
                second_button.config(bg="red")
                self.root.after(1000, self.reset_buttons, first_button, second_button)
            else:
                first_button, second_button = self.buttons
                first_button.config(bg="green")
                second_button.config(bg="green")
            self.values.clear()
            self.buttons.clear()


    def reset_buttons(self,first_button, second_button):
        first_button.config(state="normal", text="", bg="gray")
        second_button.config(state="normal", text="", bg="gray")


class GameByNumbers(Game): 

    def __init__(self,root): 
        self.matrix=gen_matrix_byNumbers()  
        self.root=root
        super().__init__(self.root,self.matrix)





root=tk.Tk()  
game=GameByNumbers(root) 
root.mainloop()