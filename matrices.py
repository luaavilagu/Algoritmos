# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

from random import randint
from time import time
 
def sum_matrix(my_matrix1, matrix_B):
 
    for i in range(len(my_matrix1)):
        for j in range(len(my_matrix1[0])):
            my_matrix1[i][j] += my_matrix2[i][j]; 
 
    return my_matrix1;
 
def product_matrix(my_matrix1, my_matrix2):
    row = len(my_matrix1);
    col = len(my_matrix1);
    matrix = [[0 for x in range(row)] for y in range(row)];
 
    for i in range(row):
        for j in range(row):
            for k in range(col):
                matrix[i][j] = my_matrix1[i][k] * my_matrix2[k][j] + matrix[i][j];
 
    return matrix;
 
nlenght = 150
 
my_matrix1 = [[nlenght],[nlenght]]
my_matrix1 = [[0 for x in range(nlenght)] for y in range(nlenght)] 
 
my_matrix2 = [[nlenght],[nlenght]]
my_matrix2 = [[0 for x in range(nlenght)] for y in range(nlenght)] 
 
for i in range( nlenght ):
        for j in range( nlenght ):
                my_matrix1[i][j] = randint(0, 100);
                my_matrix2[i][j] = randint(0, 100);
 
t0 = time();
sum_matrix(my_matrix1, my_matrix2);
t1 = time();
product_matrix(my_matrix1, my_matrix2);
t2 = time();
 
print ('tiempo matriz suma: %f' %(t1-t0));
print ('tiempo matriz multiplicacion: %f' %(t2-t1));