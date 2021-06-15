def determinant(ls):
  if len(ls)!=1 and len(ls)!=2 and len(ls)!=3:
      return None
  else:
      try:
          if len(ls)==1:
              det=ls[0][0]
          elif len(ls)==2:
              det=(ls[0][0]*ls[1][1])-(ls[0][1]*ls[1][0])
          elif len(ls)==3:
              det=(ls[0][0]*((ls[1][1]*ls[2][2])-(ls[1][2]*ls[2][1])))-(ls[0][1]*((ls[1][0]*ls[2][2])-(ls[1][2]*ls[2][0])))+(ls[0][2]*((ls[1][0]*ls[2][1])-(ls[1][1]*ls[2][0])))       
      except IndexError:
          return None
  return det   