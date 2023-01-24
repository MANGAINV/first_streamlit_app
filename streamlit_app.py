import streamlit

streamlit.title('My Mom\'s new healthy diner')

streamlit.header('BREAKFAST MENU')

streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🍹Kale, Spinach & Rocket smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')


streamlit.header('🍒 🍇Built my own fruit smoothie🍓 🍑')

import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
