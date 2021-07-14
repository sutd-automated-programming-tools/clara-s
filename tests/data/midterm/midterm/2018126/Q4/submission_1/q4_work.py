"""
@author: methylDragon

                       .     .
                    .  |\-^-/|  .    
                   /| } O.=.O { |\  
                  /´ \ \_ ~ _/ / `\
                /´ |  \-/ ~ \-/  | `\
                |   |  /\\ //\  |   | 
                 \|\|\/-""-""-\/|/|/
                         ______/ /
                         '------'
           _   _        _  ___                         
 _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _  
| '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \ 
|_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                   |__/                 |___/          
-------------------------------------------------------
               github.com/methylDragon


2018 MIDTERMS!!!!!

"""

def determinant(matrix):
    
    if not any([len(matrix) != x for x in range(1,4)]):
        return None
    
    if len(matrix) != len(matrix[0]):
        return None

    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    if len(matrix) == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        
        s_mat_a = [x[1:3] for x in matrix[1:3]]
        s_mat_b = [x[::2] for x in matrix[1:3]]
        s_mat_c = [x[0:2] for x in matrix[1:3]]

        return a * determinant(s_mat_a) - b * determinant(s_mat_b) + c * determinant(s_mat_c)
