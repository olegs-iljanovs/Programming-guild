### SALES REPORT
sales_performers = []
ERROR_MESSAGE_INT = "You must enter a positive integer number"
ERROR_MESSAGE_FLOAT = "You must enter a positive number"

#validates input for int or float and check if they are positive
def validate_input(input_message, error_message, input_type):
    input_num = None
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

#prompts the user to enter sales performers data values and appends them to dict
def add_sales_info():
    data_quantity = validate_input("Enter how many data entries you want to add: ",
                                ERROR_MESSAGE_INT,
                                "int")
    for _ in range(data_quantity):
        sales_name = input("Enter sales performer name: ")
        sales_sum = validate_input("Enter sales performer revenue: ",
                                ERROR_MESSAGE_FLOAT,
                                'float')
        sales_performers.append({"name":sales_name,"sales":float(sales_sum)})

#sorts and displays the dict in the form of a table with top N positions
def show_performers_table():
    list_length = validate_input("Enter how many performers should be shown: ",
                                ERROR_MESSAGE_INT,
                                "int")
    
    sorted_data = sorted(sales_performers, reverse=True, key=lambda i: i['sales'])[:list_length]

    print(f'Top {list_length} Sales Performers:')
    for position, key in enumerate(sorted_data): 
        print(str(position+1)+'. '+key['name']+" - $"+str(key['sales']))

add_sales_info()
show_performers_table()



