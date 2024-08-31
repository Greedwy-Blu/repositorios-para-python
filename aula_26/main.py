# method chaining
class Car:

  def turn_on(self):
    print("You start the engine")
    return self

  def driver(self):
    print("You drive the car")
    return self

  def breke(self):
    print("You stepp on the brakes")
    return self

  def turn_off(self):
    print("You turn off the engine")
    return self


car = Car()

car.turn_on().driver()

car.breke().turn_off

car.turn_on()\
  .driver()\
  .breke()\
  .turn_off()





