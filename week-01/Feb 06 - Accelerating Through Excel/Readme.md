### Accelerating Through Excel ###

The following **concepts** has been coverd in this class:
* Feb-06-2019

* [x] Analytics Paradigm
    * [-] Decompose the Ask
    * [-] Identify Data Sources
    * [-] Define Strategy and Metrics
    * [-] Build Data Retrieval Plan
    * [-] Retrieve the Data
    * [-] Assemble and Clean
    * [-] Analyze for Trends
    * [-] Acknowledge Limitations
    * [-] Make the Call or Tell the Story
* [x] Formulas
    * [-] Functions
        ```
            = Sum(1,2,3)
            = Avg(F4:F6)
        ```
    * [-] Conditionals
        ```
            = IF(D2>5,TRUE,FALSE)
            = Avg(F4:F6)
        ```
    * [-] AND, OR, NOT
        ```
            = IF(AND(D2>5, D2<10),TRUE,FALSE)
        ```
    * [-] Lookups
        - Syntax
        ```
            =vlookup( <value>, <full table>, <column to retrieve>,<match parameter>)
        ```
        - Code
        ```
            =vlookup( “Asteroid 9”, Planets, 3, FALSE)
        ```
    
