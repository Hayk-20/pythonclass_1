class Country:
    def __init__(self, country_name: str, continent: str):
        self.country_name = country_name
        self.continent = continent

    def country_info(self):
        return f"Country name {self.country_name} , Continent {self.continent} "


class Brand:
    def __init__(self, brand_name: str, business_start_date: int):
        self.brand_name = brand_name
        self.business_start_date = business_start_date

    def presentation(self):
        return f"Brand name {self.brand_name}, Business start date {self.business_start_date} "


class Season:
    def __init__(self, season_name: str, temperature: int):
        self.season_name = season_name
        self.temperature = temperature

    def season_info(self):
        return f"Season {self.season_name}, Temperature {self.temperature}"


class Product(Season, Brand, Country):
    def __init__(self, product_name: str, p_type: str, product_price: int, product_quantity: int, *args, **kwargs):
        Country.__init__(self, country_name, continent)
        Brand.__init__(self, brand_name,business_start_date)
        Season.__init__(self, season_name,temperature)
        self.p_name = product_name
        self.p_type = p_type
        self.p_price = product_price
        self.p_quantity = product_quantity
        super().__init__(*args, **kwargs)

    def present(self):
        return f"Product name{self.p_name}, {self.season_name} {self.temperature} {self.brand_name}\
               {self.business_start_date} {self.country_name} {self.continent}"

    def discount_price(self):
        if self.p_price == 5000:
            return self.p_price*(25 / 100)

    def increase_quantity(self):
         self.p_quantity += 1
         return f"New quantity {self.p_quantity}"

    def decrease_quantity(self):
        self.p_quantity -= 1
        return f"New quantity {self.p_quantity}"

