import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

# Reading the data
print(os.listdir(r'C:/Users/ata-d/'))
data = pd.read_csv(r'C:/Users/ata-d/OneDrive/Masaüstü/ML/Datasets/vgsales.csv')

data.info()

data.isna().sum()

# Dropping the NaN rows.
data = data.dropna(subset=['Publisher', 'Year'], axis=0)

# Resetting index for the consistency
data = data.reset_index(drop=True)

# Converting float year type to int
data['Year'] = data['Year'].astype(int)

# -------------------------------------------------------------------------------------------------------


# Number of Games Published Annually
'''''''''
AnnualNumberOfGames = data['Year'].groupby(data['Year']).count()

fig = px.line(AnnualNumberOfGames, x=AnnualNumberOfGames.index, y=AnnualNumberOfGames,
              labels={
                  "index": "Year",
                  "y": "Number of Games Published"
              }
              )
fig.update_layout(title_text='Number of Games Published Annually',
                  title_x=0.5, title_font=dict(size=24))

fig.show()
'''''''''

# Global Video Game Sales Annually
'''''''''
AnnualSales = data.groupby('Year')['Global_Sales'].sum().reset_index()
fig = px.line(AnnualSales, x=AnnualSales['Year'], y=AnnualSales['Global_Sales'],
              labels={
                  "index": "Year",
                  "Global_Sales": "Global Sales (M)"
              }
              )
fig.update_layout(title_text='Global Video Game Sales Annually',
                  title_x=0.5, title_font=dict(size=24))
fig.show()
'''''''''

# Video Game Sales for each Market Annually
'''''''''
AnnualSalesMarket = data.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Scatter(x=AnnualSalesMarket['Year'], y=AnnualSalesMarket['NA_Sales'],
                         name="North America Sales",
                         hovertext=AnnualSalesMarket['NA_Sales']))

fig.add_trace(go.Scatter(x=AnnualSalesMarket['Year'], y=AnnualSalesMarket['EU_Sales'],
                         name="Europe Sales",
                         hovertext=AnnualSalesMarket['EU_Sales']))

fig.add_trace(go.Scatter(x=AnnualSalesMarket['Year'], y=AnnualSalesMarket['JP_Sales'],
                         name="Japan Sales",
                         hovertext=AnnualSalesMarket['JP_Sales']))

fig.add_trace(go.Scatter(x=AnnualSalesMarket['Year'], y=AnnualSalesMarket['Other_Sales'],
                         name="Other Sales",
                         hovertext=AnnualSalesMarket['Other_Sales']))

fig.update_layout(title_text='Video Game Sales for each Market Annually',
                  title_x=0.5, title_font=dict(size=22))  # Location and the font size of the main title
fig.update_layout(
    xaxis_title="Years",
    yaxis_title="Sales (M)")

fig.show()
'''''''''

# Top 15 Publishers that have the highest Global Sales
'''''''''
PublisherTotalGames = data['Global_Sales'].groupby(data['Publisher']).sum().sort_values(ascending=False).to_frame()
PublisherTotalGames_top = PublisherTotalGames.nlargest(15, 'Global_Sales')[['Global_Sales']]

fig = px.bar(data_frame=PublisherTotalGames_top, x=PublisherTotalGames_top.index, y='Global_Sales', color=PublisherTotalGames_top.index)
fig.update_layout(title_text='Top 15 Publishers that have the highest Global Sales',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Games - Global
'''''''''
GameGlobalSales = data['Global_Sales'].groupby(data['Name']).sum().sort_values(ascending=False).to_frame()
GameGlobalSales_top = GameGlobalSales.nlargest(15, 'Global_Sales')[['Global_Sales']]

