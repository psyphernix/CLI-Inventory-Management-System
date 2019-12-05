#---------------------------to generate invoice receipt-----------------------#
import datetime # to import inbuilt date and time module
def invoice(fr_list,ui_list):
    ''' function to create invoice receipt (bill) '''
    name = ui_list[0][3] # to assign customer's name stored in list to variable name
    hist = [["Product",'\t',"Quantity",'\t',"Price",'\t',"Total"]] # to create a list named hist   
    year = datetime.datetime.now().year   # to assign current year to variable year
    month = datetime.datetime.now().month # to assign current month to variable month
    day = datetime.datetime.now().day     # to assign current day to variable day
    hour = datetime.datetime.now().hour   # to assign current hour to variable hour
    minute = datetime.datetime.now().minute # to assign current minute to variable minute
    second = datetime.datetime.now().second # to assign current second to variable year
    date = ("%d/%02d/%02d %02d:%02d:%02d" %(year, month, day, hour, minute, second)) # to create full date-time in proper format
    total_items = 0 # to create variable for future use
    total_discount = 0
    for i in ui_list: # to iterate in user input list
        nist = [] # to create a empty list
        product = i[0] # to assign value at index 0 of i to product
        nist.append(product) # to append product to list
        nist.append('\t') # to append tab-spacing to list
        nist.append('\t')
        quantity = i[1] # to assign value at index 1 of i to quantity
        nist.append(quantity) # to append quantity to list
        nist.append('\t')
        nist.append('\t')
        for j in fr_list: # to iterate in file read list
            if product in j: # to assign value at index 1 of j to price if product is in j
                price = j[1]
        nist.append(price) # to append price to list
        nist.append('\t')
        total = quantity * price
        nist.append(total) # to append total to list
        hist.append(nist) # to append list named nist to another list named hist
        total_items = total_items + total
        discount= i[2] # to assign value at index 2 of i to variable discount
        discount_calculate = total * (discount / 100)
        total_discount = total_discount + discount_calculate
    total_after_discount = total_items - total_discount
    total_after_vat = total_after_discount + 0.13 * total_after_discount
    mist = [['\t',"Astro Electronics Limited"],['\t',"   Dhangadhi-8-Kailali"],['\t',"     Invoice Receipt"],["Date:", date],["Customer's Name:",name]]
    kist = [['\t','\t','\t',"  Discount: %.2f " % total_discount],['\t','\t','\t',"       VAT: 13 %"],['\t','\t','\t',"     Total: %.2f" % total_after_vat]]
    date_full = ("%d%02d%02d%02d%02d%02d" %(year, month, day, hour, minute, second))
    files = name + date_full + ".txt"
    with open(files, 'w') as file: # creating a new file in write mode
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in mist)
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in hist)
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in kist)          
    print("------------------------------------------------")   
    with open(files, 'r') as file: # reading created file
        for i in file: # iterating in file 
            print(i) # printing line i of file
    print("------------------------------------------------")
    print("Thank you for shopping from our shop!")
    print("Hoping to see you again!")
    return None # function has no return value
