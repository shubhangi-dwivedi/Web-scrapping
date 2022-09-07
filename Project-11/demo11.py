import pandas as pd

df = pd.read_csv('Jobs.txt')

df.to_excel('cretorial_jobs.xlsx', 'Sheet1')