fig = px.bar(data_frame=GameGlobalSales_top, x=GameGlobalSales_top.index, y='Global_Sales', color=GameGlobalSales_top.index)
fig.update_layout(title_text='Top 15 most Sold Games - Global All Time',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Games - North America
'''''''''
GameGlobalSales = data['NA_Sales'].groupby(data['Name']).sum().sort_values(ascending=False).to_frame()
GameGlobalSales_top = GameGlobalSales.nlargest(15, 'NA_Sales')[['NA_Sales']]

fig = px.bar(data_frame=GameGlobalSales_top, x=GameGlobalSales_top.index, y='NA_Sales', color=GameGlobalSales_top.index)
fig.update_layout(title_text='Top 15 most Sold Games - North America',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Games - Europe
'''''''''
GameGlobalSales = data['EU_Sales'].groupby(data['Name']).sum().sort_values(ascending=False).to_frame()
GameGlobalSales_top = GameGlobalSales.nlargest(15, 'EU_Sales')[['EU_Sales']]

fig = px.bar(data_frame=GameGlobalSales_top, x=GameGlobalSales_top.index, y='EU_Sales', color=GameGlobalSales_top.index)
fig.update_layout(title_text='Top 15 most Sold Games - Europe',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Games - Japan
'''''''''
GameGlobalSales = data['JP_Sales'].groupby(data['Name']).sum().sort_values(ascending=False).to_frame()
GameGlobalSales_top = GameGlobalSales.nlargest(15, 'JP_Sales')[['JP_Sales']]

fig = px.bar(data_frame=GameGlobalSales_top, x=GameGlobalSales_top.index, y='JP_Sales', color=GameGlobalSales_top.index)
fig.update_layout(title_text='Top 15 most Sold Games - Japan',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Games - Other
'''''''''
GameGlobalSales = data['Other_Sales'].groupby(data['Name']).sum().sort_values(ascending=False).to_frame()
GameGlobalSales_top = GameGlobalSales.nlargest(15, 'Other_Sales')[['Other_Sales']]

fig = px.bar(data_frame=GameGlobalSales_top, x=GameGlobalSales_top.index, y='Other_Sales', color=GameGlobalSales_top.index)
fig.update_layout(title_text='Top 15 most Sold Games - Other',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 15 most Sold Platforms - Global All Time
'''''''''
PlatformGlobalSales = data['Global_Sales'].groupby(data['Platform']).sum().sort_values(ascending=False).to_frame()
PlatformGlobalSales = PlatformGlobalSales.nlargest(15, 'Global_Sales')[['Global_Sales']]

fig = px.bar(data_frame=PlatformGlobalSales, x=PlatformGlobalSales.index, y='Global_Sales', color=PlatformGlobalSales.index)
fig.update_layout(title_text='Top 15 most Sold Platforms - Global All Time',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Distribution of the Video Game Sales by Genre
'''''''''
GenreTotalGames = data['Global_Sales'].groupby(data['Genre']).sum().sort_values(ascending=False).to_frame()

fig = go.Figure(data=[go.Pie(labels=GenreTotalGames.index,
                             values=GenreTotalGames['Global_Sales'], opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Video Game Sales by Genre',
                  title_x=0.5, title_font=dict(size=22))
fig.show()
'''''''''

# Number of Games Published by Publishers
'''''''''
PublisherCount = data.groupby(pd.Grouper(key='Publisher')).size().reset_index(name='count')
fig = px.treemap(PublisherCount, path=['Publisher'], values='count')
fig.update_layout(title_text='Number of Games Published by Publishers',
                  title_x=0.5, title_font=dict(size=30)
                  )
fig.update_traces(textinfo="label+value")
fig.show()
'''''''''

# Playstation Console Global Sales (PS + PSP)
'''''''''
PS = data[data['Platform'] == 'PS'].groupby('Year')['Global_Sales'].sum().reset_index()
PS2 = data[data['Platform'] == 'PS2'].groupby('Year')['Global_Sales'].sum().reset_index()
PS3 = data[data['Platform'] == 'PS3'].groupby('Year')['Global_Sales'].sum().reset_index()
PS4 = data[data['Platform'] == 'PS4'].groupby('Year')['Global_Sales'].sum().reset_index()
PSP = data[data['Platform'] == 'PSP'].groupby('Year')['Global_Sales'].sum().reset_index()
PSV = data[data['Platform'] == 'PSV'].groupby('Year')['Global_Sales'].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Scatter(x=PS['Year'], y=PS['Global_Sales'],
                         name="PS Sales",
                         hovertext=PS['Global_Sales']))

fig.add_trace(go.Scatter(x=PS2['Year'], y=PS2['Global_Sales'],
                         name="PS2 Sales",
                         hovertext=PS2['Global_Sales']))

fig.add_trace(go.Scatter(x=PS2['Year'], y=PS2['Global_Sales'],
                         name="PS2 Sales",
                         hovertext=PS2['Global_Sales']))

fig.add_trace(go.Scatter(x=PS3['Year'], y=PS3['Global_Sales'],
                         name="PS3 Sales",
                         hovertext=PS3['Global_Sales']))

fig.add_trace(go.Scatter(x=PS4['Year'], y=PS4['Global_Sales'],
                         name="PS4 Sales",
                         hovertext=PS4['Global_Sales']))

fig.add_trace(go.Scatter(x=PSP['Year'], y=PSP['Global_Sales'],
                         name="PSP Sales",
                         hovertext=PSP['Global_Sales']))

fig.add_trace(go.Scatter(x=PSV['Year'], y=PSV['Global_Sales'],
                         name="PSV Sales",
                         hovertext=PSV['Global_Sales']))

fig.update_layout(title_text='Playstation Console Global Sales (PS + PSP)',
                  title_x=0.5, title_font=dict(size=22))  # Location and the font size of the main title
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Global Sales (M)")

fig.show()
'''''''''

# Playstation vs PC Global Sales Comparison
'''''''''
PS = data[data['Platform'] == 'PS'].groupby('Year')['Global_Sales'].sum().reset_index()
PS2 = data[data['Platform'] == 'PS2'].groupby('Year')['Global_Sales'].sum().reset_index()
PS3 = data[data['Platform'] == 'PS3'].groupby('Year')['Global_Sales'].sum().reset_index()
PS4 = data[data['Platform'] == 'PS4'].groupby('Year')['Global_Sales'].sum().reset_index()
PC = data[data['Platform'] == 'PC'].groupby('Year')['Global_Sales'].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Scatter(x=PS['Year'], y=PS['Global_Sales'],
                         name="PS Sales",
                         hovertext=PS['Global_Sales']))

fig.add_trace(go.Scatter(x=PS2['Year'], y=PS2['Global_Sales'],
                         name="PS2 Sales",
                         hovertext=PS2['Global_Sales']))

fig.add_trace(go.Scatter(x=PS2['Year'], y=PS2['Global_Sales'],
                         name="PS2 Sales",
                         hovertext=PS2['Global_Sales']))

fig.add_trace(go.Scatter(x=PS3['Year'], y=PS3['Global_Sales'],
                         name="PS3 Sales",
                         hovertext=PS3['Global_Sales']))

fig.add_trace(go.Scatter(x=PS4['Year'], y=PS4['Global_Sales'],
                         name="PS4 Sales",
                         hovertext=PS4['Global_Sales']))

fig.add_trace(go.Scatter(x=PC['Year'], y=PC['Global_Sales'],
                         name="PC Sales",
                         hovertext=PC['Global_Sales']))

fig.update_layout(title_text='Playstation vs PC Global Sales Comparison',
                  title_x=0.5, title_font=dict(size=22))  # Location and the font size of the main title
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Global Sales (M)")

fig.show()
'''''''''

# Distribution of Top Seller 50 Games by Publishers
'''''''''
Top50byPublisher = data.nlargest(50, 'Global_Sales')[['Global_Sales', 'Name', 'Publisher']]
Top50byPublisher = Top50byPublisher.groupby(pd.Grouper(key='Publisher')).size().reset_index(name='Number of Games')

fig = px.bar(data_frame=Top50byPublisher, x=Top50byPublisher['Publisher'], y='Number of Games',
             color=Top50byPublisher['Publisher'])
fig.update_layout(title_text='Distribution of Top Seller 50 Games by Publishers',
                  title_x=0.5, title_font=dict(size=20))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Platforms and their Game Genre Distribution
'''''''''
fig = px.sunburst(data_frame=data,
                  path=["Platform", "Genre"],
                  color="Platform",
                  maxdepth=-1,
                  branchvalues='total',
                  hover_name='Platform',
                  hover_data={'Platform': False},
                  title='Platforms and their Game Genre Distribution', template='ggplot2'
                  )

fig.update_traces(textinfo='label+percent parent')
fig.update_layout(font=dict(size=18))
fig.show()
'''''''''
