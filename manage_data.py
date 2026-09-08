import random  


matrix=[["" for i in range(3)] for x in range(4) ]

def fill_matrix(item): 
    filled=False  
    while(filled!=True):  
        row=random.randint(0,3)
        column=random.randint(0,2)
       
        if matrix[row][column]=="":  
            #space is free  
            matrix[row][column]=item
            filled=True  



def gen_matrix_byNumbers():  
    
    data=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]

    for pair in data:  
        fill_matrix(str(pair[0])) 
        fill_matrix(str(pair[1]))  

    return matrix  



