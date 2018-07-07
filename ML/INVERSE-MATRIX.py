
# coding: utf-8

# # Matrix Inverse
# 
# In this exercise, you will write a function to calculate the inverse of either a 1x1 or a 2x2 matrix.

# In[18]:


### TODO: Write a function called inverse_matrix() that 
###       receives a matrix and outputs the inverse
###       
###       You are provided with start code that checks
###       if the matrix is square and if not, throws an error
###
###       You will also need to check the size of the matrix.
###       The formula for a 1x1 matrix and 2x2 matrix are different,
###       so your solution will need to take this into account.
###
###       If the user inputs a non-invertible 2x2 matrix or a matrix
###       of size 3 x 3 or greater, the function should raise an
###       error. A non-invertible
###       2x2 matrix has ad-bc = 0 as discussed in the lesson
###
###       Python has various options for raising errors
###       raise RuntimeError('this is the error message')
###       raise NotImplementedError('this functionality is not implemented')
###       raise ValueError('The denominator of a fraction cannot be zero')

def inverse_matrix(matrix):
    
    inverse = []
    
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')
    
    ## TODO: Check if matrix is larger than 2x2.
    ## If matrix is too large, then raise an error
    
    ## TODO: Check if matrix is 1x1 or 2x2.
    ## Depending on the matrix size, the formula for calculating
    ## the inverse is different. 
    # If the matrix is 2x2, check that the matrix is invertible
    m_rows = len(matrix)
    m_cols = len(matrix[0])
    
    #1 x 1
    if m_rows == 1 and m_cols == 1:
        val = matrix[0][0]
        row = []
        row.append(1/val)
        inverse.append(row)
    
    elif m_rows == 2 and m_cols == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        
        ad = a * d
        bc = b * c
        
        if ad == bc:
            raise ValueError('Matrix is non-invertible')
        
        mult = 1/(ad - bc)
        
        #print(mult)
            
        row1 = [1. * d * mult, -1. * b * mult]
        row2 = [-1. * c * mult, 1. * a * mult]
        
        inverse.append(row1)
        inverse.append(row2)
        #print(inverse)
        
    else:
        raise ValueError('Invalid matrix size')
        

    

    ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.
    
    return inverse
    
    


# In[19]:


## TODO: Run this cell to check your output. If this cell does 
## not output anything your answers were as expected.

assert inverse_matrix([[100]]) == [[0.01]]
assert inverse_matrix([[4, 5], [7, 1]]) == [[-0.03225806451612903, 0.16129032258064516],
 [0.22580645161290322, -0.12903225806451613]]


# In[20]:


### Run this line of code and see what happens. Because ad = bc, this
### matrix does not have an inverse
inverse_matrix([[4, 2], [14, 7]])


# In[21]:


### Run this line of code and see what happens. This is a 3x3 matrix
inverse_matrix([[4, 5, 1], [2, 9, 7], [6, 3, 9]])

