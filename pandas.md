# Pandas DataFrame Tutorial: SQL-Like Queries in Python

Pandas is a powerful Python library for data manipulation and analysis. In this tutorial, we'll explore how to use Pandas to perform common SQL-like queries on a DataFrame. Specifically, we'll cover how to read a CSV file into a DataFrame and execute queries similar to `WHERE`, `GROUP BY`, `ORDER BY`, `LIKE`, and `HAVING`.

## Table of Contents
1. [Installing Pandas](#installing-pandas)
2. [Reading a CSV File](#reading-a-csv-file)
3. [Filtering Rows (`WHERE`)](#filtering-rows-where)
4. [Grouping Data (`GROUP BY`)](#grouping-data-group-by)
5. [Sorting Data (`ORDER BY`)](#sorting-data-order-by)
6. [String Matching (`LIKE`)](#string-matching-like)
7. [Filtering Groups (`HAVING`)](#filtering-groups-having)

## 1. Installing Pandas

First, ensure you have Pandas installed. You can install it using pip:

```bash
pip install pandas
```

## 2. Reading a CSV File

Let's start by reading a CSV file into a Pandas DataFrame. Suppose we have a CSV file named `data.csv`.

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())
```

## 3. Filtering Rows (`WHERE`)

To filter rows based on a condition, use the `query` method or boolean indexing. This is equivalent to the SQL `WHERE` clause.

```python
# Example: Select rows where 'age' is greater than 30
filtered_df = df[df['age'] > 30]

# Alternatively, using the query method
filtered_df = df.query('age > 30')

print(filtered_df)
```

## 4. Grouping Data (`GROUP BY`)

To group data and apply aggregate functions, use the `groupby` method. This is equivalent to the SQL `GROUP BY` clause.

```python
# Example: Group by 'department' and calculate the average 'salary'
grouped_df = df.groupby('department')['salary'].mean().reset_index()

print(grouped_df)
```

## 5. Sorting Data (`ORDER BY`)

To sort data, use the `sort_values` method. This is equivalent to the SQL `ORDER BY` clause.

```python
# Example: Sort the DataFrame by 'salary' in descending order
sorted_df = df.sort_values(by='salary', ascending=False)

print(sorted_df)
```

## 6. String Matching (`LIKE`)

To filter rows based on a string pattern, use the `str.contains` method. This is equivalent to the SQL `LIKE` clause.

```python
# Example: Select rows where the 'name' contains 'John'
like_df = df[df['name'].str.contains('John', case=False, na=False)]

print(like_df)
```

## 7. Filtering Groups (`HAVING`)

To filter grouped data, you can combine `groupby` with `filter`. This is equivalent to the SQL `HAVING` clause.

```python
# Example: Group by 'department' and filter groups with an average 'salary' greater than 50000
having_df = df.groupby('department').filter(lambda x: x['salary'].mean() > 50000)

print(having_df)
```

## Conclusion

In this tutorial, we've explored how to perform SQL-like queries in Pandas. You learned how to filter rows, group data, sort data, match strings, and filter grouped data. Pandas provides powerful tools to perform data manipulation and analysis in a way that's similar to SQL but integrated with Python's flexibility.
