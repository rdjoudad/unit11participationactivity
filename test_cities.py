from city_functions import country_capital

def test_city_country():
    assert country_capital("Santiago", "Chile") == "Santiago, Chile"