playlist = {}
playlist ["Canciones"] = []

def app ():
    print ("\nPlaylist de artista y sus canciones\n")
    print ("Agregar artista\n")
    
    agregarPlaylist = True
    while agregarPlaylist:
        nombre_playlist = input ("¿Como desea nombre del 'artista'? \n").capitalize()
        if nombre_playlist:
            playlist ["Artista"] = nombre_playlist
            agregarPlaylist = False 
            
            agregarCancion ()

def agregarCancion():
    print ("\nAgregar canciones del artista\n")
    
    agregarCancion = True
    while agregarCancion:
        nombre_playlist  = playlist ["Artista"]
        pregunta = f"Agregar canciones para la playlist {nombre_playlist}\n"
        pregunta += "Escribe 'X' para dejar de agregar canciones\n"
        cancion = input(pregunta).capitalize()
        
        if cancion == "X":
            agregarCancion = False
            # Mostrar resumen de canciones
            mostrarResumen()
        else:
            #Agregar Canciones a la playlist
            playlist ["Canciones"].append(cancion)

def mostrarResumen():
    nombre_playlist  = playlist ["Artista"]
    print (f"Playlist \n{nombre_playlist}")
    print ("\nCanciones")
    for cancion in playlist["Canciones"]:
        print (cancion)          
            
app()