def determinant(matrix):
  if len(matrix) == 1:
      ans1 = matrix[0][0]
      return ans1
  elif len(matrix) > 1:
      for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
          return None
        elif len(matrix) == 2:
          ans2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
          return ans2
        elif len(matrix) == 3:
          ans3 = matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][2]*matrix[1][0]*matrix[2][1] + matrix[0][1]*matrix[2][0]*matrix[1][2] - matrix[0][2]*matrix[1][1]*matrix[2][0] - matrix[0][0]*matrix[1][2]*matrix[2][1] - matrix[0][1]*matrix[1][0]*matrix[2][2]
          return ans3


