# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:39:20 2018

@author: yeoka
"""
#stri = "Computing" 
#for i in stri:
#    print(i)
#    if i == 'u' :
#        print( "Found 'u' :) ") 
#        

#def my_function(n): 
#    return_value = None 
#    if n == 0 or n == 1: 
#        return_value = False 
#    i=2 
#    while i < n**0.5: 
#        if n%i==0: 
#            return_value = False 
#            break 
#        i+=1 
#        return_value = True 
#    return return_value
#
#print(my_function(37))

'''q3'''
#import math
#
#def area_square(s):
#    area = s**2
#    return area
#
#
#def vol_frustum(top_area, bottom_area, height):
#    vol = (height / 3) * ( top_area + bottom_area + math.sqrt(top_area * bottom_area) )
#    return vol
#
#def get_volume(s1, s2, height):
#    topa = area_square(s1)
#    bota = area_square(s2)
#    vvol = vol_frustum(topa, bota, height)
#    return vvol

'''q4''' 
#def determinant(matrix):
#    if( len(matrix) != len(matrix[0]) ):
#        for i in matrix:
#            if( matrix.count(list) % len(matrix[0]) != 0 ):
#               return None
#    else:
#        for cube in matrix:
#            if( len(matrix) == 1 ):
#                det = matrix[0]
#                return det
#               
#            elif( len(matrix) == 2 ):
#                det = ( matrix[0][0] * matrix[1][1] ) - ( matrix[0][1] * matrix [1][0] )
#                return det
#                 
#            elif( len(matrix) == 3 ):
#                de1 = (  matrix[0][0] * ( matrix[1][1] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][1] )  )
#                de2 = (  matrix[0][1] * ( matrix[1][0] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][0] )  )
#                de3 = (  matrix[0][2] * ( matrix[1][0] * matrix[2][1] ) - ( matrix[1][1] * matrix [2][0] )  )
#                det = de1 - de2 - de3
#                return det 
#
#
#print(determinant([[100]]) )
#print( determinant( [[0,3,5], [5,5,2], [3,4,3]] )  )


##matrix[int(str(i))]

'''no'''
#def determinant(matrix):
#    for i in matrix:
#        if( len(matrix) != len(str(matrix[int(i)]))  ):
#            if( len(matrix[int(str(i))] )% len(matrix) != 0 ):
#                return None
#    else:
#        for cube in matrix:
#            if( len(matrix) == 1 ):
#                det = matrix[0]
#                return det
#               
#            elif( len(matrix) == 2 ):
#                det = ( matrix[0][0] * matrix[1][1] ) - ( matrix[0][1] * matrix [1][0] )
#                return det
#                 
#            elif( len(matrix) == 3 ):
#                de1 = (  matrix[0][0] * ( matrix[1][1] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][1] )  )
#                de2 = (  matrix[0][1] * ( matrix[1][0] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][0] )  )
#                de3 = (  matrix[0][2] * ( matrix[1][0] * matrix[2][1] ) - ( matrix[1][1] * matrix [2][0] )  )
#                det = de1 - de2 - de3
#                return det 


'''q5'''
#def nroot(n, i, num):
#    if( num < 0 ):
#        return None
#    
#    else:
#        x = x**n
#        
#        
#        
#
#def nroot_complex(n, i, num):
#    if not( num < 0 ):
#        return nroot(n, i, num)
#    
#    else:
#        if( n % 2 == 0 ):
#            bum = nroot(n, i, num) * j
#            return bum 
#        
#        else:
#            pass
        
        
        
'''q6'''
#a
def read_stations(f):
    mydict = {}
    f = open('file', 'r')
    
    for li in f:
        string = f.read()
        strip = string.strip()
        split = strip.split()
        
        for k,v in mydict.items():
            newkey = mydict.dictionary.update(") 
#
#        
#        
#    def diff(p):
#    ans = {}
#    
#    for k,v in p.items():
#        if( k >0 ):
#            diff_power = k - 1
#            ans[diff_power] = k * v 
#            
#    return ans
#    
#
#import numpy as m 