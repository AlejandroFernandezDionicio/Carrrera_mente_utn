import pygame
from datos import*
from colores import*
from biblioteca import*

# LISTAS 
lista_preguntas = crear_listas(lista,"pregunta")
lista_respuestas_a = crear_listas(lista,"a")
lista_respuestas_b = crear_listas(lista,"b")
lista_respuestas_c = crear_listas(lista,"c")
lista_respuestas_correctas = crear_listas(lista,"correcta")
lista_ubicaciones_casillas = [(250,350),(370,350),(490,350),(610,350),(730,350),(850,350),(970,350),(1090,350)]
print(lista_ubicaciones_casillas[3])
# ETC
index = 0
score = 0

# INICIA PYGAME
pygame.init()

# SE CREA LA PANTALLA
pantalla = pygame.display.set_mode((1300, 900))
pygame.display.set_caption("VIDEOJUEGO")

# IMAGENES
posicion_carrera_utn = [0, 0]
imagen_carrera_utn = pygame.image.load("Captura.PNG")
imagen_carrera_utn = pygame.transform.scale(imagen_carrera_utn,(265, 200))
imagen_estudiante = pygame.image.load("—Pngtree—korea fashion figure beige coat_6245117.png")
imagen_estudiante = pygame.transform.scale(imagen_estudiante,(100, 100))

# Se CREA EL TIMER
tiempo = pygame.USEREVENT
segundos = "5"
pygame.time.set_timer(tiempo, 1000)
fin_tiempo = False

# SE CREA EL TEXTO
fuente_botones = pygame.font.SysFont("Arial", 30)
fuente_textos = pygame.font.SysFont("Arial", 25)

# SE CREAN LOS BOTONES
rect_comenzar = pygame.Rect((250,740), (300, 150))
rect_respuesta_a = pygame.Rect((270,140),(235,50))
rect_respuesta_b = pygame.Rect((547,140),(235,50))
rect_respuesta_c = pygame.Rect((847,140),(235,50))
rect_casilla_avanza = pygame.Rect((850,300),(100,100))
rect_casilla_retrocede = pygame.Rect((610,500),(100,100))
rect_estudiante = pygame.Rect((0,300,101,101))
# INICIA EL JUEGO
limite = False
mostrar_preguntas = False
mostrar_juego = True

while mostrar_juego:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            mostrar_juego = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)
            
            if rect_comenzar.collidepoint(evento.pos):
                mostrar_preguntas = True

            if rect_respuesta_a.collidepoint(evento.pos):
                if lista_respuestas_correctas[index] == "a":
                    index +=1
                    segundos = 5
                    score += 10
                    
                    respuesta_correcta = True
                elif lista_respuestas_correctas[index] != "a":
                    index +=1
                    
                    respuesta_correcta = False
                    segundos = 5
                if index >= len(lista_preguntas):
                    index = 0

            if rect_respuesta_b.collidepoint(evento.pos):
                if lista_respuestas_correctas[index] == "b":
                    index +=1
                    segundos = 5
                    score += 10
                    
                    respuesta_correcta = True
                elif lista_respuestas_correctas[index] != "b":
                    index +=1
                    
                    respuesta_correcta = False
                    segundos = 5
                if index >= len(lista_preguntas):
                    index = 0

            if rect_respuesta_c.collidepoint(evento.pos):
                if lista_respuestas_correctas[index] == "c": 
                    index +=1      
                    segundos = 5 
                    score += 10   
                    
                    respuesta_correcta = True
                elif lista_respuestas_correctas[index] != "c":
                    index +=1
                       
                    respuesta_correcta = False     
                    segundos = 5          
                if index >= len(lista_preguntas):
                    index = 0   

        if evento.type == pygame.USEREVENT:
            if evento.type == tiempo:
                if mostrar_preguntas == True:
                    if fin_tiempo == False:
                        segundos = int(segundos) - 1
                        if int(segundos) == 0:
                            segundos = 5
                            index += 1
        

    pantalla.fill(COLOR_CELESTE_OSCURO)

    pygame.draw.rect(pantalla, COLOR_CELESTE_CLARO, rect_comenzar)
    pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, (270, 10, 830, 190))
    pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_a)
    pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_b)
    pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_c)
    pygame.draw.rect(pantalla, COLOR_NARANJA, (250,300,100,300))
    pygame.draw.rect(pantalla, COLOR_VERDE_CLARO, (370,300,100,300))
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (490,300,100,300))
    pygame.draw.rect(pantalla, COLOR_CELESTE, rect_casilla_retrocede)
    pygame.draw.rect(pantalla, COLOR_CELESTE, (610,300,100,100))
    pygame.draw.rect(pantalla, COLOR_ROJO, (730,300,100,300))
    pygame.draw.rect(pantalla, COLOR_VIOLETA, rect_casilla_avanza)
    pygame.draw.rect(pantalla, COLOR_VIOLETA, (850,500,100,100))
    pygame.draw.rect(pantalla, COLOR_MARRON, (970,300,100,300))
    pygame.draw.rect(pantalla, COLOR_ROSA,(1090,300,100,300))
    pygame.draw.rect(pantalla, COLOR_CELESTE_OSCURO, (250,400,1000,100))
    pygame.draw.rect(pantalla, COLOR_ROJO, rect_estudiante)

    texto_comenzar = fuente_botones.render("COMENZAR", True, COLOR_NEGRO)
    texto_segundos = fuente_botones.render(str(segundos), True, COLOR_BLANCO)
    texto_tiempo = fuente_botones.render("TIEMPO:", True, COLOR_BLANCO)
    texto_score = fuente_textos.render(str(score), True, COLOR_BLANCO)
    texto_puntaje = fuente_textos.render("PUNTAJE:",True, COLOR_BLANCO)
    texto_salida = fuente_textos.render("Salida", True, COLOR_NEGRO)
    texto_avanza_1 = fuente_textos.render("Avanza 1", True, COLOR_NEGRO)
    texto_retrocede_1 = fuente_textos.render("Retrocede 1", True, COLOR_NEGRO)


    pantalla.blit(texto_comenzar, (310, 795))
    pantalla.blit(texto_tiempo, (1110, 50))
    pantalla.blit(texto_segundos, (1235, 50))
    pantalla.blit(texto_score,(1235, 100))
    pantalla.blit(texto_puntaje,(1110,100))
    pantalla.blit(texto_avanza_1,(848,370))
    pantalla.blit(texto_retrocede_1, (590,570))
    pantalla.blit(imagen_estudiante, rect_estudiante)
    pantalla.blit(texto_salida,(120,360))
    pantalla.blit(imagen_carrera_utn, (posicion_carrera_utn))


    if mostrar_preguntas:
        texto_preguntas = fuente_textos.render(lista_preguntas[index], True, COLOR_AMARILLO)
        texto_respuestas_a = fuente_textos.render(lista_respuestas_a[index], True, COLOR_AMARILLO)
        texto_respuestas_b = fuente_textos.render(lista_respuestas_b[index], True, COLOR_AMARILLO)
        texto_respuestas_c = fuente_textos.render(lista_respuestas_c[index], True, COLOR_AMARILLO)

        pantalla.blit(texto_preguntas, (370, 50))
        pantalla.blit(texto_respuestas_a, (270, 150))
        pantalla.blit(texto_respuestas_b, (550, 150))
        pantalla.blit(texto_respuestas_c, (850, 150))

    pygame.display.flip()

pygame.quit()