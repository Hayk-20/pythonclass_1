class Country:
    def __init__(self, country_name: str, continent: str):
        self.c_name = country_name
        self.continent = continent

    def country_info(self):
        return f"Country name {self.c_name} , Continent {self.continent} "


my_country = Country("Erevan", "Armenia")
print(my_country.country_info())


class Brand:
    def __init__(self, brand_name: str, business_start_date: int):
        self.brand_name = brand_name
        self.business_start_date = business_start_date

    def presentation(self):
        return f"Brand name {self.brand_name}, Business start date {self.business_start_date} "


my_presentation = Brand("Lexus", 2000)
print(my_presentation.presentation())


class Season:
    def __init__(self, season_name: str, temperature: int):
        self.season_name = season_name
        self.temperature = temperature

    def season_info(self):
        return f"Season {self.season_name}, Temperature {self.temperature}"


my_season = Season("Winter", 35)
print(my_season.season_info())


class Product(Season, Brand, Country):
    def __init__(self, product_name: str, product_type: str, product_price: int, product_quantity: int):
        Country.__init__(self, country_name, continent)
        Brand.__init__(self,brand_name,business_start_date)
        Season.__init__(self,season_name,temperature)
        self.p_name = product_name
        self.p_type = product_type
        self.p_price = product_price
        self.p_quantity = product_quantity


    def prod_t(self):
        return f"Name {self.p_name}, Type {self.p_type}, price {self.p_price}, Quantity {self.p_quantity}"


