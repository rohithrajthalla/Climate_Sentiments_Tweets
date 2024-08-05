from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(input_file, output_file):
    spark = SparkSession.builder.appName("SentimentAnalysis").getOrCreate()
    df = spark.read.csv(input_file, header=True, inferSchema=True)

    # Initialize VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Define a UDF for sentiment analysis
    def sentiment_score(text):
        if text:
            return float(analyzer.polarity_scores(text)['compound'])
        else:
            return 0.0

    sentiment_udf = udf(sentiment_score, FloatType())
    df = df.withColumn("sentiment", sentiment_udf(df['text']))

    df.write.csv(output_file, header=True)
    spark.stop()

if __name__ == "__main__":
    analyze_sentiment('data/processed_data.csv', 'data/sentiment_data.csv')
