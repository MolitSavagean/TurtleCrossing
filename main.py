import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")
car = CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == FINISH_LINE_Y:
        car.increase_speed()
        player.repeat()
        scoreboard.level_up()

screen.exitonclick()





