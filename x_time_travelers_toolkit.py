import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import x_time_travelers_toolkit_custom_module

# Today's Date
current_date = dt.date.today()
current_time = dt.datetime.now()

print(f"Current date: {current_date}")
print(f"Current time: {current_time}")

# Random Year
start_year = 1500
end_year = 3000
random_year = randint(start_year, end_year)

# Random Destinations
destinations = ["Paris", "New York", "Tokyo", "Cairo", "Sydney", "Belgrade"]

random_destination = choice(destinations)

# Calculate the Time Travel Cost
base_cost = Decimal("1000.00")

current_year = dt.datetime.now().year
target_year = random_year

year_difference = abs(current_year - target_year)

cost_multiplier = Decimal(year_difference)

final_cost = base_cost + cost_multiplier

formatted_cost = f"{final_cost:.2f}"
#print(formatted_cost)

# Using the Custom Module
message = x_time_travelers_toolkit_custom_module.generate_time_travel_message(random_year, random_destination, formatted_cost)

print(message)











