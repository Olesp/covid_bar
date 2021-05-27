#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
#-*- coding: utf-8 -*-


# Metadata allows your plugin to show up in the app, and website.
#
#  <xbar.title>Covid numbers</xbar.title>
#  <xbar.version>v0.2.0</xbar.version>
#  <xbar.author>Olvier Lespagnon</xbar.author>
#  <xbar.author.github>olesp</xbar.author.github>
#  <xbar.desc>Display covid states from the country you choose.</xbar.desc>
#  <xbar.image>https://i.ibb.co/dQ6NSmJ/Capture-d-e-cran-2021-05-27-a-14-50-07.png</xbar.image>
#  <xbar.dependencies>python,requests,json</xbar.dependencies>

# Variables become preferences in the app:
#
#  <xbar.var>string(VAR_COUNTRY="France"): The country from where the data will be retrieved.</xbar.var>
# Get your API key at https://rapidapi.com/Gramzivi/api/covid-19-data
#  <xbar.var>string(VAR_APIKEY="YOUR-API-KEY"): Your api key from rapidapi.com.</xbar.var>

import requests
import os
import json
import csv

from requests.api import request

key = os.environ["VAR_APIKEY"]
country = os.environ["VAR_COUNTRY"]

url = "https://covid-19-data.p.rapidapi.com/country"
querystring = {"name":country}

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring).json()
response = response[0]

vaccine_csv = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/{country}.csv".format(country=country)).content
if not os.path.isdir(country):
    os.mkdir(country)
with open("{country}/data.csv".format(country=country),'wb') as file:
        file.write(vaccine_csv)
with open("{country}/data.csv") as data:
    csv_reader = csv.DictReader(data,delimiter=",")
    data_string = json.dumps(list(csv_reader))
    data_jstring = json.loads(data_string)
data = data_jstring[-1]

print("🦠")
print("---")
print("😷Cases")
print("--Total cases in {country} : {cases:,} | color=white".format(cases=response["confirmed"], country=country))
print("--Deaths in {country} : {morts:,} | color=red".format(morts=response["deaths"], country=country))
print("--Recovered in {country} : {recovered:,} | color=green".format(recovered=response["recovered"], country=country))
print("---")
print("💉Vaccines")
print("--Total vaccinated in {country} : {total_vacc:,} | color=white".format(country=country, total_vacc=int(data["total_vaccinations"])))
print("--One dose recieved : {partial:,} | color=yellow".format(country=country, partial=int(data["people_vaccinated"])))
print("--Two dose recieved : {full:,} | color=green".format(country=country, full=int(data["people_fully_vaccinated"])))
