import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('graphs', exist_ok=True)

# Load data
df = pd.read_excel('data/data_cts_intentional_homicide.xlsx', skiprows=2)
df.columns = df.columns.str.strip()

# Our 10 countries
countries = ['Afghanistan', 'Brazil', 'El Salvador', 'Guyana',
             'Honduras', 'Jamaica', 'Peru', 'South Africa',
             'Trinidad and Tobago', 'Venezuela']

# Filter
df = df[df['Country'].isin(countries)]
df = df[df['Sex'] == 'Total']
df = df[df['Age'] == 'Total']
df = df[df['Unit of measurement'] == 'Counts']
df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
df = df.dropna(subset=['VALUE'])
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Use data from 2000 to 2023
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2023)]

print(" Data loaded! Shape:", df.shape)
print(df[['Country', 'Year', 'VALUE']].head(10))

# GRAPH 1 - Homicide trends over years per country
plt.figure(figsize=(14, 7))
for country in df['Country'].unique():
    data = df[df['Country'] == country].sort_values('Year')
    plt.plot(data['Year'], data['VALUE'], marker='o', label=country, linewidth=2)
plt.title('Intentional Homicide Trends (2000-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Homicides')
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/01_trends.png')
plt.show()
print(" Graph 1 saved!")

# GRAPH 2 - Total homicides per country
total = df.groupby('Country')['VALUE'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=total.values, y=total.index, palette='Reds_r')
plt.title('Total Homicides by Country (2000-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Total Homicides')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('graphs/02_total.png')
plt.show()
print(" Graph 2 saved!")

# GRAPH 3 - Latest available year per country comparison
latest_data = df.loc[df.groupby('Country')['Year'].idxmax()]
plt.figure(figsize=(12, 6))
sns.barplot(data=latest_data.sort_values('VALUE', ascending=False),
            x='Country', y='VALUE', palette='Oranges_r')
plt.title('Most Recent Homicide Count per Country', fontsize=16, fontweight='bold')
plt.xlabel('Country')
plt.ylabel('Homicides')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('graphs/03_latest.png')
plt.show()
print(" Graph 3 saved!")

# GRAPH 4 - Pie chart crime share
plt.figure(figsize=(10, 8))
plt.pie(total.values, labels=total.index, autopct='%1.1f%%',
        startangle=140, colors=sns.color_palette('Set2', len(total)))
plt.title('Share of Total Homicides by Country (2000-2023)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('graphs/04_pie.png')
plt.show()
print(" Graph 4 saved!")

print(" All 4 graphs saved in graphs folder!")