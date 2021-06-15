def determinant(matrix):
    #implement checker
    row = len(matrix)
    col = len(matrix[0])
    #print (row, col)
    
    if row != col or row<1 or row>3 or col<1 or col>3:
        return None
    
    #calculate det
    det = 0
    #n = 1 case
    if row == 1:
        det  = a
        return det
    #n = 2 case
    if row == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return det
    #n =3 case
    if row == 3:
        m_dict = {}
        p = 1
        for x in matrix:
            for y in x:
                m_dict.update({p:y})
                p+=1
        det = m_dict[1]*(m_dict[5]*m_dict[9]-m_dict[6]*m_dict[8]) - m_dict[2]*(m_dict[4]*m_dict[9]-m_dict[6]*m_dict[7]) +  m_dict[3]*(m_dict[4]*m_dict[8]-m_dict[5]*m_dict[7])
        return det
      
print(determinant([[0,3,5], [5,5,2], [3,4,3]]))