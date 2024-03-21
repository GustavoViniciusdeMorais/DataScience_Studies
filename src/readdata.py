import pyspark

# spark session

spark = pyspark.sql.SparkSession.builder\
           .config('spark.jars.packages', 'org.xerial:sqlite-jdbc:3.34.0')\
           .getOrCreate()

products = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='products',
                 url='jdbc:sqlite:/work/database.db')\
        .load()

orders = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='orders',
                 url='jdbc:sqlite:/work/database.db')\
        .load()

customers = spark.read.format('jdbc') \
        .options(driver='org.sqlite.JDBC', dbtable='customers',
                 url='jdbc:sqlite:/work/database.db')\
        .load()

# Join orders with products using product_id
orders_products_df = orders.join(products, orders.product_id == products.product_id, "left")

# Join orders_products with customers using customer_id
customers_orders_products_df = orders_products_df.join(customers, orders_products_df.customer_id == customers.customer_id, "left")

# Show the resulting dataframe
customers_orders_products_df.show()

print('Dataframe loaded successfully')
print(df.show())