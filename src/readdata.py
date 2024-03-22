import pyspark

# spark session

spark = pyspark.sql.SparkSession.builder\
           .config('spark.jars.packages', 'org.xerial:sqlite-jdbc:3.34.0')\
           .getOrCreate()

products = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='products',
                 url='jdbc:sqlite:/work/database.db')\
        .load()
products = products.withColumnRenamed("name", "product_name")

orders = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='orders',
                 url='jdbc:sqlite:/work/database.db')\
        .load()
orders = orders.withColumnRenamed("customer_id", "order_customer_id")
orders = orders.withColumnRenamed("product_id", "order_product_id")

customers = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='customers',
                 url='jdbc:sqlite:/work/database.db')\
        .load()
customers = customers.withColumnRenamed("name", "customer_name")

# Join datasets
orders_products_df = orders.join(products, orders.order_product_id == products.product_id, "left")
customers_orders_products_df = orders_products_df.join(customers, orders_products_df.order_customer_id == customers.customer_id, "left")
customers_orders_products_df.show()

# Define the SQLite database URL
database_url = "jdbc:sqlite:/work/database.db"

# Define the properties for the JDBC connection
jdbc_properties = {
    "driver": "org.sqlite.JDBC",
    "url": database_url,
    "dbtable": "customers_orders"
}

# Write the DataFrame to the SQLite database
customers_orders_products_df.write \
    .jdbc(url=database_url, table="customers_orders", mode="overwrite", properties=jdbc_properties)

print('Dataframe loaded successfully')
print(df.show())