### Real-World Data Parsing with Pandas ###

The following **concepts** has been coverd in this class:
* March-06-2019

* [x] Jupyter coding - Real world Data Parsing
    * [-] Merging
        * [-] Inner join merge
        ```
        # read data frame from first data frame
        raw_data_info = {
            "customer_id": [112, 403, 999, 543, 123],
            "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
            "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
        }
        info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
        info_pd

        # read data frame from second data frame
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
        ```
    * [-] Outer join merge
        ```
        # read data frame from first data frame
        raw_data_info = {
            "customer_id": [112, 403, 999, 543, 123],
            "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
            "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
        }
        info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
        info_pd

        # read data frame from second data frame
        raw_data_items = {
            "customer_id": [403, 112, 543, 999, 654],
            "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
            "cost": [3.00, 4.50, 600, 900, 150]
        }
        items_pd = pd.DataFrame(raw_data_items, columns=[
                                "customer_id", "item", "cost"])
        items_pd

        # Merge two dataframes using an inner join
        merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="outer")
        merge_table
        ```
    * [-] Left join merge
        ```
        # read data frame from first data frame
        raw_data_info = {
            "customer_id": [112, 403, 999, 543, 123],
            "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
            "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
        }
        info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
        info_pd

        # read data frame from second data frame
        raw_data_items = {
            "customer_id": [403, 112, 543, 999, 654],
            "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
            "cost": [3.00, 4.50, 600, 900, 150]
        }
        items_pd = pd.DataFrame(raw_data_items, columns=[
                                "customer_id", "item", "cost"])
        items_pd

        # Merge two dataframes using an inner join
        merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="left")
        merge_table
        ```
    * [-] right join merge
        ```
        # read data frame from first data frame
        raw_data_info = {
            "customer_id": [112, 403, 999, 543, 123],
            "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
            "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
        }
        info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
        info_pd

        # read data frame from second data frame
        raw_data_items = {
            "customer_id": [403, 112, 543, 999, 654],
            "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
            "cost": [3.00, 4.50, 600, 900, 150]
        }
        items_pd = pd.DataFrame(raw_data_items, columns=[
                                "customer_id", "item", "cost"])
        items_pd

        # Merge two dataframes using an inner join
        merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="right")
        merge_table
        ```
    * [-] BINNING
        * [-] Binning using Cut
        ```
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
        ```
* [x] Excercise
  * [-] Bitcoins and dash coins merge
  * [-] Udemy
