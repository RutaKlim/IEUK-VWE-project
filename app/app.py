import pandas as pd

temp_limit = 85
vib_mm_s_limit = 15

print('Checking for failing Turbines...')

df = pd.read_csv('app/data/telemetry_data.csv')
# search through csv file and print info of that row for whether the data is an anomoly
anomalies = df[(df['temperature_c'] > temp_limit) | (df['vibration_mm_s'] > vib_mm_s_limit)]

failed_turbines = anomalies['turbine_id'].value_counts()
failed_turbines = failed_turbines[failed_turbines > 1]

print('Failed turbines: ')
counter = 1
for (turbine_id, count) in failed_turbines.items():
   print(f"{counter}. {turbine_id}: failed {count} times")
   counter += 1
