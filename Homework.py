class Hotel:

    def __init__(self, name, place, mid_rooms, mid_room_price, lux_rooms, lux_room_price):
        self.name = name
        self.place = place
        self.mid_rooms = mid_rooms
        self.mid_room_price = mid_room_price
        self.lux_rooms = lux_rooms
        self.lux_room_price = lux_room_price

    def dict(self):
        self.mid_rooms = dict(room_1 = "free", room_2 = "free", room_3 = "booked")
        self.lux_rooms = dict(lux_room_1 = "free", lux_room_2 = "booked", lux_room_3 = "booked")
        return f"These are our mid rooms {self.mid_rooms} and these are our lux rooms {self.lux_rooms}"

    def represent(self):
        return f"Welcome to the hotel {self.name}, we are glad you are here.\nYou are one of the best hotels in {self.place}." \
               f" We have mid rooms and lux rooms you can check availability below.\nThe price of mid rooms is {self.mid_room_price}$ per night" \
               f" and the price of lux numbers is {self.lux_room_price}$ per night"


    def booking(self):
        a = input("Do you want to book a number in our hotel\n>>> ")
        if a == "yes":
            global b
            b = input(f"Do you want a lux number or mid\n {self.mid_rooms} {self.mid_room_price}/night \n {self.lux_rooms} {self.lux_room_price}/night"
                   f"\n (If you want a lux number ype lux and if mid type mid)\n>>> ")
            if b == "lux":
                self.lux_rooms = dict(lux_room_1="booked", lux_room_2="booked", lux_room_3="booked")
                print("You successfully booked a lux room. Your room number is 1")
                return self.lux_rooms

            else:
                self.mid_rooms = dict(room_1="booked", room_2="free", room_3="booked")
                print("You successfully booked a mid number. Your room number is 1")
                return self.mid_rooms
        elif a == "no":
            print("OK!, BYE")
        else:
            raise SyntaxError("Sorry, yes or no was expected!")

    def available_rooms_check(self):
        w = input("If you are interested in our available rooms we can show them to you. Do you want it?\n>>> ")
        if w == "yes":
            if b == "lux":
                return f"There are no available lux rooms but there are two available mid rooms {self.mid_rooms}"
            elif b == "mid":
                return f"There is one available mid room {self.mid_rooms} and one lux room {self.lux_rooms}"
        elif w == "no":
            return "OK"
        else:
            raise SyntaxError("Sorry, yes or no was expected!")


    def discount(self):
        d = input("Do you have a discount code? If yes insert it\n>>> ")
        if d == "MGMCALI":
            if b == "lux":
                return f"Your new price is {self.lux_room_price - (self.lux_room_price * 0.2)}$ per night instead of old {self.lux_room_price}$"
            elif b == "mid":
                return f"Your new price is {self.mid_room_price - (self.mid_room_price * 0.2)}$ per night instead of old {self.mid_room_price}$"
        else:
            return f"The discount code you tried is invalid or too old. Your price stays same"


class Taxi:
    def __init__(self, name, cars, price_of_ride):
        self.name = name
        self.cars = cars
        self.price_of_ride = price_of_ride

    def represent(self):
        return f"The cost of ride for your whole tour is {self.price_of_ride}, you will be driven by {self.name}"

    def discount(self):
        r = input("If you have a discount code please type it\n>>> ")
        if r == "uber2021":
            return f"Your new price is {self.price_of_ride - (self.price_of_ride * 0.1)}"
        else:
            return f"Your discount code didn't work so the price is same {self.price_of_ride}"

class Tour(Hotel, Taxi):
    def __init__(self, name):
        Hotel.__init__(self, name = hotel_1.name, place = hotel_1.place, mid_rooms = hotel_1.mid_rooms, mid_room_price = hotel_1.mid_room_price, lux_rooms =hotel_1.lux_rooms,lux_room_price=hotel_1.lux_room_price)
        Taxi.__init__(self, name = taxi_1.name, cars = taxi_1.cars, price_of_ride = taxi_1.price_of_ride)
        self.name = name
        self.price_lux = self.lux_room_price + self.price_of_ride
        self.price_mid = self.mid_room_price + self.price_of_ride

    def gl_represent(self):
        k = input(f"In the very beginning you were asked to choose between lux and mid.\n"
                  f"If you have chosen mid and want to keep you decision type >>> yes I want a mid packet\n"
                  f"If you have chosen lux and ant to keep your decision type >>> yes I want a lux packet\n"
                  f"If you forgot your choice or changed your mind you can press Enter and start again \U0001f600\n>>> ")
        if k == "yes I want a lux packet":
            return f"You have chosen the lux tour which will cost you {self.price_lux}$.\n" \
                   f" The price includes 1 night at {hotel_1.name} (lux number) + taxi cost.\n" \
                   f" You will see the most beautiful places of {hotel_1.place}"
        elif k == "yes I want a mid packet":
            return f"You have chosen the mid tour which will cost you {self.price_mid}$\n " \
                   f"The price includes 1 night at {hotel_1.name} (mid number) + taxi cost.\n " \
                   f"You will see the most beautiful places of {hotel_1.place}"
        else:
            while True:
                break




hotel_1 = Hotel("MGM", "California", 1, 250, 1, 500)
taxi_1 = Taxi("Uber", "Mercedes", 50)
tour_1 = Tour("Cali tour")
print(hotel_1.represent())
print(hotel_1.dict())
print(hotel_1.booking())
print(hotel_1.available_rooms_check())
print(hotel_1.discount())
print(taxi_1.represent())
print(taxi_1.discount())
print(tour_1.gl_represent())





