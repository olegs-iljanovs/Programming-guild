def generate_sales_report(sales_data, top_N):
    # sort by sales- desc order
    # use dict.get and setting default value to $0
    sorted_data = sorted(sales_data, key=lambda item: item.get("sales", 0), reverse=True)
    
    # top N performers
    report = []
    for index, performer in enumerate(sorted_data):
        if index < top_N: 
            name = performer.get("name", "Unknown user")
            sales = performer.get("sales", 0)
            report.append(name + ": $" + str(sales))
        else:
            break

    return report


# test function using data
top_N = 4

sales_data = [
    {"name": "Alice"},
    {"sales": 10000},
    {"name": "Bob"},
    {"name": "Charlie"},
    {"name": "David", "sales": 4200.00},
    {"name": "Eva", "sales": 3000.00}
]


report = generate_sales_report(sales_data, top_N)

# display top performers
print("Top {} Performers:".format(top_N))
for result in report:
    print(result)
