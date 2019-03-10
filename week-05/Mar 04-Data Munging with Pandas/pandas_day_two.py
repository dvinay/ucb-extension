# Python Pandas: using dataframes

# Day 2 Objectives
# ---
# - Understand how to navigate through DataFrames using Loc and Iloc
# - Understand how to filter and slice Pandas DataFrames
# - Understand how to create and access Pandas GroupBy objects
# - Understand how to sort DataFrames
# ---
# May help to review built-in methods from the Pandas website
# http://pandas.pydata.org/pandas-docs/version/0.24/reference/frame.html



#### LOC AND ILOC
# Set new index to last_name
df = df_original.set_index("last_name")
df.head()

# Grab the data contained within the "Berry" row and the "Phone Number" column
berry_phone = df.loc["Berry", "Phone Number"]
print("Using Loc: " + berry_phone)

also_berry_phone = df.iloc[1, 2]
print("Using Iloc: " + also_berry_phone)

# Grab the first five rows of data and the columns from "id" to "Phone Number"
# The problem with using "last_name" as the index is that the values are not unique so duplicates are returned
# If there are duplicates and loc[] is being used, Pandas will return an error
richardson_to_morales = df.loc[["Richardson", "Berry", "Hudson",
                                "Mcdonald", "Morales"], ["id", "first_name", "Phone Number"]]
print(richardson_to_morales)

# Using iloc[] will not find duplicates since a numeric index is always unique
also_richardson_to_morales = df.iloc[0:4, 0:3]
print(also_richardson_to_morales)

# The following will select all rows for columns `first_name` and `Phone Number`
df.loc[:, ["first_name", "Phone Number"]].head()

# the following logic test/conditional statement returns a series of boolean values
named_billy = df["first_name"] == "Billy"
named_billy.head()

# Loc and Iloc also allow for conditional statments to filter rows of data
# using Loc on the logic test above only returns rows where the result is True
only_billys = df.loc[df["first_name"] == "Billy", :]
print(only_billys)

# Multiple conditions can be set to narrow down or widen the filter
only_billy_and_peter = df.loc[(df["first_name"] == "Billy") | (
    df["first_name"] == "Peter"), :]
print(only_billy_and_peter)



#### CLEANING DATA
# Dependencies
import pandas as pd
import numpy as np

# Name of the CSV file
file = 'Resources/donors2008.csv'

# Preview of the DataFrame
# Note that FIELD8 is likely a meaningless column
df.head()

# Delete extraneous column
del df['FIELD8']
df.head()

# Identify incomplete rows
df.count()

# Drop all rows with missing information
df = df.dropna(how='any')

# Verify dropped rows
df.count()

# The Amount column is the wrong data type. It should be numeric.
df.dtypes

# Use pd.to_numeric() method to convert the datatype of the Amount column
df['Amount'] = pd.to_numeric(df['Amount'])

# Verify that the Amount column datatype has been made numeric
df['Amount'].dtype

# Display an overview of the Employers column
df['Employer'].value_counts()

# Clean up Employer category. Replace 'Self Employed' and 'Self' with 'Self-Employed'
df['Employer'] = df['Employer'].replace(
    {'Self Employed': 'Self-Employed', 'Self': 'Self-Employed'})

# Verify clean-up.
df['Employer'].value_counts()

df['Employer'] = df['Employer'].replace({'Not Employed': 'Unemployed'})
df['Employer'].value_counts()

# Display a statistical overview
# We can infer the maximum allowable individual contribution from 'max'
df.describe()



#### GROUP BY
# Create a reference the CSV file desired
csv_path = "Resources/ufoSightings.csv"

# Read the CSV into a Pandas DataFrame
ufo_df = pd.read_csv(csv_path)

# Print the first five rows of data to the screen
ufo_df.head()

# Remove the rows with missing data
clean_ufo_df = ufo_df.dropna(how="any")
clean_ufo_df.count()

# Converting the "duration (seconds)" column's values to numeric
clean_ufo_df["duration (seconds)"] = pd.to_numeric(
    clean_ufo_df["duration (seconds)"])

# Filter the data so that only those sightings in the US are in a DataFrame
usa_ufo_df = clean_ufo_df.loc[clean_ufo_df["country"] == "us", :]
usa_ufo_df.head()

# Count how many sightings have occured within each state
state_counts = usa_ufo_df["state"].value_counts()
state_counts.head()

# Using GroupBy in order to separate the data into fields according to "state" values
grouped_usa_df = usa_ufo_df.groupby(['state'])

# The object returned is a "GroupBy" object and cannot be viewed normally...
print(grouped_usa_df)

# In order to be visualized, a data function must be used...
grouped_usa_df.count().head(10)

# Since "duration (seconds)" was converted to a numeric time, it can now be summed up per state
state_duration = grouped_usa_df["duration (seconds)"].sum()
state_duration.head()

# Creating a new DataFrame using both duration and count
state_summary_table = pd.DataFrame({"Number of Sightings": state_counts,
                                    "Total Visit Time": state_duration})
state_summary_table.head()

# It is also possible to group a DataFrame by multiple columns
# This returns an object with multiple indexes, however, which can be harder to deal with
grouped_international_data = clean_ufo_df.groupby(['country', 'state'])

grouped_international_data.count().head(20)

# Converting a GroupBy object into a DataFrame
international_duration = pd.DataFrame(
    grouped_international_data["duration (seconds)"].sum())
international_duration.head(10)



#### SORTING
csv_path = "Resources/Happiness_2017.csv"
happiness_df = pd.read_csv(csv_path)
happiness_df.head()

# Sorting the DataFrame based on "Freedom" column
# Will sort from lowest to highest if no other parameter is passed
freedom_df = happiness_df.sort_values("Freedom")
freedom_df.head()

# To sort from highest to lowest, ascending=False must be passed in
freedom_df = happiness_df.sort_values("Freedom", ascending=False)
freedom_df.head()

# It is possible to sort based upon multiple columns
family_and_generosity = happiness_df.sort_values(
    ["Family", "Generosity"], ascending=False)
family_and_generosity.head()

# The index can be reset to provide index numbers based on the new rankings.
new_index = family_and_generosity.reset_index(drop=True)
new_index.head()

