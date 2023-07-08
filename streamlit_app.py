#Import the Python package library called 'streamlit'
import streamlit

#Make the title of the page
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boild Free-Range Egg')
streamlit.text('🥑🍞 Arvocado Toast')

#Make the header of the page
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Import the Python package library called 'pandas'
import pandas

#Make pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv to pull the data into a dataframe we'll call my_fruit_list
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)
