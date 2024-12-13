### SALES REPORT
ERROR_MESSAGE_INT = "You must enter a positive integer number"
ERROR_MESSAGE_FLOAT = "You must enter a positive number"

'''validates input for int or float and check if they are positive'''
def validate_number_input(input_message, input_type):
    input_num = None
    error_message = ERROR_MESSAGE_INT if input_type == 'int' else ERROR_MESSAGE_FLOAT
    while True:
        input_num = input(input_message)
        try:
            if input_type == 'float':
                input_num = float(input_num)
            elif input_type == 'int':
                input_num = int(input_num)
            
            if input_num <= 0:
                raise ValueError
        except ValueError:
            print(error_message)
            continue
        return input_num
    
def validate_name_input(input_message, sales_performers):
    while True:
        input_name = input(input_message)
        if any(input_name in dict.values() for dict in sales_performers):
            print("Entered name is already in performers list.")
            continue
        return input_name

'''prompts the user to enter sales performers data values and appends them to dict'''
def add_sales_info(sales_performers):
    data_quantity = validate_number_input("Enter how many data entries you want to add: ",
                                "int")
    for _ in range(data_quantity):
        sales_name = validate_name_input("Enter sales performer name (remember that it should be unique): ", sales_performers)

        sales_sum = validate_number_input("Enter sales performer revenue: ",
                                'float')
        sales_performers.append({"name":sales_name,"sales":float(sales_sum)})

'''sorts and displays the dict in the form of a table with top N positions'''
def show_performers_table(sales_performers):
    list_length = validate_number_input("Enter how many performers should be shown: ",
                                "int")
    
    sorted_data = sorted(sales_performers, reverse=True, key=lambda i: i['sales'])[:list_length]
    if list_length < len(sales_performers):
            print("Entered value bigger then actual list of permormers. Displaying all entries: ")
    print(f'Top {list_length} Sales Performers:')
    for position, key in enumerate(sorted_data): 
        print(str(position+1)+'. '+key['name']+" - $"+"{:.2f}".format(key['sales']))

sales_performers = []
add_sales_info(sales_performers)
show_performers_table(sales_performers)



