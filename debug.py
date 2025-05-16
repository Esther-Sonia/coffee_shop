from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Esther")
customer2 = Customer("Joy")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

Order(customer1, coffee1, 4.0)
Order(customer2, coffee1, 5.0)
Order(customer1, coffee2, 4.5)


print("All tests passed!")
print(f"{customer1.name} ordered: {[coffee.name for coffee in customer1.coffees()]}")
print(f"{coffee1.name} was ordered by: {[customer.name for customer in coffee1.customers()]}")