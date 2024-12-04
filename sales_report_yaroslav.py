def validation(sales_data, top_n):
    if len(sales_data) < 1 or top_n < 1:
        return False, "Put valid data"
    for item in sales_data:
        if not isinstance(item.get("name"), str):
            return False, f"Missing name in {item}"
        if not isinstance(item.get("sales"), float) and not isinstance(item.get("sales"), int):
            return False, f"Missing sales in {item}"
    return True, "All good"

def sales_report(sales_data, top_n):
    #data validation
    validated = validation(sales_data, top_n)
    if validated[0]:
        top_performers = f'''Top {top_n} Sales Performers:\n'''
        sales_data.sort(reverse = True, key=lambda person: float(person.get("sales"))) #sorting list based on sales

        #filling output string
        for n, _ in enumerate(sales_data):
            if n >= top_n:
                break
            top_performers += f'{n+1}. {sales_data[n].get("name")} - ${sales_data[n].get("sales")}\n'
            
        return top_performers
    else:
        return validated[1]

#data for testing
sales_data = [
{"name": "Alice", "sales": 123},
{"name": "Bob", "sales": 2000.50},
{"name": "Charlie", "sales": 5000.00},
{"name": "David", "sales": 4200.00},
{"name": "Eva", "sales": 3000.00}
 ]
a = sales_report(sales_data, 2)
print(a)