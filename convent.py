import pandas as pd
import os
FILE = 'log_trend.csv'

def convert_to_tfb_series(data):
    data = data.set_index("date")
    melted_df = data.melt(value_name="data", var_name="cols", ignore_index=False)
    return melted_df.reset_index()[['date', 'data', 'cols']]

data = pd.read_csv(rf"./{FILE}")
data.rename(columns={data .columns[0]: 'date'},inplace=True)

print(data.head())
melted_df = convert_to_tfb_series(data)
print(melted_df.head())

DATASET_PATH = os.path.join("dataset", "forecasting")
if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)
melted_df.to_csv(os.path.join(DATASET_PATH,f'c_{FILE}'), index=False)
print(f'Converted file at {DATASET_PATH}: c_{FILE}')