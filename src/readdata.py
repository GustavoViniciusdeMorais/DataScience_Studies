import pyspark

# spark session

spark = pyspark.sql.SparkSession.builder\
           .config('spark.jars.packages', 'org.xerial:sqlite-jdbc:3.34.0')\
           .getOrCreate()

df = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='my_table',
                 url='jdbc:sqlite:/../database.db')\
        .load()
