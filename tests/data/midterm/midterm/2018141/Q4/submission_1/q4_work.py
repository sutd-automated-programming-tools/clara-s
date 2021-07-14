import numpy as np

def determinant(matrix):
    try:
        a = np.array(matrix)
        return round(np.linalg.det(a),1)
    except:
        return None