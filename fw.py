#-----------------------------to write file-----------------------------------#
def file_write(fr_list,ui_list,file):
    '''create function to write changes to file'''
    for i in fr_list: # to iterate in list of available items
        for x in ui_list: # to iterate in user input list
            if x[0] in i: # to check if item bought by customer is in items list
                i[2] = i[2] - x[1] # to reduce quantity in items by subtracting bought quantity
    with open(file, 'w') as files: # to open textfile in write mode
        files.writelines(',''\t'.join(str(j) for j in i) + '\n' for i in fr_list) # to write changes to file
    return None # function has no return value


