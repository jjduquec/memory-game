import random  


class GenData: 
    def __init__(self):

        self.matrix=[["" for i in range(3)] for x in range(4) ]



    def _fill_matrix(self,item): 
        """
        asing a random position for item  at matrix 
        """
        filled=False  
        while(filled!=True):  
            row=random.randint(0,3)
            column=random.randint(0,2)
        
            if self.matrix[row][column]=="":  
                #space is free  
                self.matrix[row][column]=item
                filled=True  



    def gen_matrix_byNumbers(self):  
        
        data=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]

        for pair in data:  
            self._fill_matrix(str(pair[0])) 
            self._fill_matrix(str(pair[1]))  

        return self.matrix  


    def gen_matrix_byColors(self):  
        data=[("red","red"),("blue","blue"),("green","green"),("yellow","yellow"),("orange","orange"),("purple","purple")]
        for pair in data:
            self._fill_matrix(pair[0])  
            self._fill_matrix(pair[1])

        return self.matrix
        



