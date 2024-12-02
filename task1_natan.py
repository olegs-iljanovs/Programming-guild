from statistics import mean
# Sort function
def sort_criteria(e):
    return e["sales"]
# Main function for report generation of top performance
def generate_sales_report (data, n):
    data.sort(key=sort_criteria, reverse = True)
    performers = []
    if n > len(data):
        n = len(data)
    if data:
        for i in range(n):
            performers.append(data[i])
    return performers
# Valid data generation function
def generate_valid_data(data):
    valid_data = [obj for obj in data if "name" in obj]
    for entry in valid_data:
        if not "sales" in entry:
            entry["sales"] = average
        elif type(entry["sales"]) is not float:
            entry["sales"] = average
    return valid_data
# List of employee and performance
sales_data = [
    {"name": "Alice", "sales": 3500.75},
    {"name": "Bob", "sales": 2000.50},
    {"name": "Charlie", "sales": 5000.00},
    {"name": "David", "sales": 4200.00},
    {"name": "Eva", "sales": 3000.00},
    {"name": "Frank", "sales": 2800.00},
    {"name": "Grace", "sales": 3600.25},
    {"name": "Hannah", "sales": 4000.50},
    {"name": "Ian", "sales": 4500.75},
    {"name": "Judy", "sales": 3900.00},
    {"name": "Kevin", "sales": 2500.00},
    {"name": "Laura", "sales": "4700.00"},
    {"name": "Oleg"},
    {}
]
# Main code
try:
    # Statistical mean calculation
    sales = [obj["sales"] for obj in sales_data if "sales" in obj and type(obj["sales"]) is float]
    average = mean(sales)
    # Valid data generation
    valid_sales_data = generate_valid_data(sales_data) 

    # Calculate Top performers
    performers = generate_sales_report(valid_sales_data, 3)

    # Output
    if performers:
        for i in performers:
            print(f"Name is {i['name']}, Sales of the month: {i['sales']}")
    else:
        print("List is empty.")
except Exception as e:
    print("Отличная работа, Олег! Ошибка:", e)