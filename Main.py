from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from Customer import Customer
from Restaurant import Restaurant
from Review import Review

# Create the database engine and session
engine = create_engine('sqlite:///sweetdishes.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables
Base.metadata.create_all(engine)

# Example usage
kelly = Customer('Kelly', 'Mwiti')
jay = Customer('Jay', 'M')
restaurant = Restaurant('Nexgen food bazzare')

review1 = Review(4, kelly, restaurant)
review2 = Review(5, kelly, restaurant)

session.add(kelly)
session.add(jay)
session.add(restaurant)
session.add(review1)
session.add(review2)
session.commit()

all_customers = session.query(Customer).all()
all_restaurants = session.query(Restaurant).all()


print('All Customers:')
for customer in all_customers:
    print(customer.full_name())

print('\nAll Restaurants:')
for restaurant in all_restaurants:
    print(restaurant.name)

# update
for customer in all_customers:
    if customer.id == 1:
        customer.first_name = "Ronny"
# session.commit()

for restaurant in all_restaurants:
    if restaurant.id == 1:
        restaurant.name = "Sweet Dishes"
session.commit()

# delete
customers_to_delete = session.query(Customer).filter(Customer.first_name == 'Ronny').all()
for customer in customers_to_delete:
    session.delete(customer)
session.commit()

session.close()
