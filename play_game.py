
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

class Game():
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake game")
        self.screen.tracer(0)
        # se spengo il tracer, ogni volta che si vuole visualizzare lo schermo aggiornato, bisogna fare uno screen update

        self.numero_mele = -1
        while self.numero_mele <= -1 or self.numero_mele > 10:
            try:
                input_text = self.screen.textinput(title="Input", prompt="Quante mele generare? (max: 10)")
                if input_text is None:  # Verifica se l'input è vuoto

                    continue

                self.numero_mele = int(input_text)
                if self.numero_mele <= 0 or self.numero_mele > 10:
                    print("Inserisci un numero compreso tra 1 e 10.")
            except ValueError:
                # Se si verifica un ValueError durante la conversione in int
                print("Errore: inserisci solo valori numerici interi.")

       
       
        self.snake = Snake()
        
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        
        self.play(self.screen,self.snake,self.numero_mele)
    
    def play(self, screen, snake, numero_mele):
       
        game_is_on = True

        foods = []
        for _ in range(numero_mele):
            foods.append(Food())
            
        scoreboard=Scoreboard()
        while game_is_on and not snake.check_collision():  # not check_collision perche' di base ritorna false
            screen.update()
            time.sleep(0.1)
            for food in foods:
                if snake.head.distance(food) < 15:
                    food.random_location() #se viene colpito riposiziona sullo schermo
                    snake.extend()  # aggiunge un segmento in coda
                    scoreboard.increase_score()

            snake.move()
            game_is_on = snake.check_inside_screen()

        scoreboard.game_over()
        self.screen.update()
        