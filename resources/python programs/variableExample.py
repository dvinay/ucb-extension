# create a name variable
name = "Frankfurter"
print("name : "+name)

# create a country variable
country = "US"
print("country : "+country)

# create a satisfied variable
satisfied = true
print(name + " is from the "+ country + " and happy with his job?" + " answer: "+ str(satisfied))

# create a age variable
age = 28 
print("age : "+ age)

# create a hourly_wage variable
hourly_wage = 15 
print("hourly_wage : "+ hourly_wage)

# create a daily_wage variable
daily_wage = hourly_wage * 8
print("daily_wage : "+ daily_wage)

# With an `f-string`, print the `daily_wage` and `satisfied` variables.
# this statement doesn't work with python 2
print(f"{name} is from the {country} and his age {age} and salary : {hourly_wage}")

