def multiTable(rows,cols):
    row_list = []
    for r in range(1,rows+1):
        col_list = []
        for c in range(1,cols+1):
            col_list.append(r*c)
        row_list.append(col_list)
    return row_list   
