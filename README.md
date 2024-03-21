# Data Science Studies

### Project setup
```sh
sudo docker-compose up -d --build
sudo touch database.db
sqlite3 database.db
.read database.sql
.tables

python3 src/readdata.py
```

### Start Spark
```sh
spark/bin/pyspark
```

# Introduction to Apache Spark

Apache Spark is an open-source distributed computing system that provides an interface for programming entire clusters with 
implicit data parallelism and fault tolerance. It's designed for fast computation and works with large-scale data processing.

## Install
Apache Spark is a folder with all the code needed, and requires java. <br>
Download java jdk deb package from oracle and install it with ` sudo dpkg -i package.deb `.
Add the JAVA_HOME path to the /etc/environment file as follows: <br>
`JAVA_HOME="/usr/lib/jvm/jdk-21-oracle-x64"`<br>
Download spark from https://spark.apache.org/downloads.html <br>
Unzip, rename to spark ` mv spark-2-hadoop-2 spark`, and execute the command ` spark/bin/pyspark `

## Configuration

To configure Apache Spark, you typically need to set up environment variables such as `SPARK_HOME` and `PYTHONPATH` to point to 
the Spark installation directory. Additionally, you might need to adjust configuration settings in the `spark-defaults.conf` file 
located in the Spark configuration directory.
[Config Details](./ConfigDetails.md)

## Example: Reading Data from SQLite Database into PySpark SQL Session

Here's a simple example of how to read data from a SQLite database into a PySpark SQL session:

## Tip
Code with the python terminal for convenience.<br>
<img src="./imgs/pyspark.png" width="700" height="600">

### Python Code

```python
# Import required libraries
import pyspark.sql as sparksql

# Create a SparkSession
spark = sparksql.SparkSession.builder \
    .appName("SQLite to Spark") \
    .config('spark.jars.packages', 'org.xerial:sqlite-jdbc:3.34.0') \
    .getOrCreate()

# Define the SQLite database file path
sqlite_db_path = "path/to/your/database.sqlite"

# Define the JDBC connection URL for SQLite
jdbc_url = f"jdbc:sqlite:{sqlite_db_path}"

# Define the table name
table_name = "your_table_name"

# Read data from the SQLite table into a DataFrame
df = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", table_name) \
    .load()

# Show the DataFrame
df.show()
```
