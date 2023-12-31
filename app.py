from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
import os
import asyncio
import random
import json


app = Flask(__name__)

# Home route
@app.route("/")                   
def home():
    return render_template("home.html")


# Booking route
@app.route("/booking", methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        cityName = request.form.get('cityName')
        countryName = request.form.get('countryName')

        # Fetch data from the API using user input
        url = 'https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation'
        querystring = {"cityName": cityName, "countryName": countryName}

        headers = {
            "X-RapidAPI-Key": "314d71ab52mshfcee920cc7c83abp12050cjsn6c0a9aff3b8d",
            "X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Render the template with the API data
        return render_template("booking.html", datum=data)

    # If it's a GET request or any other case, render the form
    return render_template("booking.html", datum=None)



# Suggestions route
@app.route("/suggestions")                   
def end():

    #API
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"
    querystrings = [
     {"cityName": "Bangkok", "countryName": "Thailand"},
    {"cityName": "Punta Cana", "countryName": "Dominican Republic"},  
    ] 

    headers = {
    "X-RapidAPI-Key": "fbbf2462damsh8f61402249d9b3fp1f85fbjsnf63fedc01dd1",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }
    all_data = []

    for querystring in querystrings:
        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        all_data.append(data)

    return render_template("suggestions.html", datum=all_data)  

if __name__ == "__main__":
    app.run(debug=True)
