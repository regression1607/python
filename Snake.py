import random
import curses

s = curses.initscr()
curses.curs_set(0)
Snake_height, Snake_width = s.getmaxyx()
w = curses.newwin(Snake_height, Snake_width, 0, 0)
w.keypad(1)
w.timeout(100)

snake_x = Snake_width/4
snake_y = Snake_height/2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [Snake_height/2, Snake_width/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, Snake_height] or snake[0][1] in [0, Snake_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    new_head = [snake[0][0], snake[0] [1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, Snake_height-1),
                random.randint(1, Snake_width-1)
            ]
            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
