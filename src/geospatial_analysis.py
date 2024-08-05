import pandas as pd

def geospatial_analysis(input_file, output_file):
    df = pd.read_csv(input_file)
    # Perform geospatial analysis
    df['region'] = df.apply(lambda row: 'North' if row['lat'] > 0 else 'South', axis=1)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    geospatial_analysis('data/processed_data.csv', 'data/geospatial_data.csv')
