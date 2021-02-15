'''
first reverse matrix
then for each row
    for each column -> flip coordinates
time: o(n**2)
'''
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
           matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
