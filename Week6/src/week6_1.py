# import
import os
import requests
import pyspark
from pyspark.sql import Row
from pyspark.sql.types import DateType
# setting spark
myConf = pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf = myConf).getOrCreate()
spark.sql('set spark.sql.legacy.timeParserPolicy=LEGACY')
# get json
r = requests.get('https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json')
wc = r.json()
wcDf = spark.createDataFrame(Row(**x) for x in wc)
# preprocessing
wcDfCasted = wcDf.withColumn('date3', wcDf['DateOfBirth'].cast(DateType()))
wcDfCasted = wcDfCasted.withColumn('NumberUnt', wcDf['Number'].cast('integer'))

print(wcDfCasted.take(1))
