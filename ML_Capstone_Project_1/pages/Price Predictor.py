import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Viz Demo")

df_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'df.pkl')
with open(df_path, 'rb') as file:
    df = pickle.load(file)

pipeline_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'pipeline.pkl')
with open(pipeline_path, 'rb') as file:
    pipeline = pickle.load(file)



st.header('🏡 Enter Your Inputs')

# property_type
property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

# Number of Bedrooms - slider
bedroom_min = int(df['bedRoom'].min())
bedroom_max = int(df['bedRoom'].max())
bedrooms = st.slider('Number of Bedrooms', min_value=bedroom_min, max_value=bedroom_max, value=2)

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

# servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
servant_room = 1.0 if st.checkbox('Servant Room', value=False) else 0.0
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('🏠 Predict'):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))


