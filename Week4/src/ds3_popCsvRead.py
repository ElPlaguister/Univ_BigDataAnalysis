import os
import pyspark

def doIt():
    print('----------Result----------')
    popDf = spark\
    .read.option('charset', 'euc-kr')\
    .option('header', 'true')\
    .csv(os.path.join('data', 'first.csv'))

    popDf.show(5)
    
    agedDf = spark\
    .read.option('charset', 'euc-kr')\
    .option('header', 'true')\
    .csv(os.path.join('data', 'second.csv'))
    
    agedDf.show(5)
    
if __name__ == '__main__':
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).getOrCreate()
    doIt()
    spark.stop()
