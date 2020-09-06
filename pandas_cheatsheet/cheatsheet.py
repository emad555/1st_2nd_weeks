# import pandas
import pandas as pd


#declare dataframes
df1 = pd.DataFrame([[2,4,6],[10,20,30]])
print(df1)

# add columns names
df2 = pd.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Age", "Value"])
print(df2)

# add index names
df3 = pd.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Age", "Value"], index = ["First", "Second"])
print(df3)


#type
print(type(df3))

# to know the methods of the datafram we use dir(df3)
dir(df3)

# to know the methods of the datafram we use "dir(df3)" //for each row
print("the mean is: ")
print(df3.mean())

# to know the methods of the datafram we use "dir(df3)" //for one column
print("the mean is: ")
print(df3.Price.mean())



