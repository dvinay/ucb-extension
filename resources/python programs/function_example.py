def test(temperature):
    if temperature > 90 and temperature < 100:
        return True
        
july_temperatures = [87, 85, 92, 79, 106]
# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if not test(temperature)]
print(hot_days)


candyList = [1, 5, 10]
candyCostType = ['in-expensive candy!' if cost < 5 else 'expensive candy' for cost in candyList] 
print(candyCostType)