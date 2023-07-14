import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import quarto
from plotnine import *


country_data = pd.read_csv('~/Desktop/Assignment_DCU/Tableau-assignment/Quarto-Report/Data/country_data.csv')
'''print(country_data)'''

fig = px.choropleth(data_frame=country_data,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='location',
                    title='COVID-19 Total Cases Worldwide',
                    color_continuous_scale='Viridis')


fig.show()

bar_data = country_data[['location', 'total_cases']].dropna()


bar_data = bar_data.sort_values('total_cases', ascending=False)


plt.figure(figsize=(10, 6))
plt.bar(bar_data['location'], bar_data['total_cases'])
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases by Country')
plt.xticks(rotation=90)
plt.tight_layout()


plt.show()


scatter_data = country_data[['total_cases', 'new_cases']].dropna()


sns.set(style='ticks')
sns.lmplot(x='total_cases', y='new_cases', data=scatter_data, scatter_kws={'alpha': 0.5})
plt.xlabel('Total Cases')
plt.ylabel('New Cases')
plt.title('Scatterplot: Total Cases vs New Cases')


plt.show()


country_data['date'] = pd.to_datetime(country_data['date'])


time_series_data = country_data[['date', 'total_cases']].dropna()


time_series_data = time_series_data.set_index('date')


plt.figure(figsize=(10, 6))
plt.plot(time_series_data.index, time_series_data['total_cases'])
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Time-Series Chart: Total Cases over Time')


plt.show()