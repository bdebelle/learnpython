cars = 100
space_in_a_car = 4
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passangers / cars_driven


print "There are" , cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", average_passanger_per_car, "in each car."


beers = 99
space_on_wall = beers - 1

print "We have", beers , "beers left to drink"
print "We only have room for", space_on_wall, "beers."
print "Start drinking them!" 