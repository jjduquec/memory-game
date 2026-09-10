from manage_data import gen_matrix_byNumbers
import tkinter as tk  

matrix=gen_matrix_byNumbers()

values=[]
buttons=[] 



def on_click(button,value):
    button.config(state="disabled")
    buttons.append(button)
    values.append(value)
    if len(values)==2:  
        if values[0]!=values[1]:
            buttons[0].config(state="normal")
            buttons[1].config(state="normal") 
        values.clear()
        buttons.clear()






root=tk.Tk()  
root.title("Memory Game")
root.geometry("265x270")
for r in range(4):
    for c in range(3):  
        
        button=tk.Button(root,width=6,height=2,text=f"{matrix[r][c]}",)
        button.config(command=lambda current_button=button, value=matrix[r][c]: on_click(current_button,value) )
        button.grid(row=r,column=c,padx=5,pady=5)
        

root.mainloop()