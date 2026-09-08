from manage_data import gen_matrix_byNumbers
import tkinter as tk  

matrix=gen_matrix_byNumbers()

root=tk.Tk()  
root.title("Memory Game")
root.geometry("265x270")
for r in range(4):
    for c in range(3):  
        button=tk.Button(root,width=6,height=2,text=f"{matrix[r][c]}")
        button.grid(row=r,column=c,padx=5,pady=5)

root.mainloop()