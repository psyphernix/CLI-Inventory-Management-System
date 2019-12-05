#-------------------------------To read text file-----------------------------#
def file_read(file):
    '''create function to read file and store data in list'''
    outlist = [] # to create empty list
    print("-------------------------------------")
    print('\t',"Available Products")
    print("Product",'\t',"Price",'\t',"Quantity")
    with open(file, 'r') as lines: # to open file in reading mode
        for line in lines: # to iterate through lines of file
            inlist = [lst.strip() for lst in line.split(',')] # .strip() removes whitesapces and .split(',') separates content by comma and append them in list
            outlist.append(inlist) # to append list to another to create 2D list
            print(line.replace(",",'\t')) # to display available items in screen
    print("-------------------------------------")
    for i in outlist: # to iterate through 2D list
        for j in range(len(i)):
            if j == 1 or j == 2:
                i[j] = int(i[j]) # to change string elements at index 1 and 2 to integers
    return outlist # to return return 2D list as output of the function
