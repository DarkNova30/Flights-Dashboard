import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from dbhelper import DB

db = DB()

st.sidebar.title("Flights Analytics")
user_option = st.sidebar.selectbox("Menu", ["Select one", "Check Flights", "Analytics"])

if user_option == "Check Flights":
    st.title("Choose source and destination")
    col1, col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        src = st.selectbox("Source", sorted(city))
    with col2:
        dest = st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        results = db.fetch_all_flights(src, dest)
        if len(results) > 1:
            st.dataframe(results)
        else:
            st.text("No Flights Avaliable :/")

elif user_option == "Analytics":
    st.title("Analytics")
    airline, fr = db.fetch_airline_fr()
    fig = go.Figure(
        go.Pie(labels=airline,
               values=fr,
               hoverinfo="label+percent",
               textinfo="value"
        )
    )
    st.header("Flight Frequencies")
    st.plotly_chart(fig)

    city, fr2 = db.busy_airport()
    fig2 = px.bar(
        x=city,
        y=fr2,
    )
    st.header("Busiest Airport City")
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

    # daily line plot
    st.header("Monthly Flight Frequencies")
    airlines = ['Jet Airways',
    'SpiceJet',
    'Air India',
    'IndiGo',
    'Air Asia',
    'Vistara',
    'GoAir',
    'Jet Airways Business',
    'Multiple carriers',
    'Vistara Premium economy',
    'Multiple carriers Premium economy',
    'Trujet'
    ]
    chosen_line = st.selectbox("Select Airline", airlines)
    date, fr3 = db.daily_fr(chosen_line)
    fig3 = px.line(
        x=date,
        y=fr3,
        title=chosen_line+" Monthly flights",
        width=60,

    )
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


    # costly airline
    c1, c2 = st.columns(2)
    with c1:
        line, price = db.costly_airline()
        fig4 = px.bar(

            x=line,
            y=price,
        )
        st.header("Costliest Airlines (on avg)")
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)
    with c2:
        line, time = db.duration_airlines()
        fig4 = px.bar(

            x=line,
            y=time,

        )
        st.header("longest duration flights (on avg)")
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)


else:
    st.title("Flights Dashboard using python & sql")
