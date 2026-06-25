import pandas as pd

temp_limit_in_C = 85.0
vib_limit_in_mmps = 15.0

print('STARTING: finding failing turbines...')

try:
   df = pd.read_csv('app/data/telemetry_data.csv')
except FileNotFoundError:
   print("File not found")

# store turbine results with anomalies
turbines = df.groupby("turbine_id").agg({"temperature_c": "mean", "vibration_mm_s": "max"}).reset_index()
# print(turbines)

failing_turbines = turbines[
   ((turbines["temperature_c"] > temp_limit_in_C) | (turbines["vibration_mm_s"] > vib_limit_in_mmps))
]

# print messages of which turbines failed
print('Failed turbines: ')
for index, row in failing_turbines.iterrows():
   print(
      f"-> Turbine: {row['turbine_id']} | Avg Temp: {row['temperature_c']:.1f}C | Max vib: {row['vibration_mm_s']:.1f} mm/s"
   )

# old ver:
# import pandas as pd

# temp_limit_in_C = 85
# vib_limit_in_mmps = 15

# print('Checking for failing Turbines...')

# df = pd.read_csv('app/data/telemetry_data.csv')
# # search through csv file and print info of that row for whether the data is an anomoly
# anomalies = df[(df['temperature_c'] > temp_limit_in_C) | (df['vibration_mm_s'] > vib_limit_in_mmps)]

# failed_turbines = anomalies['turbine_id'].value_counts()
# failed_turbines = failed_turbines[failed_turbines > 1]

# print('Failed turbines: ')
# counter = 1
# for (turbine_id, count) in failed_turbines.items():
#    print(f"{counter}. {turbine_id}: failed {count} times")
#    counter += 1
