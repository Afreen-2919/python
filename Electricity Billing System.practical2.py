# Electricity Billing System 
def calculate_bill(units): 
    bill = 0 
    if units <= 100: 
        bill = units * 1.50 
    elif units <= 200: 
        bill = 100 * 1.50 + (units - 100) * 2.50 
    elif units <= 500: 
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00 
    else: 
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00 
    return bill 
n = int(input("Enter number of customers: ")) 
for i in range(1, n + 1): 
    print(f"\nCustomer {i}") 
    name = input("Enter customer name: ") 
    units = float(input("Enter units consumed: ")) 
    bill = calculate_bill(units)
    print("Customer Name :", name) 
    print("Units         :", units) 
    print("Bill Amount   : Rs.", round(bill, 2)) 
    if units > 500:
        print("WARNING: High electricity usage!")

'''
sample output

Enter number of customers: 4

Customer 1
Enter customer name: Abhi
Enter units consumed: 60
Customer Name : Abhi
Units         : 60.0
Bill Amount   : Rs. 90.0

Customer 2
Enter customer name: Banu
Enter units consumed: 200
Customer Name : Banu
Units         : 200.0
Bill Amount   : Rs. 400.0

Customer 3
Enter customer name: Cales
Enter units consumed: 450
Customer Name : Cales
Units         : 450.0
Bill Amount   : Rs. 1400.0

Customer 4
Enter customer name: Danila
Enter units consumed: 650
Customer Name : Danila
Units         : 650.0
Bill Amount   : Rs. 2500.0
WARNING: High electricity usage!

'''