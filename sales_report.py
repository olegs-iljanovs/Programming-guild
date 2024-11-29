def sales_report(sales_data, top_n):
    top_performers = f'''Top {top_n} Sales Performers:\n'''
    sales_data.sort(reverse = True, key=lambda person: person.get("sales")) #sorting list based on sales

    #filling output string
    for n in range(top_n):
        top_performers += f"{n+1}. {sales_data[n].get("name")} - ${sales_data[n].get("sales")}\n"

    return top_performers

#data for testing

# sales_data = [
# {"name": "Alice", "sales": 3500.75},
# {"name": "Bob", "sales": 2000.50},
# {"name": "Charlie", "sales": 5000.00},
# {"name": "David", "sales": 4200.00},
# {"name": "Eva", "sales": 3000.00}
#  ]
# a = sales_report(sales_data, 3)
# print(a)