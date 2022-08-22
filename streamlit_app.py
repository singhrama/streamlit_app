import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Favorites")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥞 Pan Cakes with maple Syrup")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
fruit_ls = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruit_ls)
