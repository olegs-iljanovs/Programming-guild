#V.Krjukovs Sales report
sales_data = []

#menu
while True:
    name = input("Enter name: ")
    sales = input("Enter sales: ")

    #input validation
    try:
        sales = float(sales)
    except:
        print("input error, please enter number in sales field")
        continue
    
    #populate data
    sales_data.append({"name":name,"sales":float(sales)})

    #exit from menu
    if input("Press enter to finish, or any other symbol to continue: ") == "": break

top_n = int(input("Enter the number of top performers to include in the report: "))

#calculate top_n
sorted_top_sales = sorted(sales_data, reverse = True, key = lambda person: person["sales"])[:top_n]

#output
print("Top {} Sales Performers:".format(top_n))
for position, i in enumerate(sorted_top_sales): print(str(position+1)+'. '+i['name']+" - $"+str(i['sales']))