import streamlit

streamlit.title('My Mom\'s new healthy diner')

streamlit.header('BREAKFAST MENU')

streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🍹Kale, Spinach & Rocket smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')


streamlit.header('🍒 🍇Built my own fruit smoothie🍓 🍑')

import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
Fruit_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Banana'])
Fruit_to_show = my_fruit_list.loc[Fruit_selected]
streamlit.dataframe(Fruit_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
