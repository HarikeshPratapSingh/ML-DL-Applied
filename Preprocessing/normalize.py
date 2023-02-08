#Normalization is the process of scaling individual samples to have unit norm
# Types: l1,l2,max
#u is a vector then
#l1 normalization = u/|u|
#l2 normalization = u/||u||
#max normalization = u/max(u)

import math
import numpy as np

def normalize(mat,norm="l2",axis="col"):
    """
    mat: matrix whose rows or columns is to be normalized
    norm: type of normalization {l1,l2,max}
    axis: axis of normalization {row,col}
    """
    
    if norm not in ("l1", "l2", "max"):
        raise ValueError("'%s' is not a supported norm" % norm)
    if axis not in ("row","col"):
        raise ValueError("'%s' is not a supported axis" % norm)
    
    matrix = np.array(mat,dtype=float)
    
    if axis=="row":
        if norm=="l1": #sum of absolute values
            for x in range(len(matrix)):
                abs_sum = 0
                for y in matrix[x]:
                    abs_sum += abs(y)
                matrix[x] /= abs_sum
                
        if norm=="l2": #sqrt of sum of squared values
            for x in range(len(matrix)):
                sq_sum = 0
                for y in matrix[x]:
                    sq_sum += y*y
                sq_sum = math.sqrt(sq_sum)
                matrix[x] /= sq_sum
                
        if norm=="max": #max of all values
            for x in range(len(matrix)):
                max_val = max(abs(matrix[x]))
                matrix[x] /= max_val
            
    if axis=="col":
        if norm=="l1": #sum of absolute values
            for x in range(len(matrix[0])):
                abs_sum = 0
                for y in matrix[:,x]:
                    abs_sum += abs(y)
                matrix[:,x] /= abs_sum
            
        if norm=="l2":
            for x in range(len(matrix[0])):
                sq_sum = 0
                for y in matrix[:,x]:
                    sq_sum += y*y
                sq_sum = math.sqrt(sq_sum)
                matrix[:,x] /= sq_sum
        
        if norm=="max":
            for x in range(len(matrix[0])):
                max_val = max(abs(matrix[:,x]))
                matrix[:,x] /= max_val
    return matrix