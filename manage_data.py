import random  


matrix=[]
def fill_matrix(number): 
    filled=False  
    while(filled!=True):  
        row=random.randint(0,3)
        column=random.randint(0,2)
        if matrix[row][column]==0:  
            #space is free  
            matrix[row][column]=number  
            filled=True  



def gen_matrix_byNumbers():  
    
    data=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]

    for i in range(4): 
        matrix.append([0 for i in range(3)])    

    for pair in data:  
        fill_matrix(pair[0]) 
        fill_matrix(pair[1])  

    return matrix  



