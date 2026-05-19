import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('graphs', exist_ok=True)

print("=" * 50)
print("INDIA CRIME ANALYSIS PROJECT")
print("=" * 50)

# Load data
df = pd.read_csv('data/42_District_wise_crimes_committed_against_women_2001_2012.csv')

# ── GRAPH 1: Total crimes per year across India ──
print("\n Generating Graph 1...")
yearly = df.groupby('Year')[['Rape','Kidnapping and Abduction','Dowry Deaths','Cruelty by Husband or his Relatives']].sum()

yearly.plot(kind='line', figsize=(12,6), marker='o', linewidth=2)
plt.title('Crimes Against Women in India (2001-2012)', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/01_yearly_trends.png')
plt.show()
print("Graph 1 saved!")

# ── GRAPH 2: Top 10 States with highest Rape cases ──
print("\n Generating Graph 2...")
state_rape = df.groupby('STATE/UT')['Rape'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=state_rape.values, y=state_rape.index, palette='Reds_r')
plt.title('Top 10 States with Highest Rape Cases (2001-2012)', fontsize=16, fontweight='bold')
plt.xlabel('Total Cases')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('graphs/02_top_states_rape.png')
plt.show()
print("Graph 2 saved!")

# ── GRAPH 3: Dowry Deaths by State ──
print("\n Generating Graph 3...")
dowry = df.groupby('STATE/UT')['Dowry Deaths'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=dowry.values, y=dowry.index, palette='Oranges_r')
plt.title('Top 10 States with Highest Dowry Deaths (2001-2012)', fontsize=16, fontweight='bold')
plt.xlabel('Total Deaths')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('graphs/03_dowry_deaths.png')
plt.show()
print("Graph 3 saved!")

# ── GRAPH 4: Crime distribution pie chart ──
print("\n Generating Graph 4...")
crime_totals = df[['Rape','Kidnapping and Abduction','Dowry Deaths','Cruelty by Husband or his Relatives','Insult to modesty of Women']].sum()

plt.figure(figsize=(10,8))
plt.pie(crime_totals, labels=crime_totals.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Distribution of Crimes Against Women in India', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('graphs/04_crime_distribution.png')
plt.show()
print("Graph 4 saved!")

print("\n All 4 graphs saved in graphs folder!")
print("=" * 50)