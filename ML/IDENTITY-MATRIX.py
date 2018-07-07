
# coding: utf-8

# # Identity Matrix
# 
# Write a function called identity_matrix that outputs an identity matrix of size n.
# 
# INPUT
# * n - size of the Identity matrix
# 
# OUPUT
# * identity matrix as a list of lists
# 
# 
# HINTS
# * nested for loops will be helpful
# * the one values are always on the diagonal. To access diagonal values in a list of lists will occur where i = j
# * whenever i does not equal j, the value in the matrix should be 0

# In[1]:


def identity_matrix(n):
    
    identity = []
    
    # TODO: Write a nested for loop to iterate over the rows and
    # columns of the identity matrix. Remember that identity
    # matrices are square so they have the same number of rows
    # and columns
    
    # Make sure to assign 1 to the diagonal values and 0 everywhere
    # else
    for i in range(n):
        row = []
        for j in range(n):
            val = 1 if i == j else 0
            row.append(val)
        identity.append(row)        
    
    return identity


# In[2]:


# TODO: Run this cell to see if your answers are as expected

assert identity_matrix(1) == [[1]]

assert identity_matrix(2) == [[1, 0], 
                             [0, 1]]

assert identity_matrix(3) == [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]

assert identity_matrix(4) == [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]


# # Multiplication with the Identity Matrix
# 
# Copy your matrix multiplication function in the code cell below. Try multiplying a matrix with an identity matrix to prove to yourself that the identity matrix is analogous to multiplyin a scalar by one.

# In[5]:


def transpose(matrix):
    matrix_transpose = []
    
    row_len = len(matrix[0])
    
    for i in range(row_len):
        row = []
        for j in range(len(matrix)):
            val = matrix[j][i]
            row.append(val)
        matrix_transpose.append(row)
        
    return matrix_transpose


# In[6]:


def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        value = vector_one[i] * vector_two[i]
        result += value
    return result


# In[7]:


# TODO: Copy your matrix multiplication function and any other helper
# funcitons here from the previous exercises

def matrix_multiplication(matrixA, matrixB):
    product = []
    B_T = transpose(matrixB)

    for i in range(len(matrixA)):
        a = matrixA[i]
        row = []
        for j in range(len(B_T)):
            b = B_T[j]
            prod = dot_product(a, b)
            row.append(prod)
        product.append(row)
    
    return product


# In[8]:


# TODO: Run this cell to see if your results are as expected.

m = [[5, 9, 2, 4],
     [3, 8, 5, 6],
     [1, 0, 0, 15]]

assert matrix_multiplication(m, identity_matrix(4)) == m
assert matrix_multiplication(identity_matrix(3), m) == m

