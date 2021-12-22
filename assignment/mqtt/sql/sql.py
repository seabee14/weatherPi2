#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
from dotenv import dotenv_values
from sense_hat import SenseHat
import sqlite3
import time
import datetime
from datetime import datetime

#function to create table for data coming from rPi sensors with sense HAT attached
def createTable():
    c.execute("""CREATE TABLE IF NOT EXISTS weatherData(
            dateNow TEXT,
            timeNow TEXT,
            temperature DOUBLE,
            humi DOUBLE,
            pres DOUBLE 
            )""")

#function to create table for data from sensors when sense HAT attached to ribbon cable
def createTable1():
    c.execute("""CREATE TABLE IF NOT EXISTS updatedWeatherData(
            dateNow TEXT,
            timeNow TEXT,
            temperature DOUBLE,
            humi DOUBLE,
            pres DOUBLE 
            )""")

#function to insert data from rPi senseHAT attached to rPi
def updateTable(date, time, temp, humidity, pressure):
    c.execute("INSERT INTO weatherData (dateNow, timeNow, temperature, humi, pres) VALUES (?, ?, ?, ?, ?)",
            (date, time, temp, humidity, pressure))
    conn.commit()

#function to insert data from rPi senseHAT attached to rPi via ribbon cable
def updateTable1(date, time, temp, humidity, pressure):
    c.execute("INSERT INTO updatedWeatherData (dateNow, timeNow, temperature, humi, pres) VALUES (?, ?, ?, ?, ?)",
            (date, time, temp, humidity, pressure))
    conn.commit()

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# create system time and date variables
now = datetime.now()
time1 = now.strftime("%H:%M:%S")
date1 = now.strftime("%d/%m/%Y")

# Create variables from rPi sensors
temp1 = round(sense.temperature,2)
humidity1 = round(sense.humidity,2)
pressure1 = round(sense.pressure,2)


# main app function
if __name__ == "__main__":
    conn = sqlite3.connect('weatherPi_database.db')
    c = conn.cursor()


    createTable()
    updateTable(date1, time1, temp1, humidity1, pressure1)
    print(temp1)
    print(humidity1)
    print(pressure1)
    print(date1)
    print(time1)


    conn.close()