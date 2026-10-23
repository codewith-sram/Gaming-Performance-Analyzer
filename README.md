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


## Day 21 - Introduction to Matplotlib

Today I learned how to visualize gaming statistics using Matplotlib.

### New Features
- Read gaming data from a CSV file
- Create a bar chart of kills per match
- Add a chart title and axis labels
- Display grid lines and a legend
- Save the chart as a PNG image

### Functions Learned
- `plt.figure()`
- `plt.bar()`
- `plt.title()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.savefig()`
- `plt.show()`

### What I Learned
Data visualization makes gaming performance easier to understand by presenting statistics as charts.

Day 21 completed successfully


## Day 22 - Gaming Performance Trend

Today I learned how to visualize gaming performance using a line chart.

### New Features
- Display kills across matches
- Show performance trends
- Add markers to data points
- Display average kills as a reference line
- Save the line chart as a PNG image

### Functions Learned
- `plt.plot()`
- `plt.axhline()`
- `plt.xticks()`
- `plt.grid()`
- `plt.savefig()`

### What I Learned
Line charts help track changes in gaming performance over multiple matches.

Day 22 completed successfully!


## Day 23 - Comparing Gaming Statistics

Today I learned how to compare multiple gaming statistics using Matplotlib.

### New Features
- Compare kills, deaths, and assists
- Display three lines on one chart
- Add different markers for each statistic
- Calculate total kills, deaths, and assists
- Save the chart as a PNG image

### Functions Learned
- `plt.plot()`
- `plt.legend()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.savefig()`

### What I Learned
Multi-line charts make it easier to compare different gaming statistics across matches.

Day 23 completed successfully!


## Day 24 - Gaming Statistics Pie Chart

Today I learned how to visualize gaming statistics using a pie chart.

### New Features
- Calculate total kills, deaths, and assists
- Display the distribution of gaming statistics
- Show percentage labels on the pie chart
- Save the chart as a PNG image

### Functions Learned
- `plt.pie()`
- `plt.axis()`
- `plt.title()`
- `plt.savefig()`

### What I Learned
Pie charts help visualize the relative proportions of different values in a dataset.

Day 24 completed successfully!


## Day 25 - Gaming Performance Dashboard

Today I combined multiple visualizations into one dashboard.

### Dashboard Features
- Total kills, deaths, and assists
- Average kills per match
- Bar chart for kills
- Line chart for match performance
- Pie chart for statistics distribution
- Performance summary panel

### New Concepts Learned
- `plt.subplots()`
- Multiple chart panels
- `fig.suptitle()`
- `axes[]`
- `plt.tight_layout()`

### What I Learned
A dashboard combines important statistics and charts into one view, making gaming performance easier to understand.

Day 25 completed successfully!


## Day 26 - Introduction to Machine Learning

Today I created my first machine learning model for the Gaming Performance Analyzer.

### New Features
- Load gaming data from CSV
- Train a Linear Regression model
- Predict kills for the next match
- Visualize actual kills and the regression line
- Save the prediction chart

### Library Learned
- `scikit-learn`

### Functions Learned
- `LinearRegression()`
- `fit()`
- `predict()`

### What I Learned
Machine learning models learn patterns from data and use those patterns to make predictions.

Day 26 completed successfully!



## Day 27 - Training and Testing a Model

Today I learned how to split data and evaluate a Linear Regression model.

### New Features
- Split data into training and testing sets
- Train a Linear Regression model
- Compare actual and predicted kills
- Calculate prediction errors
- Save testing results to CSV
- Create a model testing chart

### Functions Learned
- `train_test_split()`
- `mean_absolute_error()`
- `mean_squared_error()`
- `model.fit()`
- `model.predict()`

### What I Learned
Testing a model on data that was not used for training helps measure its prediction performance.

Day 27 completed successfully!



## Day 28 - Comparing Machine Learning Models

Today I compared Linear Regression and Decision Tree Regression.

### New Features
- Train two machine learning models
- Evaluate models using MAE and RMSE
- Compare prediction errors
- Save results to a CSV file
- Visualize model errors using a bar chart

### Libraries and Functions Learned
- `DecisionTreeRegressor()`
- `LinearRegression()`
- `mean_absolute_error()`
- `mean_squared_error()`
- `idxmin()`

### What I Learned
Comparing models helps us understand which model makes smaller errors on a given test dataset.

Day 28 completed successfully!


## Day 29 - Feature Engineering

Today I learned how to create useful features from gaming statistics.

### New Features
- Calculate K/D ratio
- Calculate headshot rate
- Prepare gaming data for machine learning
- Train a Random Forest regression model
- Evaluate predictions using MAE and RMSE
- Save prediction results and a chart

### Functions and Concepts Learned
- Feature engineering
- `RandomForestRegressor()`
- `model.fit()`
- `model.predict()`
- `mean_absolute_error()`
- `mean_squared_error()`

### What I Learned
Feature engineering transforms raw data into useful information for machine learning. Features must be chosen carefully to avoid leaking the answer into the model.

Day 29 completed successfully!

## Day 30 - Feature Importance

Today I learned how to examine feature importance in a Random Forest model.

### New Features
- Train a Random Forest regression model
- Evaluate predictions using MAE
- Calculate feature-importance scores
- Rank gaming features
- Export importance scores to CSV
- Visualize feature importance using a bar chart

### Functions and Concepts Learned
- `RandomForestRegressor()`
- `feature_importances_`
- `sort_values()`
- `mean_absolute_error()`
- `plt.bar()`

### What I Learned
Feature importance helps identify which input features a trained model relies on most when making predictions.

Day 30 completed successfully!

## Day 31 - K-Fold Cross-Validation

Today I learned how to evaluate a machine learning model using cross-validation.

### New Features
- Evaluate a Random Forest model across five folds
- Calculate MAE for each fold
- Calculate average MAE and standard deviation
- Export cross-validation results to CSV
- Visualize evaluation results using a bar chart

### Functions and Concepts Learned
- `KFold()`
- `cross_val_score()`
- `neg_mean_absolute_error`
- Mean Absolute Error (MAE)
- Standard deviation

### What I Learned
Cross-validation evaluates a model across multiple data splits and helps us understand how its prediction errors vary.

Day 31 completed successfully!


## Day 32 - Hyperparameter Tuning with Grid Search

Today I learned how to tune a Random Forest model using Grid Search.

### New Features
- Test multiple model configurations
- Use five-fold cross-validation
- Find the best model settings
- Compare cross-validation errors
- Export Grid Search results to CSV
- Visualize model performance

### Functions and Concepts Learned
- `GridSearchCV()`
- `param_grid`
- `best_params_`
- `best_score_`
- `n_estimators`
- `max_depth`

### What I Learned
Hyperparameter tuning helps compare model settings to find a configuration with better cross-validation performance.

Day 32 completed successfully!



## Day 33 - Saving and Loading a Machine Learning Model

Today I learned how to save and reload a trained Random Forest model.

### New Features
- Train a Random Forest model using Grid Search
- Save the trained model with joblib
- Load the saved model
- Predict kills from new match statistics
- Save predictions to a CSV file

### Functions Learned
- `joblib.dump()`
- `joblib.load()`
- `model.predict()`
- `pd.DataFrame()`
- `to_csv()`

### What I Learned
Saving a trained model allows it to be reused later without having to rebuild it from scratch.

Day 33 completed successfully!

