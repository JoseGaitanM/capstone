from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("example_spark_job").getOrCreate()

    # Read the input CSV file
    df = spark.read.csv("/opt/airflow/data/files/info.csv", header=True)

    # Perform some transformations
    df = df.filter("age >= 18").groupBy("gender").count()

    # Write the result to a new CSV file
    df.write.csv("/opt/airflow/data/files/result.csv", header=True)

    # Stop the SparkSession
    spark.stop()