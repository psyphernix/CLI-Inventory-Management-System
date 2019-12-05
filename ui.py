#------------------------------to take user input-----------------------------#
def user_input(fr_list):
    ''' function to take user input'''
    list_out = [] # creating a empty list
    wish = input("Does customer want to buy anything?(yes/no): ")
    enter = "yes" # assigning "yes" to enter for future use
    n = 0 # setting counter n
    check = [] # creating empty list to store customer's buying item's name
    if wish == "yes": # do given operations if wish equals to "yes"
        while enter == "yes": # iterate through given operations when enter equals "yes"
            list_input = [] # creating empty list 
            res = False # assigning False value to variable res for exception handling purpose
            while res == False: # iterate through given operations as long as res equals False
                try: # do given operations while res equals False
                    product = input("Enter the Product Name: ") # asking user to enter product name
                    for item in fr_list: # iterating in file read list
                        if item[0] == product and item[2] == 0: # print following if product is out of stock
                            print("Sorry! %s is out of stock." % product)
                        elif product in check and product in item: # print following message if product is customer's buying list
                            print("Sorry! %s has already bought %s." % (name_customer, product))
                        elif product in item: # assign True to res if product is available 
                            res = True
                except:
                    print("Product not available!") # message to print if all conditions in try failed
            list_input.append(product) # append product to list named list_input
            res1 = False # assigning False value to variable res1 for exception handling purpose
            while res1 == False: # iterate through given operations as long as res1 equals False
                try: # do given operations while res1 equals False
                    quantity = int(input("Enter the Quantity: ")) # asking user to input quantity and coverting to interger
                    for i in fr_list: # iterating in file read list
                        if i[0] == product:  # do following if value at index 0 of i is equal to product                        
                            if quantity < 1 or quantity > i[2]: # message to display if quantity entered is less than 1 and greater than quantity available
                                print("Quantity should be 1 to available quantity. Please enter properly!")
                            else: # assign True to res1 if above if conditions fail
                                res1 = True
                except:
                    print("Invalid Input!") # message to print if all conditions in try failed
            list_input.append(quantity) # append quantity to list named list_input
            res2 = False # assigning False value to variable res2 for exception handling purpose
            while res2 == False: # iterate through given operations as long as res2 equals False
                try: # do given operations while res2 equals False
                    discount_amount = int(input("Enter the Discount Amount in Percentage: ")) # asking user to input discount in percent and coverting to interger
                    if discount_amount < 0 or discount_amount > 100: # message to display if discount amount is negative and greater than 100
                        print("Percentage should be 0 to 100. Please enter properly!")
                    else: # assign True to res2 if above if conditons fail
                        res2 = True
                except:
                    print("Invalid Input!") # message to print if all conditions in try failed
            list_input.append(discount_amount) # append discount amount to list named list_input
            if n == 0:  # ask user to enter his/her name if when n equals 0            
                name_customer = input("Enter the customer's name: ")
            list_input.append(name_customer) # append customer's name to list named list_input
            list_out.append(list_input)  # append list named list_input to another list named list_out to create 2D list
            enter = input("Does %s want to buy another product?(yes/no): " % name_customer) # to ask customer if he/she wants to buy another product
            if enter == "yes": # do following operations if user want to buy another product
                check.append(product) # appending product to list named check
                n = n + 1 # increase n value by 1
        else:
            return list_out # to return list named list_out from function 
    else:
        return False # if wish is not equal to "yes", return False from function
    
