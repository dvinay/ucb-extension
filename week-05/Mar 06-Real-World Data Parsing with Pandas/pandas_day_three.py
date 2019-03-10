# Python Pandas: using dataframes

# Day 3 Objectives
# ---
# - Know how to merge DataFrames together whilst understanding the differences between inner, outer, left, and right merges.
# - Be able to slice data using the cut() method and create new values based upon a series of bins.
# - Feel more confident in your ability to fix Python/Pandas bugs within Jupyter Notebook.
# - Be able to use Google to explore additional Pandas functionality when necessary.
# ---



#### MERGING
raw_data_info = {
    "customer_id": [112, 403, 999, 543, 123],
    "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
    "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
}
info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
info_pd

# Create DataFrames
raw_data_items = {
    "customer_id": [403, 112, 543, 999, 654],
    "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
    "cost": [3.00, 4.50, 600, 900, 150]
}
items_pd = pd.DataFrame(raw_data_items, columns=[
                        "customer_id", "item", "cost"])
items_pd

# Merge two dataframes using an inner join
merge_table = pd.merge(info_pd, items_pd, on="customer_id")
merge_table

# Merge two dataframes using an outer join
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="outer")
merge_table

# Merge two dataframes using a left join
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="left")
merge_table

# Merge two dataframes using a right join
merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="right")
merge_table



#### BINNING
raw_data = {
    'Class': ['Oct', 'Oct', 'Jan', 'Jan', 'Oct', 'Jan'], 
    'Name': ["Cyndy", "Logan", "Laci", "Elmer", "Crystle", "Emmie"], 
    'Test Score': [90, 56, 72, 88, 98, 67]}
df = pd.DataFrame(raw_data)
df

# Create the bins in which Data will be held
# Bins are 0, 60, 70, 80, 90, 100
bins = [0, 60, 70, 80, 90, 100]

# Create the names for the four bins
group_names = ["F", "D", "C", "B", "A"]

df["Test Score Summary"] = pd.cut(df["Test Score"], bins, labels=group_names)
df

# Creating a group based off of the bins
df = df.groupby("Test Score Summary")
df.max()



#### MAPPING
# Mapping lets you format an entire DataFrame
file = "Resources/sample_data.csv"
file_df = pd.read_csv(file)
file_df.head()

# Use Map to format all the columns
file_df["avg_cost"] = file_df["avg_cost"].map("${:.2f}".format)
file_df["population"] = file_df["population"].map("{:,}".format)
file_df["other"] = file_df["other"].map("{:.2f}".format)
file_df.head()

# Mapping has changed the datatypes of the columns to strings
file_df.dtypes
