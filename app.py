import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Загрузка модели
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Прогноз цен на недвижимость")
st.write("Введите данные о квартире")

# Ввод всех данных, необходимых для модели
longitude = st.number_input("Долгота", min_value=-125.0, max_value=-114.0, step=0.01)
latitude = st.number_input("Широта", min_value=32.0, max_value=42.0, step=0.01)
housing_median_age = st.number_input("Средний возраст домов", min_value=1, max_value=100, step=1)
total_rooms = st.number_input("Общее количество комнат", min_value=1, max_value=10000, step=1)
total_bedrooms = st.number_input("Общее количество спален", min_value=1, max_value=5000, step=1)
population = st.number_input("Население", min_value=1, max_value=50000, step=1)
households = st.number_input("Количество домохозяйств", min_value=1, max_value=10000, step=1)
median_income = st.number_input("Средний доход", min_value=0.0, max_value=15.0, step=0.1)
ocean_proximity = st.selectbox("Близость к океану", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

# Преобразование в DataFrame с правильными названиями столбцов
features = pd.DataFrame([[longitude, latitude, housing_median_age, total_rooms,
                          total_bedrooms, population, households, median_income, 
                          ocean_proximity]],
                        columns=["longitude", "latitude", "housing_median_age", "total_rooms",
                                 "total_bedrooms", "population", "households", "median_income",
                                 "ocean_proximity"])

if st.button("Предсказать цену"):
    try:
        price = model.predict(features)[0]
        st.success(f"Прогнозируемая цена: {round(price, 2)}$")
    except Exception as e:
        st.error(f"Ошибка при предсказании: {e}")
