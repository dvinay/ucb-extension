july_temperatures = [87, 85, 92, 79, 106]
# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature > 90 and temperature <100]
print(hot_days)