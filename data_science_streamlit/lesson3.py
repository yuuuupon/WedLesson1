# -*- coding: utf-8 -*-
"""Lesson3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZtK4BkvBPbNHQMFvH-jWVTWP-egSxaN
"""

# from google.colab import drive
# drive.mount('/content/drive')

# !pip install --upgrade streamlit

# !streamlit --version

# !npm install localtunnel

# dir_name = '/content/drive/MyDrive/水1-2/2/data_science_streamlit'

# Commented out IPython magic to ensure Python compatibility.
# %%writefile {dir_name}/main_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header('コロナ　影響')

df = pd.read_csv('./country_covid_status.csv')
df = df.rename(
 columns={'New_cases':'感染者数', 'New_deaths': '死亡者数', 'population':'人口',
          'deaths_by_cases':'死亡率', 'gdp_per_capita':'一人当たりのGDP'})

option = st.selectbox('国の選択', df['Country'])
st.write(option, 'を選びました')

st.write(df[df['Country'] == option][['人口', '感染者数', '死亡者数', '死亡率', '一人当たりのGDP']])

df_covid = pd.read_csv('./covid_data.csv')

#st.write(df_covid[df_covid['Country'] == option])

def CovidPlot(df, country):

  #datatimeに変換
  df['Date_reported'] = pd.to_datetime(df['Date_reported'])

  #指定した国に絞る
  df_2 = df[df['Country'] == country]

  fig, ax = plt.subplots(2, figsize = (10, 10))
  ax[0].plot(df_2['Date_reported'], df_2['New_cases'], color='lightseagreen')
  ax[1].plot(df_2['Date_reported'], df_2['New_deaths'], color='violet')
  #plt.show()

  return fig

st.write(CovidPlot(df_covid, option))

#dir_name_2 = dir_name + '/pages'

#!streamlit run {dir_name}/main_app.py &>/content/logs.txt &

#!npx localtunnel --port 8501