def generate_sales_report(sales_data, top_n):
    sorted_data = sorted(sales_data, key = lambda item : item['sales'], reverse = True)
    top_of_performers = sorted_data[:top_n]
    report = "Top" + " " + str(top_n) + " " + "Sales Performers: "
    for value in top_of_performers:
        report += f"\n  {value['name']} - ${value['sales']:.2f}"
    return report
sales_data = [
    {"name": "Alice", "sales": 3500.75},
    {"name": "Bob", "sales": 2000.50},
    {"name": "Charlie", "sales": 5000.00},
    {"name": "David", "sales": 4200.00},
    {"name": "Eva", "sales": 3000.00}
]

top = generate_sales_report(sales_data, 3)
print(top)
