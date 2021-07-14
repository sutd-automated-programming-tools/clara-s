def determinant(matrix):
    len(matrix) = n
    mat = []
    if n<1 or n > 3:
        return None
    if n == 1:
        return i
    if n == 2:
        value = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
        
#check the validity of size of the matrix 
#make a new nested-list to represent the matrix since making the check of n easier when u look at the length of the list
#Eg. mat = [] -> mat = [[a,b],[c,d]]
#when n > 3 or n < 1, return None as the matrix is invalid
#when n == 1, det(M) is the first element
#when n == 2, take the first element -> mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
#best to create a function for n=2
#when n == 3,
#mat = [[a,b,c],[d,e,f],[g,h,i]]
#call function n2 then put into the determinant formula
#or split calculations slowly
# part1 = find det of 1st,2nd ,3rd box
#part 2 put in the final formula