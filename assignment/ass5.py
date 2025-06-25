#ques1
import pandas as pd
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
print(s)

print("\n--------------from tuple------")
data2 = (100, 200, 300)
s2 = pd.Series(data2)
print(s2)

print("\n--------------printing elements-----")

print(s['b'])
print(s2[1])
print(s2[0:])

#ques2
import pandas as pd

# 1. DataFrame from a two-dimensional list
data1 = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 22]]
df1 = pd.DataFrame(data1, columns=['ID', 'Name', 'Age'])
print("1. DataFrame from 2D List:")
print(df1, '\n')

# 2. DataFrame from a dictionary
data2 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
}
df2 = pd.DataFrame(data2)
print("2. DataFrame from Dictionary:")
print(df2, '\n')

# 3. DataFrame from list of lists
data3 = [['Alice', 25], ['Bob', 30], ['Charlie', 22]]
df3 = pd.DataFrame(data3, columns=['Name', 'Age'])
print("3. DataFrame from List of Lists:")
print(df3, '\n')

# 4. DataFrame from list of tuples
data4 = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]
df4 = pd.DataFrame(data4, columns=['Name', 'Age'])
print("4. DataFrame from List of Tuples:")
print(df4, '\n')

# 5. DataFrame from list of dictionaries
data5 = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Charlie', 'Age': 22}
]
df5 = pd.DataFrame(data5)
print("5. DataFrame from List of Dictionaries:")
print(df5)

#ques 3
import pandas as pd

# 1. Create a larger sample DataFrame
data = {
    'Name': ['Ram', 'Mohan', 'Tanuj', 'Naval', 'Vaibhav', 'Rohan'],
    'Age': [25, 30, 35, 40, 28, 33],
    'Salary': [50000, 54000, 58000, 60000, 52000, 57000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Iterate Over Rows
print("\nIterating with iterrows():")
for index, row in df.iterrows():
    print(f"{row['Name']} is {row['Age']} years old with salary {row['Salary']}")

print("\nIterating with itertuples():")
for row in df.itertuples(index=False):
    print(f"{row.Name} earns {row.Salary}")

# 3. Select Rows Based on Condition
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# 4. Select Row Using iloc[]
print("\nThird row :")
print(df.iloc[2])

# 5. Limited Rows Selection with Given Column
print("\nFirst 4 names :")
print(df.loc[:3, 'Name'])

# 6. Drop Rows Based on a Condition
print("\nDropping rows where Salary < 55000:")
print(df[df['Salary'] >= 55000])

# 7. Insert a Row at a Given Position
new_row = pd.DataFrame({'Name': ['Somya'], 'Age': [29], 'Salary': [53000]})
df_updated = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print("\nDataFrame after inserting a new row at position 2:")
print(df_updated)

# 8. Create List from Rows
print("\nDataFrame rows as list of lists:")
print(df.values.tolist())

