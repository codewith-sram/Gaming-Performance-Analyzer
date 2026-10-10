# 🎮 Gaming Performance Analyzer

My 45-day Python, AI and Machine Learning learning project.

## Day 1

Today I started my project and learned the basics of the Python `print()` function.

## Goal

Build a Gaming Performance Analyzer using:

- Python
- Pandas
- NumPy
- Matplotlib
- Machine Learning

## Day 2

Today I learned about Python variables.

I created variables to store:
- Player name
- Game name
- Matches
- Kills
- Deaths
- Wins
- Losses

## Day 3 - User Input

Today I learned how to use the `input()` function in Python.

I made the Gaming Performance Analyzer interactive. Now the user can enter their own gaming information.

### Information collected

- Player Name
- Game Name
- Total Matches
- Total Kills
- Total Deaths
- Total Wins
- Total Losses
- Total Headshots

### Python concepts learned

- `input()`
- `int()`
- Variables
- User input and output

### Example

```text
Player Name: Ram
Game: Free Fire
Matches: 10
Kills: 85
Deaths: 40
Wins: 6
Losses: 4
Headshots: 25

## Day 4 - Gaming Performance Calculations

Today I learned how to perform calculations in Python.

### New features

- K/D Ratio calculation
- Win Rate calculation
- Handling zero deaths
- Rounding decimal values

### Formulas

K/D Ratio:

Kills / Deaths

Win Rate:

(Wins / Matches) × 100

### Example

```text
Kills: 85
Deaths: 40
K/D Ratio: 2.12

Wins: 6
Matches: 10
Win Rate: 60.0%


## Day 5 - Performance Rating

Today I learned how to use:

- `if`
- `elif`
- `else`
- Comparison operators
- `and`

### New Feature

The Gaming Performance Analyzer can now give the player a performance rating based on K/D ratio and win rate.

### Performance Levels

- Excellent
- Very Good
- Good
- Average
- Needs Improvement

### Example

```text
K/D Ratio: 2.12
Win Rate: 60.0%
Performance Rating: Very Good

## Day 6 - Loops and Multiple Matches

Today I learned about:

- `for` loops
- `range()`
- Repeating code
- Adding values using a loop
- Calculating averages

### New Feature

The Gaming Performance Analyzer can now collect statistics from multiple matches.

For each match, the user can enter:

- Kills
- Deaths

The program calculates:

- Total kills
- Total deaths
- Average kills

### Example

```text
Match 1: 8 kills
Match 2: 10 kills
Match 3: 6 kills
Match 4: 12 kills
Match 5: 9 kills

Total Kills: 45
Average Kills: 9.0

## Day 7 - Lists and Match Analysis

Today I learned about Python lists and how to store multiple match statistics.

### Match Data Stored

- Kills
- Deaths
- Headshots
- Assists

### New Features

The Gaming Performance Analyzer can now:

- Store individual match data
- Calculate total kills
- Calculate total deaths
- Calculate total headshots
- Calculate total assists
- Calculate average kills
- Calculate average deaths
- Calculate average headshots
- Calculate average assists
- Find highest kills
- Find lowest kills
- Find the best match
- Find the worst match

### Python Concepts Learned

- Lists
- `append()`
- `sum()`
- `max()`
- `min()`
- `index()`
- `for` loop

Day 7 completed successfully!

## Day 8 - Per-Match K/D Analysis

Today I improved the Gaming Performance Analyzer by adding K/D ratio analysis for every match.

### New Features

The Gaming Performance Analyzer can now:

- Calculate K/D ratio for each match
- Store K/D ratios in a list
- Find the highest K/D ratio
- Find the match with the highest K/D ratio
- Display K/D ratio for all matches

### Python Concepts Learned

- List indexing
- `max()`
- `index()`
- `append()`
- Creating and using multiple lists
- Calculating values inside a `for` loop

### Example

```text
Match 1 → K/D: 2.00
Match 2 → K/D: 1.50
Match 3 → K/D: 3.00

Highest K/D: 3.00
Best K/D Match: Match 3

## Day 9 - Python Functions

Today I learned how to use functions in Python.

### Functions Added

The Gaming Performance Analyzer now uses functions for:

- Calculating K/D ratio
- Calculating average statistics
- Finding highest values
- Finding lowest values

### Functions Created

```python
calculate_kd()
calculate_average()
find_highest()
find_lowest()

## Day 10 - Complete Performance Report

Today I combined the Python concepts learned during Days 1-9 to create a complete gaming performance report.

### New Features

The Gaming Performance Analyzer can now:

- Display player information
- Store multiple match statistics
- Calculate K/D for every match
- Calculate total statistics
- Calculate average statistics
- Calculate overall K/D
- Find the best match
- Find the worst match
- Find the highest K/D match
- Generate an overall performance rating

### Performance Ratings

The program gives a rating based on overall K/D:

- 3.0 or higher - Excellent
- 2.0 or higher - Very Good
- 1.5 or higher - Good
- 1.0 or higher - Average
- Below 1.0 - Needs Improvement

