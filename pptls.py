#creamos la iteracin aleatoria de la seleccion de la maquina
import random
options = ("piedra", "papel", "tijera", "lagarto", "spock" )
computer_wins = 0
user_wins = 0
round = 1
print("Bienvenido al Piedra 🪨, papel 📄, tijera ✂️, largarto 🦎 y spock 🖖 creado por Sheldon Lee Cooper 🤓")
while True:
  print("*" * 10)
  print("ROUND",  round)
  print("*" * 10)
  print("Computadora ", computer_wins)
  print("*" * 10)
  print("Usuario", user_wins)
  print("*" * 10)
# lo que se muestra a empezar al programa
 
  
  #pedimos la opcion al juador
  user_option = input("Por favor, elige una de las opciones piedra, papel, tijera, lagarto o spock: ")
  #transformamos la selecicon del jugaor a minusculas
  user_option = user_option.lower()
  
  
  emojis = {
    "piedra": "🪨",
    "papel": "📄",
    "tijera": "✂️",
    "spock": "🖖",
    "lagarto": "🦎",
  }
  computer_option = random.choice(options)
  # una validacion si es que el usuario ingresa una opcion no valida
  if not user_option in options:
    print(f"Esa opcion no es valida, por favor elige una opcion valida" )
    
  # este else se ejecuta si el usuario elije una respuesta valida y se muestran las opciones de los dos jugadores. 
  else:
    if user_option == "piedra":
      print("¡Elegiste! =>", user_option, emojis["piedra"])
    if computer_option == "piedra":
      print("¡La computadora eligio! =>", computer_option, emojis["piedra"])
    if user_option == "lagarto":
      print("¡Elegiste! =>", user_option, emojis["lagarto"])
    if computer_option == "lagarto":
      print("¡La computadora eligio! =>", computer_option, emojis["lagarto"])
    if user_option == "tijera":
      print("¡Elegiste! =>", user_option, emojis["tijera"])
    if computer_option == "tijera":
      print("¡La computadora eligio! =>", computer_option, emojis["tijera"])
    if user_option == "spock":
      print("¡Elegiste! =>", user_option, emojis["spock"])
    if computer_option == "spock":
      print("¡La computadora eligio! =>", computer_option,emojis["spock"])
    if user_option == "papel":
      print("¡Elegiste! =>", user_option, emojis["papel"])
    if computer_option == "papel":
      print("¡La computadora eligio! =>", computer_option, emojis["papel"])
#esta ejecucion si es un empate
    if user_option == computer_option:
      print("Esto es un empate ")

#desde aqui se realizan las validaciones de quien gana 
    elif user_option == "piedra":
      if computer_option == "tijera":
        print("Piedra aplasta las tijeras ", emojis["tijera"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "spock":
        print("Spock Vaporiza la Piedra ", emojis["piedra"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "lagarto":
        print("Piedra aplasta al Lagarto ", emojis["lagarto"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "papel":
        print("Papel envuelve la piedra ", emojis["piedra"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      
    elif user_option == "papel":
      if computer_option == "piedra":
        print("Papel envuelve la Piedra ", emojis["piedra"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "spock":
        print("Papel refuta a spock ", emojis["spock"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "lagarto":
        print("Lagarto se come el Papel ",emojis["papel"])
        print("¡La maquina te Ganó!") 
        computer_wins += 1
      elif computer_option == "tijera":
        print("Tijera corta el Papel ",emojis["papel"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
    
    
    elif user_option == "tijera":
      if computer_option == "papel":
        print("Tijera corta el Papel ",emojis["papel"])
        print("Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "lagarto":
        print("Tijera Decapita al Lagarto ",emojis["lagarto"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "spock": 
        print("Spock aplasta las Tijeras " ,emojis["tijera"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "piedra":
        print("Piedra aplasta las Tijera ",emojis["tijera"])
        print("¡La maquina te Ganó!")  
        computer_wins += 1
        
    elif user_option == "lagarto":
      if computer_option == "papel":
        print("Papel aplasta al lagarto ",emojis["lagarto"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "tijera":
        print("Tijera decapita al lagarto ",emojis["lagarto"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "spock": 
        print("Lagarto Envenena a Spock ", emojis["spock"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "piedra":
        print("Piedra aplasta a Lagarto " ,emojis["lagarto"])
        print("¡La maquina te Ganó!")  
        computer_wins += 1
    
    elif user_option == "spock":
      if computer_option == "papel":
        print("Papel Refuta a Spock ", emojis["spock"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "tijera":
        print("Spock aplasta las Tijeras ",emojis["tijera"])
        print("¡La maquina te Ganó!")
        computer_wins += 1
      elif computer_option == "piedra":
        print("Spock Vaporiza la Piedra " , emojis["piedra"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
      elif computer_option == "lagarto":
        print("Lagarto envenena a Spock ", emojis["spock"])
        print("¡Ganaste a la maquina!")
        user_wins += 1
# añanimos victorias a los jugadores segun quien ganó
  if computer_wins == 2:
    print("-" * 35)
    print( f"¡El ganador es la computadora! { computer_wins} - {user_wins}")
    print("-" * 35)
    break
  if user_wins == 2:
    print("-" * 35)
    print(f"¡El ganador es el usuario!  { user_wins} - {computer_wins}")
    print("-" * 35)
    break
#añadimos el numero de rondas que estamos jugando
  round += 1
