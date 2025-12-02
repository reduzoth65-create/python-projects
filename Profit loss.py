actual_cost=float(input("please enter the Actual Product Price:"))
sale_amount=float(input("please enter th eSales Amount:"))

if(sale_amount > actual_cost):
    amount=sale_amount-actual_cost
    print("Total Profit={0}".format(amount))
else:
    print("NO PROFIT!!!!!!")