### Python Concepts Used

- Variables
- User input
- Conditions
- For loops
- Lists
- List methods
- Built-in functions
- Custom functions
- Parameters
- Return values
- Basic calculations

### Project Progress

Days 1-10 completed successfully! 

The project is now ready to move from Python basics toward data handling with NumPy and Pandas.

## Day 11 - Introduction to NumPy

Today I started learning NumPy for data analysis.

### What I Learned

- What NumPy is
- How to install NumPy
- NumPy arrays
- Converting Python lists into NumPy arrays
- Calculating totals using NumPy
- Calculating averages using NumPy
- Finding maximum values
- Finding minimum values

### NumPy Functions Used

```python
np.array()
np.sum()
np.mean()
np.max()
np.min()

## Day 12 - NumPy Match Analysis

Today I continued learning NumPy and used NumPy arrays for match-by-match gaming analysis.

### New Features

The Gaming Performance Analyzer can now:

- Calculate K/D ratio using NumPy arrays
- Calculate average K/D
- Find highest K/D
- Find lowest K/D
- Find the best K/D match
- Find the worst K/D match
- Round K/D values using NumPy

### New NumPy Functions

```python
np.argmax()
np.argmin()
np.round()

## Day 13 - NumPy Statistical Analysis

Today I learned more NumPy statistical functions and added statistical analysis to the Gaming Performance Analyzer.

### New Features

The analyzer can now:

- Calculate median kills
- Calculate median K/D
- Calculate kill standard deviation
- Analyze player consistency
- Compare average and median performance

### New NumPy Functions

```python
np.median()
np.std()

## Day 14 - NumPy Performance Comparison

Today I learned how to compare NumPy arrays with values and analyze individual match performance.

### New Features

The Gaming Performance Analyzer can now:

- Find matches above average kills
- Find matches below average kills
- Count matches above average kills
- Count matches below average kills
- Find matches above average K/D
- Count matches above average K/D
- Compare individual matches with overall performance

### New Concepts

- Boolean arrays
- Array comparison
- `True` and `False` values
- Counting conditions using `np.sum()`

### Example

If the average kills are 13:

```text
Kills: [12, 15, 8, 20, 10]

Above Average:
[False, True, False, True, False]

Matches Above Average: 2

## Day 15 - Introduction to Pandas

Today I started learning Pandas for data analysis.

### What I Learned

- What Pandas is
- How to install Pandas
- What a DataFrame is
- How to create a DataFrame
- How to add a new column
- How to select a column
- How to display gaming data as a table

### Pandas Functions and Concepts

```python
pd.DataFrame()
df["column"]

## Day 16 - Pandas Data Analysis

Today I learned how to analyze a Pandas DataFrame.

### New Functions and Concepts

- `df.head()`
- `df.tail()`
- `df.info()`
- `df.describe()`
- `df.shape`

### What They Do

`head()` displays the first rows of the dataset.

`tail()` displays the last rows of the dataset.

`info()` provides information about columns and data types.

`describe()` provides statistical information about numerical data.

`shape` tells us the number of rows and columns.

### Gaming Data Analysis

The Gaming Performance Analyzer can now inspect the structure and statistics of the gaming dataset.

Day 16 completed successfully! 

## Day 17 - Pandas Filtering and Sorting

Today I learned how to filter and sort gaming data using Pandas.

### New Features

The Gaming Performance Analyzer can now:

- Find matches with 15 or more kills
- Find matches with 5 or fewer deaths
- Find matches with 2.5 or higher K/D
- Sort matches by kills
- Sort matches by K/D
- Find the best K/D match

### Pandas Concepts Learned

```python
df[df["Kills"] >= 15]
df[df["Deaths"] <= 5]
df[df["K/D"] >= 2.5]
df.sort_values()
df.loc[]
df.idxmax()

## Day 19 - Pandas Data Cleaning

Today I learned how to clean gaming data using Pandas.

### New Features

- Detect missing values
- Fill missing values using the median
- Detect duplicate rows
- Remove exact duplicate rows
- Reset DataFrame indexes
- Calculate K/D after cleaning data

### Pandas Functions Learned

- `isnull()`
- `fillna()`
- `median()`
- `duplicated()`
- `drop_duplicates()`
- `reset_index()`

### What I Learned

Data cleaning improves the quality of a dataset before performing data analysis or machine learning.

Day 19 completed successfully! 


## Day 20 - Exporting Gaming Statistics to CSV

Today I learned how to save and load gaming statistics using Pandas.

### New Features

- Export gaming data to a CSV file
- Read CSV files using Pandas
- Check whether a file exists
- Calculate total and average kills
- Display a summary report

### Functions Learned

- `to_csv()`
- `read_csv()`
- `os.path.exists()`
- `sum()`
- `mean()`

### What I Learned

CSV files help store gaming data so it can be reused for future analysis and visualization.

Day 20 completed successfully!
