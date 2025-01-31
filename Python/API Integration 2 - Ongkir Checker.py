import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Replace with your RajaOngkir API key
API_KEY = "8f780aec72df6df254bb73cc365cbd4c"
BASE_URL = "https://api.rajaongkir.com/starter/cost"
CITIES_URL = "https://api.rajaongkir.com/starter/city"


# Fetch city data
def fetch_cities():
    headers = {
        "key": API_KEY
    }

    response = requests.get(CITIES_URL, headers=headers)
    if response.status_code == 200:
        cities = response.json()['rajaongkir']['results']
        city_dict = {}
        for city in cities:
            city_dict[city['city_name']] = city['city_id']
        return city_dict
    else:
        messagebox.showerror("Error", "Failed to retrieve city data")
        return {}


# Function to check delivery cost
def check_cost():
    origin_city_name = origin_combobox.get()
    destination_city_name = destination_combobox.get()
    weight = weight_entry.get()
    courier = courier_combobox.get()

    if not (origin_city_name and destination_city_name and weight and courier):
        messagebox.showerror("Error", "Please fill all fields")
        return

    origin_city_id = city_dict[origin_city_name]
    destination_city_id = city_dict[destination_city_name]

    headers = {
        "key": API_KEY
    }

    data = {
        "origin": origin_city_id,
        "destination": destination_city_id,
        "weight": int(weight),
        "courier": courier
    }

    response = requests.post(BASE_URL, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        try:
            costs = result['rajaongkir']['results'][0]['costs']
            cost_text.delete(1.0, tk.END)  # Clear previous results
            for item in costs:
                service = item['service']
                cost = item['cost'][0]['value']
                etd = item['cost'][0]['etd']
                cost_text.insert(tk.END, f"Service: {service}, Cost: {cost}, Estimated Delivery Time: {etd} days\n")
        except KeyError:
            messagebox.showerror("Error", "Invalid response from API")
    else:
        messagebox.showerror("Error", "Failed to retrieve data from API")


# Create the main window
window = tk.Tk()
window.title("Delivery Cost Checker")
window.geometry("400x400")

# Fetch cities and create dictionary
city_dict = fetch_cities()
city_names = list(city_dict.keys())

# Create and place widgets
tk.Label(window, text="Origin City:").pack()
origin_combobox = ttk.Combobox(window, values=city_names)
origin_combobox.pack()

tk.Label(window, text="Destination City:").pack()
destination_combobox = ttk.Combobox(window, values=city_names)
destination_combobox.pack()

tk.Label(window, text="Weight (grams):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Courier:").pack()
courier_combobox = ttk.Combobox(window, values=["jne", "pos", "tiki"])
courier_combobox.pack()

check_button = tk.Button(window, text="Check Cost", command=check_cost)
check_button.pack()

cost_text = tk.Text(window, height=10, width=50)
cost_text.pack()

# Start the Tkinter event loop
window.mainloop()