import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') #agarra de la columna fruits los index para la lista

#We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] #agarra las frutas seleccionadas y las jala del full data set a otra variable llamada fruits to show

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Lesson 9 snowflake course
#importing another pyhton package library called request

#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")


#add a text extry box and send the input to fruityvice as part of the api call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json()) #just writes the data on the screen

#take the raw json version of the response and normalize it, it models it as a table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# outputs the screen as a table
streamlit.dataframe(fruityvice_normalized)

#the line shown below will tell your app to bring in some code from the snowflake library you added (snowflake-connector-python). 
import snowflake.connector

#Let's Query Our Trial Account Metadata 
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#querying some data 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#adding a second text entry box
#add a text extry box and send the input to fruityvice as part of the api call
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)







