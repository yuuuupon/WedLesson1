import streamlit as st
import pandas as pd

#"st.set_page_config()

df = pd.read_csv('country_covid_status.csv')
df_covid = pd.read_csv('covid_data.csv')

df = df.rename(
    columns={'New_cases':'感染者数', 'New_deaths':'死亡者数',
    'population':'人口', 'deaths_by_cases':'死亡率', 'gdp_per_capita':'一人あたりのGDP（USドル）'})

df_covid = df_covid.rename(
    columns={'Date_reported':'日付', 'New_cases':'感染者数', 'New_deaths':'死亡者数'})

st.header('コロナによる影響')
# 国を選択
option = st.selectbox(
    '国の選択',
     df['Country'])

st.write(df[df['Country']==option][['人口','感染者数', '死亡者数', '死亡率', '一人あたりのGDP（USドル）']])
st.text('※感染者数と死亡者数は2023年4月13日時点の累計\n※人口は2021年のデータ')


import matplotlib.pyplot as plt
def plot_new_covid_cases_and_deaths_by_country(df, country):

    df_c = df[df['Country']==country]

    df_c['日付'] = pd.to_datetime(df_c['日付'])

    fig, ax = plt.subplots(2, figsize=(20, 8))
    ax[0].plot(df_c['日付'], df_c['感染者数'])
    ax[1].plot(df_c['日付'], df_c['死亡者数'], color='orange')
    return fig


st.write(plot_new_covid_cases_and_deaths_by_country(df_covid[df_covid['Country']==option], option))

st.write(df_covid[df_covid['Country']==option][['日付', '感染者数', '死亡者数']])
