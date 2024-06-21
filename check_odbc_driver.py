# /mnt/data/check_odbc_driver.py

import streamlit as st
import pyodbc

def check_odbc_driver():
    drivers = [driver for driver in pyodbc.drivers()]
    return drivers

st.title("ODBC Driver Check")

drivers = check_odbc_driver()

st.write("Available ODBC Drivers:")
for driver in drivers:
    st.write(driver)

required_driver = "ODBC Driver 17 for SQL Server"
if required_driver in drivers:
    st.success(f"'{required_driver}' is installed.")
else:
    st.error(f"'{required_driver}' is not installed.")
