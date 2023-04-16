from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

credentials_location = '/opt/google/credentials/final-project-382415-972971564a58.json'

gcs_bucket_raw_data = 'chicago-crime-raw-data'
gcs_bucket_transformed_data = 'chicago-crime-transformed-data'
conf = SparkConf()
conf.set("spark.jars", "/opt/bitnami/spark/jars/gcs-connector-latest-hadoop3.jar")
conf.set('spark.hadoop.google.cloud.auth.service.account.enable', 'true')
conf.set('spark.hadoop.google.cloud.auth.service.account.json.keyfile', credentials_location)
sc = SparkContext(conf=conf)

hadoop_conf = sc._jsc.hadoopConfiguration()

hadoop_conf.set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")

spark = SparkSession.builder \
    .config(conf=sc.getConf()) \
    .getOrCreate()

# df_pandas = pd.read_csv('/tmp/additional_data/crimes.csv')
# df = spark.createDataFrame(df_pandas)
df = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/tmp/additional_data/crimes.csv")
)

df.printSchema()
df.show()
df.repartition('Year').write.format('csv').partitionBy(['Year']).mode('overwrite').save(f'gs://{gcs_bucket_raw_data}/crime')

