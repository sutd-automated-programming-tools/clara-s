def determinant(matrix):
	#pseudo code
    # check dimensions of matrix by finding out the len of matrix and the len of the sublist in the matrix.
    # both len(matrix) == len(sublist) , where the values can only be 1,2 or 3
    #else return None.
    
    #if len(matrix)== len(sublist) == 1:
    #   return(int(sublist))
    
    #if len(matrix)== len(sublist) == 2:
    #   return(element in the first position of the first list*element in the second position of the second list-element in the second position of the first list*element in the first position of the second list)
    
    #if len(matrix)== len(sublist) == 3:
    #output = []
    #output1 = []
    #for i in matrix:
    #     for j in matrix:
    #     output.append(matrix[i][0]) (this is to extract the first element from each list out)
    # compute the determinants of the remaining 3 lists consisting of 2 elements each and append the values to another list called output1
    # zip(i,j) for i,j in output,output1
    #compute the 3 lists by multiplyong both values together    
    #compute the overall determinant by adding the first and third value and subtracting the second value