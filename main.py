from manage_data import gen_matrix_byNumbers, gen_matrix_byColors
import tkinter as tk  

matrix=gen_matrix_byNumbers()

values=[]
buttons=[] 



def on_click(button,value):
    button.config(state="disabled",text=value,bg="black",fg="white")
    buttons.append(button)
    values.append(value)
    if len(values)==2:  
        if values[0]!=values[1]:
            first_button, second_button = buttons
            first_button.config(bg="red")
            second_button.config(bg="red")
            root.after(1000, reset_buttons, first_button, second_button)
        else:
            first_button, second_button = buttons
            first_button.config(bg="green")
            second_button.config(bg="green")
        values.clear()
        buttons.clear()


def reset_buttons(first_button, second_button):
    first_button.config(state="normal", text="", bg="gray")
    second_button.config(state="normal", text="", bg="gray")


root=tk.Tk()  
root.title("Memory Game")
root.geometry("265x270")
for r in range(4):
    for c in range(3):  
        button=tk.Button(root,width=6,height=2,text="",)
        button.config(command=lambda current_button=button, value=matrix[r][c]: on_click(current_button,value) ,fg="white", bg="gray")
        button.grid(row=r,column=c,padx=5,pady=5)
        

root.mainloop()