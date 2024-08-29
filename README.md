# Flight Dashboard
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen.svg)
![SQL](https://img.shields.io/badge/SQL-Supported-orange.svg)
![Plotly](https://img.shields.io/badge/Plotly-Express-lightblue.svg)

A data-driven web application to explore and analyze flight information, built using Python, SQL, and Streamlit. This dashboard allows users to search for available flights based on their source and destination and provides insightful visualizations, including pie charts, line plots, and bar charts, to help understand trends in the airline industry.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)

## Project Overview

The Flight Dashboard project is designed to help users search for available flights based on specific routes and gain insights into the flight data through interactive visualizations. The web app is built using Streamlit and is powered by Python and SQL for data handling and analysis.

### Data
The dataset used in this project is a CSV file containing the following columns:
- **Airline Name**: Name of the airline operating the flight.
- **Date of Journey**: Date on which the flight is scheduled.
- **Source**: The origin city of the flight.
- **Destination**: The destination city of the flight.
- **Route**: The flight path taken.
- **Departure Time**: The scheduled departure time.
- **Duration**: The total duration of the flight.
- **Total Stops**: The number of stops during the flight.
- **Price**: The fare for the flight.

## Features

- **Flight Search**: Allows users to search for flights by selecting the source and destination cities. The dashboard displays all available flights for the selected route.
  
- **Flight Analytics**:
  - **Pie Chart of Flight Frequencies by Airline**: Visualizes the distribution of flights operated by different airlines.
  - **Line Plot of Busiest Cities**: Shows the busiest cities in terms of flights taken off and landed.
  - **Bar Plots**:
    - **Priciest Airline on Average**: Displays the average flight price for each airline.
    - **Average Flight Duration by Airline**: Compares the average duration of flights across different airlines.

## Technologies Used

- **Python**: The core programming language used for data processing and analysis.
- **Streamlit**: A framework used to deploy the web application locally.
- **SQL**: Used for querying and managing the flight data.
- **Plotly/Plotly Express**: Libraries used for creating interactive visualizations.



## Usage

1. **Search Flights**:
   - Select the source and destination cities from the dropdown boxes.
   - The dashboard will display a table of available flights matching the criteria.

2. **Flight Analytics**:
   - **Flight Frequencies by Airline**: A pie chart showing the proportion of flights operated by each airline.
   - **Busiest Cities**: A line plot representing the cities with the highest flight take-offs and landings.
   - **Priciest Airlines**: A bar plot comparing the average flight prices across airlines.
   - **Flight Duration**: A bar plot showing the average flight duration for each airline.



