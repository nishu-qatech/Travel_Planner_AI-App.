import streamlit as st
from google import genai
import datetime

client = genai.Client(api_key='AIzaSyA-mPacw1-3EXSMQoUtA_--EYDX1znpycY')

st.title("Travel Planner AI 🌍✈️")
with st.form("my_form"):
    starting_point = st.text_input("Starting Point(City)" , placeholder= "Eg; New York, Tokyo, Thailand")
    destination_point = st.text_input("Destination Point(Place)", placeholder="Eg; paris, London, Rome")
    Starting_date = st.date_input("Starting Date", min_value=datetime.date.today())
    Ending_date = st.date_input("Ending Date",min_value=Starting_date)
    num_travelers = st.number_input("Number of Travelers", min_value=1,value=1)
    Currency = st.selectbox("Currency",options=["USD","INR","EURO","GBP"])
    Budget = st.number_input("Budget(in INR)", min_value=10000)
    Trip_type = st.selectbox("Trip type",options=["Adventure", "Leisure","Cultural","Family","Solo","Honeymoon"])
    submit_btn = st.form_submit_button("Get Travel Plan", type="primary")

if submit_btn:
    if not all([starting_point,destination_point,Starting_date,Ending_date,Currency,Budget,Trip_type]):
        st.error("Please fill all the field")
    else:
        with st.spinner("Generating your Travel Planner AI.."):
            prompt = f"""
            Create a detailed travel itenerary with the following information:

            Starting from: {starting_point}
            Destination to visit: {destination_point}
            Trip start from {Starting_date} to {Ending_date}
            Number of Travelers : {num_travelers}
            Budget: {Budget} {Currency}
            Travel style: {Trip_type}

            Please provide a itinerary incluing:
            1.Transportion option between locations
            2.Recommended accomadation
            3.Key attraction to visit each day
            4.Estimation costs for each majot activity
            5.local cusine recomendation
            6. Any pratical tip or consideration

            Format the response in aclear ,organized manner with section for each day. """

            response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
            st.write(response.text)