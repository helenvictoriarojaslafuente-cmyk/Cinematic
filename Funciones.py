#2_Funciones

peliculas = {}
Acción = {
    "The Killer (El asesino)": ["Accion", 1989, 5],
    "The Dark Knight (El caballero oscuro)": ["Accion", 2008, 5],
    "Mission: Impossible - Fallout": ["Accion", 2018, 5],
    "The Raid (La redada)": ["Accion", 2012, 5],
    "Speed (Máxima velocidad)": ["Accion", 1994, 5],
    "Baby Driver": ["Accion", 2017, 5],
    "John Wick": ["Accion", 2014, 4],
    "Predator (Depredador)": ["Accion", 1987, 5],
    "Léon: The Professional": ["Accion", 1994, 4]}
Comedia = {
    "The Nice Guys (Dos tipos peligrosos)": ["Comedia", 2016, 4],
    "What We Do in the Shadows": ["Comedia", 2014, 5],
    "Hot Fuzz (Arma fatal)": ["Comedia", 2007, 5],
    "The Grand Budapest Hotel": ["Comedia", 2014, 5],
    "Ghostbusters (Los cazafantasmas)": ["Comedia", 1984, 4],
    "Son como niños (Grown Ups)": ["Comedia", 2010, 5],
    "Knives Out (Entre navajas y secretos)": ["Comedia", 2019, 5],
    "Y dónde están las rubias? (White Chicks)": ["Comedia", 2004, 5],
    "Tropic Thunder": ["Comedia", 2008, 4],
    "Game Night (Noche de juegos)": ["Comedia", 2018, 4]}
Drama = {
    "Tár": ["Drama", 2022, 4],
    "Anatomy of a Fall (Anatomía de una caída)": ["Drama", 2023, 5],
    "The Zone of Interest (Zona de interés)": ["Drama", 2023, 3],
    "12 Angry Men (12 hombres en pugna)": ["Drama", 1957, 4],
    "The Truman Show": ["Drama", 1998, 3],
    "The Whale (La ballena)": ["Drama", 2022, 5],
    "Manchester by the Sea": ["Drama", 2016, 5],
    "Amadeus": ["Drama", 1984, 5],
    "The Social Network (Red social)": ["Drama", 2010, 4],
    "One Flew Over the Cuckoo's Nest": ["Drama", 1975, 4]}
Ciencia_Ficción = {
    "Coherence": ["Ciencia Ficción", 2013, 4],
    "Annihilation (Aniquilación)": ["Ciencia Ficción", 2018, 5],
    "Snowpiercer": ["Ciencia Ficción", 2013, 4],
    "The Martian (Misión rescate)": ["Ciencia Ficción", 2015, 5],
    "Ex Machina": ["Ciencia Ficción", 2014, 5],
    "Looper (Asesinos del futuro)": ["Ciencia Ficción", 2012, 4],
    "District 9 (Sector 9)": ["Ciencia Ficción", 2009, 4],
    "Source Code (8 minutos antes de morir)": ["Ciencia Ficción", 2011, 4],
    "Moon (En la Luna)": ["Ciencia Ficción", 2009, 4],
    "Avatar": ["Ciencia Ficción", 2009, 8]}
Fantasía = {
    "Harry Potter and the Sorcerer's Stone": ["Fantasía", 2001, 5],
    "The Fall (El sueño de Alejandría)": ["Fantasía", 2006, 4],
    "The Green Knight (El caballero verde)": ["Fantasía", 2021, 5],
    "A Monster Calls (Un monstruo viene a verme)": ["Fantasía", 2016, 5],
    "Howl's Moving Castle (El increíble castillo vagabundo)": ["Fantasía", 2004, 5],
    "Kubo and the Two Strings": ["Fantasía", 2016, 5],
    "Edward Scissorhands (El joven manos de tijera)": ["Fantasía", 1990, 5],
    "The NeverEnding Story (La historia sin fin)": ["Fantasía", 1984, 5],
    "Guillermo del Toro's Pinocchio": ["Fantasía", 2022, 5],
    "Mary Poppins": ["Fantasía", 1964, 5]}
Terror = {
    "Talk to Me (Háblame)": ["Terror", 2022, 4],
    "Verdad o reto (Truth or Dare)": ["Terror", 2017, 4],
    "The Witch (La bruja)": ["Terror", 2015, 4],
    "Smile (Sonríe)": ["Terror", 2022, 4],
    "Tarot": ["Terror", 2024, 4],
    "It": ["Terror", 2017, 5],
    "The Invisible Man (El hombre invisible)": ["Terror", 2020, 4],
    "Halloween": ["Terror", 1978, 4],
    "The Exorcist (El exorcista)": ["Terror", 1973, 4],
    "Late Night with the Devil": ["Terror", 2023, 4]}
