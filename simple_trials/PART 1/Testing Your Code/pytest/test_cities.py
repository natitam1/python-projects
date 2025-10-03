# test_city_functions.py
from city_functions import format_city_name

def test_city_country():
    assert format_city_name("santiago", "chile" , 5000000) == "Santiago, Chile - Population 5000000"

def test_city_country_population():
    assert format_city_name("santiago", "chile", population=5000000) == "Santiago, Chile - Population 5000000" 