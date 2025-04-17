import requests
import webbrowser
OPENWEATHER_API_KEY = "c36d6cd315401c8670153667c752c675"
def get_location_details(city_name):
    endpoint = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city_name,
        'appid': OPENWEATHER_API_KEY,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    if response.status_code == 200 and data:
        return data[0]  
    else:
        print(f"Error: {data[0].get('message', 'Unknown error') if data else 'No data found'}")
        return None
def open_google_map(lat, lon):
    google_maps_url = f"https://www.google.com/maps?q={lat},{lon}"
    webbrowser.open(google_maps_url)
def main():
    city_name = input("Enter the city name: ")
    location_details = get_location_details(city_name)
    if location_details:
        print("\nLocation Details:")
        print(f"Name: {location_details['name']}")
        print(f"Country: {location_details['country']}")
        print(f"Latitude: {location_details['lat']}")
        print(f"Longitude: {location_details['lon']}")
        open_map = input("Would you like to open this location on Google Maps? (yes/no): ").lower()
        if open_map == 'yes':
            open_google_map(location_details['lat'], location_details['lon'])
    else:
        print("Failed to retrieve location details.")

if __name__ == "__main__":
    main()
