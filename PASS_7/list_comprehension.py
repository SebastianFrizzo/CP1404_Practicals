products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = [product for product in products if product[2]]
print(on_sale_products)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(n) for n in almost_numbers]
print(numbers)

big_numbers = [n for n in numbers if n > 10]
print(big_numbers)

