
# coding: utf-8

# # Transpose of a Matrix
# 
# In this set of exercises, you will work with the transpose of a matrix.
# 
# Your first task is to write a funciton that takes the transpose of a matrix. Think about how to use nested for loops efficiently.
# 
# The second task will be to write a new matrix multiplication function that takes advantage of your matrix transposition function.

# In[5]:


### TODO: Write a function called transpose() that 
###       takes in a matrix and outputs the transpose of the matrix

def transpose(matrix):
    matrix_transpose = []
    
    row_len = len(matrix[0])
    
    for i in range(row_len):
        row = []
        for j in range(len(matrix)):
            val = matrix[j][i]
            row.append(val)
        matrix_transpose.append(row)
                       
        
    
#     m_len = len(matrix) 
#     for i in range(m_len):
#         for j in range(m_len):
#             for k in range(len(matrix[j])):
            
#     #swap i and j
#     for i in range(m_len):
#         for j in range(m_len):
#                 for k in range(len(matrix[j]))
                    
    
    return matrix_transpose


# In[6]:


### TODO: Run the code in the cell below. If there is no 
###       output, then your answers were as expected

assert transpose([[5, 4, 1, 7], [2, 1, 3, 5]]) == [[5, 2], [4, 1], [1, 3], [7, 5]]
assert transpose([[5]]) == [[5]]
assert transpose([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]]) == [[5, 7, 1, 8], [3, 1, 1, 9], [2, 4, 2, 1]]


# ### Matrix Multiplication
# 
# Now that you have your transpose function working, write a matrix multiplication function that takes advantage of the transpose. 
# 
# As part of the matrix multiplication code, you might want to re-use your dot product function from the matrix multiplication exercises. But you won't need your get_row and get_column functions anymore because the tranpose essentially takes care of turning columns into row vectors.
# 
# Remember that if matrix A is mxn and matrix B is nxp, then the resulting product will be mxp.

# In[9]:


### TODO: Write a function called matrix_multiplication() that
###       takes in two matrices and outputs the product of the two
###       matrices

### TODO: Copy your dot_product() function here so that you can
###       use it in your matrix_multiplication function
def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        value = vector_one[i] * vector_two[i]
        result += value
    return result

def matrix_multiplication(matrixA, matrixB):
    product = []
    
    
    ## TODO: Take the transpose of matrixB and store the result
    ##       in a new variable
    B_T = transpose(matrixB)
    
    
    ## TODO: Use a nested for loop to iterate through the rows
    ## of matrix A and the rows of the tranpose of matrix B
    for i in range(len(matrixA)):
        a = matrixA[i]
        row = []
        for j in range(len(B_T)):
            b = B_T[j]
            prod = dot_product(a, b)
            row.append(prod)
        product.append(row)
    
    ## TODO: Calculate the dot product between each row of matrix A
    ##         with each row in the transpose of matrix B
    
    ## TODO: As you calculate the results inside your for loops,
    ##       store the results in the product variable
    
    
    ## TODO:
    return product


# In[10]:


### TODO: Run the code in the cell below. If there is no 
###       output, then your answers were as expected

assert matrix_multiplication([[5, 3, 1], 
                              [6, 2, 7]], 
                             [[4, 2], 
                              [8, 1], 
                              [7, 4]]) == [[51, 17], 
                                           [89, 42]]

assert matrix_multiplication([[5]], [[4]]) == [[20]]

assert matrix_multiplication([[2, 8, 1, 2, 9],
                             [7, 9, 1, 10, 5],
                             [8, 4, 11, 98, 2],
                             [5, 5, 4, 4, 1]], 
                             [[4], 
                              [2], 
                              [17], 
                              [80], 
                              [2]]) == [[219], [873], [8071], [420]]


assert matrix_multiplication([[2, 8, 1, 2, 9],
                             [7, 9, 1, 10, 5],
                             [8, 4, 11, 98, 2],
                             [5, 5, 4, 4, 1]], 
                             [[4, 1, 2], 
                              [2, 3, 1], 
                              [17, 8, 1], 
                              [1, 3, 0], 
                              [2, 1, 4]]) == [[61, 49, 49], [83, 77, 44], [329, 404, 39], [104, 65, 23]]

