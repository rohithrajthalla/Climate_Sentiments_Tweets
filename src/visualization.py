import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(input_file):
    df = pd.read_csv(input_file)
    # Create visualizations
    plt.figure(figsize=(10, 6))
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Analysis')
    plt.show()

if __name__ == "__main__":
    create_visualizations('data/sentiment_data.csv')
