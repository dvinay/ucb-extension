# Matplotlib

# Day 2 Objectives
# ---
# - Feel comfortable creating plots using the DataFrame.plot() method
# - Understand the advantages and disadvantages of creating charts using the DataFrame.plot() method.
# - Be able to work your way through a complex data set using Pandas and then chart some visualizations based upon the cleaned DataFrame.
# ---
# Please reference/search the documentation
# URL to Matplotlib: https://matplotlib.org/examples/index.html



#### PANDAS PLOT

%matplotlib notebook

# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Using MatplotLib to Chart a DataFrame
# Load in csv
rain_df = pd.read_csv("../Resources/avg_rain_state.csv")
rain_df.head()

# Set x axis and tick locations
x_axis = np.arange(len(rain_df))
tick_locations = [value for value in x_axis]

# Create a list indicating where to write x labels and set figure size to adjust for space
plt.figure(figsize=(20,3))
plt.bar(x_axis, rain_df["Inches"], color='r', alpha=0.5, align="center")
plt.xticks(tick_locations, rain_df["State"], rotation="vertical")

# Set x and y limits
plt.xlim(-0.75, len(x_axis))
plt.ylim(0, max(rain_df["Inches"])+10)

# Set a Title and labels
plt.title("Average Rain per State")
plt.xlabel("State")
plt.ylabel("Average Amount of Rainfall in Inches")

# Save our graph and show the grap
plt.tight_layout()
plt.savefig("../Images/avg_state_rain.png")
plt.show()

### Using Pandas to Chart a DataFrame
# Filter the DataFrame down only to those columns to chart
state_and_inches = rain_df[["State","Inches"]]

# Set the index to be "State" so they will be used as labels
state_and_inches = state_and_inches.set_index("State")

state_and_inches.head()

# Use DataFrame.plot() in order to create a bar chart of the data
state_and_inches.plot(kind="bar", figsize=(20,3))

# Set a title for the chart
plt.title("Average Rain Per State")

plt.show()
plt.tight_layout()

# Pandas can also plot multiple columns if the DataFrame includes them
multi_plot = rain_df.plot(kind="bar", figsize=(20,5))

# PandasPlot.set_xticklabels() can be used to set the tick labels as well
multi_plot.set_xticklabels(rain_df["State"], rotation=45)

plt.show()
plt.tight_layout()




#### GROUP PLOTS
%matplotlib notebook

# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd

# Import our data into pandas from CSV
used_string = '../Resources/used_cars.csv'
used_car_df = pd.read_csv(used_string)

used_car_df

# Create a group based on the values in the 'maker' column
maker_group = used_car_df.groupby('maker')

# Count how many times each maker appears in our group
count_makers = maker_group['maker'].count()

count_makers

# Create a bar chart based off of the group series from before
count_chart = count_makers.plot(kind='bar')

# Set the xlabel and ylabel using class methods
count_chart.set_xlabel("Car Manufacturer")
count_chart.set_ylabel("Number of Cars")


plt.show()
plt.tight_layout()



#### PANDAS MULTI LINE
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read CSV
unemployed_data_one = pd.read_csv("../Resources/unemployment_2010-2011.csv")
unemployed_data_two = pd.read_csv("../Resources/unemployment_2012-2014.csv")

# Merge our two data frames together
combined_unemployed_data = pd.merge(unemployed_data_one, unemployed_data_two, on="Country Name")
combined_unemployed_data.head()

# Delete the duplicate 'Country Code' column and rename the first one back to 'Country Code'
del combined_unemployed_data['Country Code_y']
combined_unemployed_data = combined_unemployed_data.rename(columns={"Country Code_x":"Country Code"})
combined_unemployed_data.head()

# Set the 'Country Code' to be our index for easy referencing of rows
combined_unemployed_data = combined_unemployed_data.set_index("Country Code")

# Collect the mean unemployment rates for the world
average_unemployment = combined_unemployed_data.mean()

# Collect the years where data was collected
years = average_unemployment.keys()

# Plot the world average as a line chart
world_avg, = plt.plot(years, average_unemployment, color="blue", label="World Average" )

# Plot the unemployment values for a single country
country_one, = plt.plot(years, combined_unemployed_data.loc['USA',["2010","2011","2012","2013","2014"]], 
                        color="green",label=combined_unemployed_data.loc['USA',"Country Name"])

# Create a legend for our chart
plt.legend(handles=[world_avg, country_one], loc="best")

# Show the chart
plt.show()

average_unemployment.plot(label="World Average")
combined_unemployed_data.loc['USA', "2010":"2014"].plot(label="United States")
plt.legend()
plt.show()







