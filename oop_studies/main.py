# import turtle
#
# creuza = turtle.Turtle()
# print(creuza)
# creuza.shape("turtle")
# creuza.color("coral")
# creuza.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

import prettytable
table = prettytable.PrettyTable()
table.align = "c"
table.add_column("Pokemons",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Eletric", "Water", "Fire"])






print(table)