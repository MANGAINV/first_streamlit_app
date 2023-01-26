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
#create the repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
#New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
         back_from_function = get_fruityvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)
         
except URLError as e:
     streamlit.error()

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
