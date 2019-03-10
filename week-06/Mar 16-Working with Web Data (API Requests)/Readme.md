### Data Munging with Pandas ###

The following **concepts** has been coverd in this class:
* March-04-2019

* [x] Jupyter coding - Data handling
    * [-] How to run jupyter 
        ```
        # Go to folder
        $ cd UCBSAN201902DATA2/

        # run jupyter notebook to run local server
        $ jupyter notebook
        ```
    * [-] How to access jupyter notbook server
        ```
        # Open browser and goto local host
        Step 1 : open google chrome
        Step 1 : http://localhost:8888/
        ```
    * [-] How to run pandas in jupyter notbook
        ```
        # activate anaconda env using command promopt
        $ source activate PythonData

        # run jupyter notebook to run local server
        $ jupyter notebook

        # Open browser and goto local host
        Step 1 : http://localhost:8888/
        
        # Create a new python Notebook
        - click New and select python 3
        
        ```
    * [-] How to read a csv file as data frame in pandas
        ```
        # import pandas dependencies
        import pandas as pd

        # create a variable pointing a filename
        moviecsv = 'Resources/movie_scores.csv'

        # Read and display with pandas
        data_frame = pd.read_csv(moviecsv)
        data_frame.head()
        ```
    * [-] How to get column names from the pandas data frame
        ```
        # Read all column names
        data_frame.columns
        ```
    * [-] How to get a particular column data to another data frame
        ```
        # Read only particular column data to new variable
        data_imdb = data_frame[["FILM","IMDB","IMDB_norm","IMDB_norm_round","IMDB_user_vote_count"]]
        ```
    * [-] How to display first few lines of data frame
        ```
        # Read only particular column data to new variable
        data_imdb.head()
        ```
    * [-] How to set a column as index for the data frame
        - pandas dataframe by default create a new index column starting position from 0
        ```
        # give a column name to set column as index
        data_imdb.set_index("FILM")
        ```
* [x] Jupyter coding - Data Cleaning
    * [-] How to import numpy
        ```
        # use import statement
        import numpy as ps
        ```
* [x] Excercise
  * [-] Netflix
  * [-] Udemy
