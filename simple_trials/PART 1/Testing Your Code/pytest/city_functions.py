# city_functions.py
def format_city_name(city, country, population=None):
    """Return city and country in title case format."""
    if population:
        return f"{city}, {country} - population {population}".title()
    else:
        return f"{city.title()}, {country.title()}"
