import pandas as pd

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    # Basic data cleaning
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw_data.csv', 'data/processed_data.csv')

