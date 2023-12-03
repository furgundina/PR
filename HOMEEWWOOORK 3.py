postcards = {"Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"}
postcards["Petra"] = "Paris"
postcards["Ivan"] = "Moscow"
postcards["Oleg"] = "Sydney"
unique_cities = len(set(postcards.values()))
print(f"Количество уникальных городов в коллекции Алисы: {unique_cities}")
print("Уникальные города в коллекции Алисы:")
print(set(postcards.values()))