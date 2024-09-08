from snake import Snake
from screen import MyScreen
import time

my_screen = MyScreen()

snake = Snake()

my_screen.onkeyfunction(snake.up,
                        snake.down,
                        snake.left,
                        snake.right)

game_is_on = True
while game_is_on:
    my_screen.screen.update()
    time.sleep(1)

    snake.move()

my_screen.screen.exitonclick()
