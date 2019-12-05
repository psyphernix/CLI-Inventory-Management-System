'''
Author : Bijay Aashish Bhatta
Version: 1.0
'''
#------------------------------------Main-------------------------------------#
# to import different functions from respective module
from fr import file_read
from ui import user_input
from inv import invoice
from fw import file_write
print("Welcome to Astro Electronics Limited!")
fle = "items.txt" # to assign text file to varialble fle
respo = "no" # default response for exiting application
while respo == "no": # to repeat given lines when response is equal to no
       fread =  file_read(fle) # to call file reading function and assign its return value as freads
       ulist =  user_input(fread) # to call user input function and assign its return value as ulist
       if ulist != False: # If ulist is not equal to False, do following operations
           invoice(fread, ulist) # to call invoice function to print invoice
           file_write(fread, ulist, fle)  # to call file write function to write changes to file
       respo = input("Do you want to exit?(yes/no): ") # to ask user whether you want to exit or not
print("Good Bye! See you again!") # to print message if response is no
