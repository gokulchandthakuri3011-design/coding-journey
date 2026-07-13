"""
### Assignment 1: GPS Coordinate Tracker

*Practice creating, accessing, and unpacking tuples.*

1. Create a tuple `coord1` with latitude `40.7128` and longitude `-74.0060` (New York).
2. Create a second tuple `coord2` with latitude `34.0522` and longitude `-118.2437` (Los Angeles).
3. Print the latitude of `coord1` and the longitude of `coord2` using index access.
4. Unpack `coord1` into variables `lat` and `lon` and print a formatted string.
5. Create a list called `trip` containing both coordinate tuples.
6. Loop through `trip`, unpack each tuple, and print `"Location: lat, lon"`.
- **File:** `Day10_Task1.py
"""
# Step 1: Creating tuples for GPS coordinates
coord1 = (40.7128, -74.0060) # New York
coord2 = (34.0522, -118.2437) # Los Angeles

# Step 2: Accessing latitude and longitude using index access
print(f"Latitude of coord1: {coord1[0]}")
print(f"Longitude of coord2: {coord2[1]}")

# Step 3: Unpacking coord1 into lat and lon
lat, lon = coord1
print(f"Unpacked coord1: Latitude = {lat}, Longitude = {lon}")

# Step 4: Creating a list of coordinate tuples called trip
trip = [coord1, coord2]

# Step 5: Looping through trip and unpacking each tuples
for location in trip:
    lat, lon = location
    print(f"Location: {lat}, {lon}")

    