import json

# Load JSON data from file
with open('arhamList.json', 'r') as file:
    data = json.load(file)

# Initialize an empty list to store artists with listener counts
artists = []

# Iterate through each item in the data
for name, details in data.items():
    # Check if "Verified Artist" is in the details list (to identify singers)
    if "Verified Artist" in details:
        # Extract monthly listeners as an integer
        monthly_listeners_str = details[1].split(" ")[0].replace(",", "")
        monthly_listeners = int(monthly_listeners_str)
        # Append tuple of (name, monthly_listeners) to the list
        artists.append((name, monthly_listeners))
    else:
        monthly_listeners_str = details[0].split(" ")[0].replace(",", "")
        monthly_listeners = int(monthly_listeners_str)
        artists.append((name, monthly_listeners))

# Sort the list of artists by monthly listeners in descending order
sorted_artists = sorted(artists, key=lambda x: x[1], reverse=True)

# Extract only the names in sorted order
sorted_artist_names = [artist[0] for artist in sorted_artists]

#save the sorted list to a file
with open('ArtistList.txt', 'w') as file:
    for artist in sorted_artist_names:
        file.write(artist + "\n")
        
