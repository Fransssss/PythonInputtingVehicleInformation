# Author : Fransiskus Agapa

# =============================
# simple program - input information of different vehicle
# practice sending object as argument
# =============================

from vehicle import Vehicle
from data import the_brand
from data import the_color
from data import the_origin_place
from data import the_year
from data import the_price

print("\n== Dealership New Input Database ==")
print("1. Car")
print("2. Motorcycle")
print("3. Bus")
print("4. Tractor")
print("5. Helicopter")
print("e. Exit")
choice = input("choice: ").lower()              # make user input to lower case to make while-loop condition simpler

while choice != 'e':
    if choice == '1':
        print("\nAdding a new car to the storage ... Car added\n")
        car = Vehicle()
        car_brand = input("Name of the car brand: ").upper()                                 # make the format nicer
        if car_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            car_color = input("Color of the car: ").capitalize()                             # make the format nicer
            if car_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                car_origin = input("Where was the car brand originally from: ").capitalize()  # make the format nicer
                if car_origin.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    try:                                                              # in case user input is not digit
                        print("What year the car was made: ", end=" ")
                        car_year = int(input())
                        print("What is the price of the car: ", end="$")
                        car_price = int(input())
                        the_brand(car, car_brand)
                        the_color(car, car_color)
                        the_origin_place(car, car_origin)
                        the_year(car, car_year)
                        the_price(car, car_price)
                        print("\n=======================")
                        print("New Car Summary")
                        print("=======================")
                        print("The brand of the car is " + str(car.brand))
                        print("The color of the car is " + str(car.color))
                        print("The car brand of the car was originally from " + str(car.origin_place))
                        print("The car was made in " + str(car.year))
                        print("The price of the car is $" + str("{:.2f}".format(car.price)))  # two decimal places
                        print("=======================")
                    except ValueError:
                        print("\n[ Invalid input - digit only ]")

    elif choice == '2':
        print("\nAdding a new motorcycle to the storage ... Motorcycle added\n")
        motorcycle = Vehicle()
        motorcycle_brand = input("Name of the motorcycle brand: ").upper()
        if motorcycle_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            motorcycle_color = input("Color of the motorcycle: ").capitalize()
            if motorcycle_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                motorcycle_origin = input("Where was the motorcycle brand originally from: ").capitalize()
                if motorcycle_origin.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    try:
                        print("What year the motorcycle was made: ", end=" ")
                        motorcycle_year = int(input())
                        print("What is the price of the motorcycle: ", end="$")
                        motorcycle_price = int(input())
                        the_brand(motorcycle, motorcycle_brand)
                        the_color(motorcycle, motorcycle_color)
                        the_origin_place(motorcycle, motorcycle_origin)
                        the_year(motorcycle, motorcycle_year)
                        the_price(motorcycle, motorcycle_price)
                        print("\n=======================")
                        print("New Motorcycle Summary")
                        print("=======================")
                        print("The brand of the motorcycle is " + str(motorcycle.brand))
                        print("The color of the motorcycle is " + str(motorcycle.color))
                        print("The brand of the motorcycle was originally from " + str(motorcycle.origin_place))
                        print("The motorcycle was made in " + str(motorcycle.year))
                        print("The price of the motorcycle is $" + str("{:.2f}".format(motorcycle.price)))
                        print("=======================")

                    except ValueError:
                        print("\n[ Invalid input - digit only ]")

    elif choice == '3':
        print("\nAdding a new bus ... Bus added\n")
        bus = Vehicle()
        bus_brand = input("Name of the bus brand: ").upper()
        if bus_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            bus_color = input("Color of the bus; ").capitalize()
            if bus_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                bus_origin = input("Where was the bus brand originally from: ").capitalize()
                if bus_origin.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    try:
                        print("What year the bus was made: ", end=" ")
                        bus_year = int(input())
                        print("What is the price of the bus: ", end="$")
                        bus_price = int(input())
                        the_brand(bus, bus_brand)
                        the_color(bus, bus_color)
                        the_origin_place(bus, bus_origin)
                        the_year(bus, bus_year)
                        the_price(bus, bus_price)
                        print("\n=======================")
                        print("New Bus Summary")
                        print("=======================")
                        print("The brand of the bus is " + str(bus.brand))
                        print("The color of the bus is " + str(bus.color))
                        print("The brand of the bus was originally from " + str(bus.origin_place))
                        print("The bus was made in " + str(bus.year))
                        print("The price of the bus is $" + str("{:.2f}".format(bus.price)))
                        print("=======================")

                    except ValueError:
                        print("\n[ Invalid input- digit only ]")

    elif choice == '4':
        print("\nAdding a new tractor - Tractor added\n")
        tractor = Vehicle()
        tractor_brand = input("What is the tractor brand: ").upper()
        if tractor_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            tractor_color = input("What is the color of the tractor: ").capitalize()
            if tractor_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                tractor_origin = input("Where the tractor brand was originally from: ").capitalize()
                if tractor_origin.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    try:
                        print("What year the tractor was made: ", end=" ")
                        tractor_year = int(input())
                        print("What is the price of the tractor: ", end="$")
                        tractor_price = int(input())
                        the_brand(tractor, tractor_brand)
                        the_color(tractor, tractor_color)
                        the_origin_place(tractor, tractor_origin)
                        the_year(tractor, tractor_year)
                        the_price(tractor, tractor_price)
                        print("\n=======================")
                        print("New Tractor Summary")
                        print("=======================")
                        print("The brand of the tractor is " + str(tractor.brand))
                        print("The color of the tractor is " + str(tractor.color))
                        print("The brand of the tractor was originally from " + str(tractor.origin_place))
                        print("The tractor was made in " + str(tractor.year))
                        print("The price of the tractor is $" + str("{:.2f}".format(tractor.price)))
                        print("=======================")

                    except ValueError:
                        print("\n[ Invalid input - digit only ]")
    elif choice == '5':
        print("\nAdding a new helicopter - Helicopter added\n")
        helicopter = Vehicle()
        heli_brand = input("What is the helicopter brand: ").upper()
        if heli_brand.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            heli_color = input("What is the color of the helicopter: ").capitalize()
            if heli_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                heli_origin = input("Where the helicopter brand was originally from: ").capitalize()
                if heli_origin.isdigit():
                    print("\n[ Invalid input - string only ]")
                else:
                    try:
                        print("What year the helicopter was made: ", end=" ")
                        heli_year = int(input())
                        print("What is the price of the helicopter: ", end="$")
                        heli_price = int(input())
                        the_brand(helicopter, heli_brand)
                        the_color(helicopter, heli_color)
                        the_origin_place(helicopter, heli_origin)
                        the_year(helicopter, heli_year)
                        the_price(helicopter, heli_price)
                        print("\n=======================")
                        print("New Helicopter Summary")
                        print("=======================")
                        print("The brand of the helicopter is " + str(helicopter.brand))
                        print("The color of the helicopter is " + str(helicopter.color))
                        print("The brand of the helicopter was originally from " + str(helicopter.origin_place))
                        print("The helicopter was made in " + str(helicopter.year))
                        print("The price of the helicopter is $" + str("{:.2f}".format(helicopter.price)))
                        print("=======================")

                    except ValueError:
                        print("\n[ Invalid input - digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Dealership New Input Database ==")
    print("1. Car")
    print("2. Motorcycle")
    print("3. Bus")
    print("4. Tractor")
    print("5. Helicopter")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
