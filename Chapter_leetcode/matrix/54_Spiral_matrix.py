
def spiralOrder(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1 
    col_end = len(matrix[0])-1
    while (row_begin <= row_end and col_begin <= col_end):
        #right
        res.extend([matrix[row_begin][i] for i in range(col_begin,col_end+1)])
        row_begin += 1
        #down
        res.extend([matrix[i][col_end] for i in range(row_begin,row_end+1)])
        col_end -= 1
        #left
        if (row_begin <= row_end):
            res.extend([matrix[row_end][i] for i in range(col_end,col_begin-1,-1)])
            row_end -= 1
        #up
        if (col_begin <= col_end):
            res.extend([matrix[i][col_begin] for i in range(row_end,row_begin-1,-1)])
            col_begin += 1
    return res


# a = [[ 1, 2, 3, 4 ],
#     [ 5, 6, 7, 8 ],
#     [ 9, 10, 11, 12 ],
#     [ 13, 14, 15, 16 ]]
 
# for x in spiralOrder(a):
#     print(x ,end=" ")
  

#https://www.youtube.com/watch?v=pcPFrFK-ZVk