Romance = {
    "Past Lives (Vidas pasadas)": ["Romance", 2023, 5],
    "Challengers (Desafiantes)": ["Romance", 2024, 5],
    "Before Sunset (Antes del atardecer)": ["Romance", 2004, 5],
    "The Worst Person in the World (La peor persona del mundo)": ["Romance", 2021, 5],
    "Palm Springs": ["Romance", 2020, 5],
    "Amélie": ["Romance", 2001, 5],
    "Notting Hill": ["Romance", 1999, 5],
    "Portrait of a Lady on Fire": ["Romance", 2019, 5],
    "Brokeback Mountain": ["Romance", 2005, 5],
    "Romeo + Juliet": ["Romance", 1996, 5]}
Animación = {
    "Spider-Man: Into the Spider-Verse": ["Animación", 2018, 5],
    "Inside Out (Intensa-Mente)": ["Animación", 2015, 5],
    "Zootopia (Zootrópolis)": ["Animación", 2016, 5],
    "Ratatouille": ["Animación", 2007, 5],
    "Toy Story": ["Animación", 1995, 5],
    "Finding Nemo (Buscando a Nemo)": ["Animación", 2003, 5],
    "Shrek": ["Animación", 2001, 5],
    "Up: Una aventura de altura": ["Animación", 2009, 5],
    "How to Train Your Dragon (Cómo entrenar a tu dragón)": ["Animación", 2010, 5],
    "Frozen": ["Animación", 2013, 5]}
Musical = {
    "Sing Street": ["Musical", 2016, 5],
    "Wonka": ["Musical", 2023, 5],
    "Tick, Tick... Boom!": ["Musical", 2021, 5],
    "Sweeney Todd": ["Musical", 2007, 5],
    "Cabaret": ["Musical", 1972, 5],
    "Yesterday": ["Musical", 2019, 5],
    "Hairspray": ["Musical", 2007, 5],
    "The Phantom of the Opera": ["Musical", 2004, 5],
    "Mamma Mia!": ["Musical", 2008, 5],
    "Annette": ["Musical", 2021, 5]}
Documental = {
    "Free Solo": ["Documental", 2018, 5],
    "13th": ["Documental", 2016, 5],
    "Won't You Be My Neighbor?": ["Documental", 2018, 5],
    "Blackfish": ["Documental", 2013, 5],
    "Fire of Love (Volcanes: La tragedia de Katia y Maurice Krafft)": ["Documental", 2022, 5],
    "Still: A Michael J. Fox Movie": ["Documental", 2023, 5],
    "The Deepest Breath (Al fondo de cada respiración)": ["Documental", 2023, 5],
    "Man on Wire": ["Documental", 2008, 5],
    "The Act of Killing": ["Documental", 2012, 5],
    "March of the Penguins": ["Documental", 2005, 5]}
peliculas = {}
peliculas["Avengers: Doomsday"] = ["Accion", 2027, 0]
peliculas["The Batman - Part II"] = ["Accion, 2028, 0"]
peliculas["Sherlock Holmes 3"] = ["Comedia", 2028, 0]
peliculas["Almas en pena (Inisherin 2)"] = ["Comedia", 2029, 0]
peliculas["The Drama"] = ["Drama", 2027, 0]
peliculas["Marty Supreme"] = ["Drama", 2028, 0]
peliculas["Avatar 4"] = ["Ciencia Ficcion", 2028, 0]
peliculas["Blade Runner - Nueva Era"] = ["Ciencia Ficcion", 2027, 0]
peliculas["Wicked - Part II"] = ["Fantasía", 2027, 0]
peliculas["The Chronicles of Narnia"] = ["Fantasía", 2028, 0]
peliculas["El Exorcista: Deceit"] = ["Terror", 2027, 0]
peliculas["Smile 3"] = ["Terror", 2028, 0]
peliculas["We Live in Time"] = ["Romance", 2027, 0]
peliculas["Normal People - Pelicula"] = ["Romance", 2028, 0]
peliculas["Frozen 3"] = ["Animación", 2027, 0]
peliculas["Coco 2"] = ["Animación", 2029, 0]
peliculas["Michael (Michael Jackson Bio)"] = ["Musical", 2027, 0]
peliculas["Wonka 2"] = ["Musical", 2029, 0]
peliculas["F1: Drive to Survive 2027"] = ["Documental", 2027, 0]
peliculas["Inside Pixar - Vol 2"] = ["Documental", 2028, 0]

