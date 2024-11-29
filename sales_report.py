def sales_report(sales_data, top_n):
    #data validation
    if len(sales_data) < 1 or top_n < 1:
        return "Put valid data"
    for item in sales_data:
        if not isinstance(item.get("name"), str):
            return f"Missing name in {item}"
        if not isinstance(item.get("sales"), float):
            return f"Missing sales in {item}" 
        

    top_performers = f'''Top {top_n} Sales Performers:\n'''
    sales_data.sort(reverse = True, key=lambda person: person.get("sales", 0.00)) #sorting list based on sales

    #filling output string
    for n, _ in enumerate(sales_data):
        if n >= top_n:
            break
        top_performers += f'{n+1}. {sales_data[n].get("name", "EmptyName")} - ${sales_data[n].get("sales", 0.00)}\n'
        
    return top_performers

#data for testing
sales_data = [
{"name": "Alice", "sales": ""},
{"name": "Bob", "sales": 2000.50},
{"name": "Charlie", "sales": 5000.00},
{"name": "David", "sales": 4200.00},
{"name": "Eva", "sales": 3000.00}
 ]
a = sales_report(sales_data, 32)
print(a)