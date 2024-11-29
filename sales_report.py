def sales_report(sales_data, top_n):
    top_performers = f'''Top {top_n} Sales Performers:\n'''
    try:
        sales_data.sort(reverse = True, key=lambda person: person.get("sales")) #sorting list based on sales

        #filling output string
        for n, _ in enumerate(sales_data):
            if n >= top_n:
                break
            top_performers += f'{n+1}. {sales_data[n].get("name")} - ${sales_data[n].get("sales")}\n'
            
        return top_performers
    except TypeError:
        return("Sales field should be float")
    except:
        return("Something went wrong. Check data and try again")


#data for testing
sales_data = [
{"name": "Alice", "sales": 3500.00},
{"name": "Bob", "sales": 2000.50},
{"name": "Charlie", "sales": 5000.00},
{"name": "David", "sales": 4200.00},
{"name": "Eva", "sales": 3000.00}
 ]
a = sales_report(sales_data, 3)
print(a)