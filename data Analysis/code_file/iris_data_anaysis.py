from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

#Creating a data frame from sklearn
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

df['species'] = data.target

# Create a figure for the plot
plt.figure(figsize=(10, 6))
df.head(100)

#Explore the structure of the dataset by checking the data types and any missing values
print(df.info())
print(df.isnull().sum())

#Clean the dataset by either filling or dropping any missing values
#df = df.dropna() as the dataset has no missing values

#Calculating simpple statistical analysis
summary = df.describe()
print(summary)

#Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
grouped_df = df.groupby('species').mean()

print(grouped_df) ##Species 0 seems to have the shortest petal width and sepal length while species 1 has the 2 has the largest pf both aspects


#Task 3: Data Visualization


#Create a line plot to visualize the relationship between petal length and petal width between species
plt.plot(df['petal length (cm)'], df['petal width (cm)'], marker='o', label='data', linestyle='--')
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.show()

#Create a Bar plot to visualize the relationship between petal length and sepal width between species
plt.bar(df['species'], df['petal length (cm)'], label='Petal Length')
plt.bar(df['species'], df['sepal width (cm)'], bottom=df['petal length (cm)'], label='Sepal Width')
plt.title('Petal Length vs Sepal Width')
plt.xlabel('Species')
plt.ylabel('Length (cm)')
plt.legend()
plt.show()

#Create a Histogram of a numerical column to understand its distribution.
plt.hist(df['petal length (cm)'], bins=20, label='Petal Length')
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#Create a Scatter Plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], label='data')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

