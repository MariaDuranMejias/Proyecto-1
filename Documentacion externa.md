# Autores: [Franciny Cruz, Maria Duran]

Nombre del proyecto: [Proyecto 1, BlackJack Game]

Descripción del proyecto

Este codigo funciona como un juego de BlackJack o 21. Con opcion para un jugador o dos jugadores.

Diseño de la solución

Para la solucion de este problema, utilizamos el siguiente diagrama: https://lucid.app/lucidchart/ed9d48bd-e97a-44a9-a907-edc8c781d302/edit?viewport_loc=-155%2C-42%2C1707%2C768%2C0_0&invitationId=inv_f0512a76-27b7-4038-9630-100fdf6b3ec1

En el menu.py, se encuentra el menu principal con las opciones de juego con un jugador, juego con 2 jugadores, las reglas, los resultados y la opcion de salir. En el archivo de texto "jugadores.txt" se van a almacenar los nombres de los jugadores que se van a utilizar para que el jugador eliga entre los jugadores existentes. En el archivo "resultados.txt" se guardan los resultados de cada jugador y se imprimen cuando el jugador selecciona el nombre de un jugador existente.

El archivo ExtraerJugadores.py tiene la funcion Mostrar_Jugadores. Esta funcion abre el archivo "jugadores.txt", lo separa por lineas y revisa si la linea tiene la frase "Jugador:", si la tiene la guarda en una lista, luego elimina las lineas repetidas y muestra el resultado en una lista.

En el archivo juego1.py, primero se tiene la clase Card que es la que crea la carta con el simbolo y el numero. Luego se define la clase Deck que crea una baraja de cartas, dentro de ella tiene la funcion shuffle donde se revuelven las cartas y la funcion deal que es la que reparte una carta. Se define la clase Hand que es la que muestra las cartas del dealer y de (los) jugador(es). La funcion add _card es la que agrega una carta al dealer y al (los) jugador(es). Ademas, la funcion ajuste_de_as le asigna el valor a la carta A que puede ser 1 o 10.  Luego vienen las funciones, tomar_carta reparte una carta a quien la necesite, incluyendo el ajuste_de_as para la carta A. Mientras se este jugando, la funcion tomar_carta_o_parar le preguntara al (los) jugador(es) si desea(n) una carta si o no, si la respuesta es si, se utiliza la funcion tomar_carta para darle una carta al jugador y esto se preguntara hasta que el jugador diga que no, cuando el jugador dice que no, se imprime un mensaje diciendo que el jugador paro y que es turno del dealer. La funcion mostrar_carta muestra una carta del dealer y la otra la enmascara, mientras que muestra las 2 cartas del (los) jugador(es). La funcion mostrar_todas_las_cartas muestra todas las cartas del dealer y todas las cartas del (los) jugador(es). Las funciones player_gana, player_pierde y empate son las funciones que se utilizan para imprimir el resultado del juego y guardarlo en el archivo de texto, resultados.txt.

Luego empieza el juego, preguntando si desea jugar o no, si se selecciona "no" se devuelve al meno principal, si se selecciona "si" se pregunta si desea elegir un nombre existente o un nombre nuevo. En el caso, de 2 jugadores, se le pregunta lo mismo a ambos jugadores. Los nombres nuevos se guardan en un archivo de texto y luego se muestran cuando el jugador decide utilizar un nombre existente. Se muestran las estadisticas de ambos jugadores. Despues, se muestran las 2 cartas del dealer (una boca abajo), y las de (los) jugador(es). Se le pregunta a cada jugador si desea otra carta, hasta que diga que no se continua. El dealer pide cartas siempre y cuando sea menor  a 17. Se revisan los resultados y se muestra el ganador o perdedor. El resultado se almacena en un archivo de texto. El archivo juego2.py hace lo mismo que el juego1.py pero para 2 jugadores.

Manual de usuario

En esta aplicacion se puede elegir en el menu principal, la opcion de jugador con un jugador, con 2 jugadores, leer las instrucciones, mostrar los resultados de los jugadores o salir de la aplicacion. El juego permite que  cada jugador elija dentro del historial de jugadores, utilizar un jugador existente o crear uno nuevo. Tambien al terminar cada partida, le pregunta si desea jugar otra vez, de lo contrario lo devuelve al menu principal.

Consideraciones especiales

-   La aplicacion funciona al correr el menu.py
-   No se lograron implementar las manos especiales del 21 como tres sietes, cinco menores o blackjack.
-  Se debe mejorar el juego2.py para poder jugar con 2 jugadores correctamente, ya que dependiendo del resultado no se imprime quien gano. 

