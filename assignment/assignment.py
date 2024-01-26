import pandas as pd

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel('employee_shifts.xlsx') 

# Print name and position of employees who worked 7 consecutive days
print("Employees who worked 7 consecutive days:")
for name, group in df.groupby('Name'):
    if (group['Date'].diff().dt.days == 1).all():
        print(name, group['Position'].iloc[0])

# Print name and position of employees with <10 and >1 hour between shifts 
print("\nEmployees with <10 and >1 hour between shifts:")
for name, group in df.groupby('Name'):
    gaps = group['Date'].diff().dt.total_seconds() / 3600
    if (gaps > 1).all() and (gaps < 10).all():
        print(name, group['Position'].iloc[0])
        
# Print name and position of employees who worked >14 hours in a single shift
print("\nEmployees who worked >14 hours in a single shift:")
for name, group in df.groupby('Name'):
    if (group['Hours'] > 14).any():
        print(name, group['Position'].iloc[0])