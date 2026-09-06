import tkinter as tk  
root=tk.Tk()  
root.title("Memory Game")
root.geometry("265x270")
for r in range(4):
    for c in range(3):  
        button=tk.Button(root,width=6,height=2)
        button.grid(row=r,column=c,padx=5,pady=5)

root.mainloop()