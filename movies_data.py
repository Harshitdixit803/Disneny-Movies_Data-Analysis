import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")
df["release_date"] = pd.to_datetime(df["release_date"], infer_datetime_format=True)
df["year"] = df["release_date"].dt.year



'''countplot for ratings'''
plt.figure(figsize=(10,10))
plt.title('Disney movies rating')
sns.countplot(x='mpaa_rating', data=df)
plt.xlabel('rating')


'''count of movies according to the genres'''
plt.figure(figsize=(10, 6)) 
plt.title('Disney movies genres')
sns.countplot(y='genre', data=df)

avg_genre = df.groupby('genre').mean()


'''Evolution of movies gross with time using lineplot'''
plt.figure(figsize=(12, 6))
plt.title('Evolution of movies gross with time') 
plt.xlabel('release date')
plt.ylabel('total gross')
sns.lineplot(x='release_date', y='total_gross', data=df)



'''Evolution of movies gross with time adjusted by inflation using lineplot'''
plt.figure(figsize=(12, 6))
plt.title('Evolution of movies gross with time adjusted by inflation')
plt.xlabel('release date')
plt.ylabel('inflation adjusted gross')
sns.lineplot(x='release_date', y='inflation_adjusted_gross', data=df)

plt.show()
