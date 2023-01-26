import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom\'s new healthy diner')

streamlit.header('BREAKFAST MENU')

streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🍹Kale, Spinach & Rocket smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')


streamlit.header('🍒 🍇Built my own fruit smoothie🍓 🍑')


my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
Fruit_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Banana'])
Fruit_to_show = my_fruit_list.loc[Fruit_selected]
streamlit.dataframe(Fruit_to_show)

#New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
if not fruit_choice:
    streamlit.write('The user entered ', fruit_choice)
else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
 except URLError as e:
    streamli.error()

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


#Second section to display fruitvice api response
#streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