peliculas.update(Acción)
peliculas.update(Comedia)
peliculas.update(Drama)
peliculas.update(Ciencia_Ficción)
peliculas.update(Fantasía)
peliculas.update(Terror)
peliculas.update(Romance)
peliculas.update(Animación)
peliculas.update(Musical)
peliculas.update(Documental)
reseñas = {"The Killer (El asesino) (1989)": ["Una obra maestra del cine de acción, con una narrativa intensa y actuaciones memorables. - 5 por Comunidad"],}
sugerencias_usuarios = []
calificaciones_usuarios = {}
def menu_cliente(usuario_activo):
    while True:
        print(f"Perfil : {usuario_activo.upper()} - CARTELERA")
        print("1. Explorar por Géneros")
        print("2. Los más Recomendados")
        print("3. Buscar Pelicula")
        print("4. Calificar y Dejar Reseña")
        print("5. Próximos Lanzamientos Exclusivos")
        print("6. Proponer Nueva Película")
        print("7. Ver Opiniones de la Comunidad")
        print("8. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("")
            print("GÉNEROS")
            generos = ["Accion", "Comedia", "Drama", "Ciencia Ficción", "Fantasía", "Terror", "Romance", "Animación", "Musical", "Documental"]
            contador = 1
            for g in generos:
                print(f"{contador}. {g}")
                contador = contador + 1
            try:
                eleccion = int(input("  Ingrese el número del género que desea ver: "))
                if eleccion >= 1 and eleccion <= len(generos):
                    genero_seleccionado = generos[eleccion - 1]
                    print(f"Películas de género {genero_seleccionado.upper()}:")
                    for p in peliculas: 
                        datos = peliculas[p]
                        if datos[0] == genero_seleccionado and datos[1] <= 2026:
                            print(f"- {p} ({datos[1]}) - Calificación: {datos[2]} estrellas")
                else: 
                    print("Opción inválida. Por favor, seleccione un número válido.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif opcion == "2":
            print("")
            print("Los mas recomendados:")
            generos_mostrados = []
            for p in peliculas: 
                datos = peliculas[p]
                if len(datos) == 3:
                    if datos[2] == 5 and datos[1] <= 2026 and datos[0] not in generos_mostrados:
                        generos_mostrados.append(datos[0])
                        print(f"{p} ({datos[1]}) - [Género: {datos[0]}] Calificación: {datos[2]} estrellas")
        elif opcion == "3":
            print("BUSCAR PELÍCULA POR NOMBRE")
            busqueda = input("Ingrese el nombre de la película que desea buscar: ").strip().lower()
            encontrada = False       
            for p in peliculas:
                if busqueda in p.lower():
                    datos = peliculas[p]
                    if datos[1] <= 2026:
                        print(f"Película encontrada: {p} ({datos[1]}) - [Género: {datos[0]}] Calificación: {datos[2]} estrellas")
                    else:
                        print(f"La película {p} aún no ha sido estrenada. Estreno previsto para {datos[1]}")
                    encontrada = True
            if not encontrada:
                print("No se encontró ninguna película con ese nombre.")
        elif opcion == "4":
            peli = input("Pelicula a calificar: ").strip()
            encontrada = False
            for p in peliculas:
                if p.lower() == peli.lower() and peliculas[p][1] <= 2026:
                    encontrada = p
                    break
            if encontrada: 
                try: 
                    nota = int(input("Estrellas (1-5): ").strip())
                    if nota >= 1 and nota <= 5:
                        comentario = input("Escriba su reseña: ").strip()
                        if encontrada not in reseñas: 
                            reseñas[encontrada] = []
                        reseñas[encontrada].append(f"{comentario} - {nota} por {usuario_activo}")
                        print("¡Tu opinión ha sido compartida!")
                    else: 
                        print("La nota debe ser del 1 al 5.")
                except ValueError:
                    print("Ingresa un número válido.")
            else: 
                print("Pelicula no disponible para calificar o aún no estrenada.")
        elif opcion == "5": 
            print("Proximos Estrenos") 
            for p in peliculas:
                datos = peliculas[p]
                if len(datos) > 1:  
                    if datos[1] > 2026:
                        print(f"Estreno en {datos[1]}: {p} [Género: {datos[0]}]")
        elif opcion == "6": 
            idea = input("Escriba el nomnbre de la pelicula que desea proponer: ").strip()
            if idea: 
                sugerencias_usuarios.append(f"´{idea}´ propuesto por {usuario_activo}")
                print("¡Idea guardada en el buzón!")
            else: 
                print("La sugerencia no puede quedar vacia.")
        elif opcion == "7": 
            print("Reseñas de la comunidad")
            if len(reseñas) == 0: 
                print("Aún no hay opiniones de usuarios.")
            else: 
                for peli_clave in reseñas:
                    print(f"Pelicula: {peli_clave}")
                    for r in reseñas[peli_clave]:
                        print(f" {r}")
        elif opcion == "8": 
            print("Cerrando sesión de cartelera...")
            break
        else: 
            print("Opcion inválida.")
        print("")