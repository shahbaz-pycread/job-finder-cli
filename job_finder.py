# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 07:44:47 2024

@author: Shahbaz
"""

cities = ["New Delhi","Gurugram","Noida","Bangalore","Hyderabad","Pune","Chennai"]
job_profiles = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Data Analyst']
job_counts = [
    [100, 80, 50, 20],  # Job counts for New Delhi
    [120, 60, 30, 10],  # Job counts for Gurugram
    [90, 40, 20, 5],    # Job counts for Noida
    [110, 70, 40, 15],  # Job counts for Bangalore
    [120, 85, 25, 50],  # Job counts for Hyderabad
    [50, 26, 10, 35],   # Job counts for Pune
    [40, 65, 15, 70],   # Job counts for Chennai
]

# Get input from the user
user_name = input("Enter your name: ")
city_input = input("Enter the city you are looking for a job in: ")
job_input = input("Enter the job profile you are looking for: ")

# Find the city index
if city_input in cities:
    city_index = cities.index(city_input)
else:
    print(f"Sorry {user_name}, we don't have data for the city {city_input}.")
    exit()

# Find the job profile index
if job_input in job_profiles:
    job_index = job_profiles.index(job_input)
else:
    print(f"Sorry {user_name}, we don't have data for the job profile {job_input}.")
    exit()

# Get the number of available jobs in that city for the specified job profile
job_count = job_counts[city_index][job_index]

# Display the result
print(f"Hello {user_name}, there are {job_count} {job_input} positions available in {city_input}.")