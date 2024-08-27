import re

#  expresiones regulares para identificar saludos y diferentes tipos de preguntas sobre el clima
saludos = re.compile(r"\b(hola|buenos días|buenas tardes|buenas noches|qué tal|hey)\b", re.IGNORECASE)
pregunta_clima_hoy = re.compile(r"\b(clima|tiempo|pronóstico)\b", re.IGNORECASE)
pregunta_clima_manana = re.compile(r"\b(mañana|futuro|próximo día)\b", re.IGNORECASE)
pregunta_sol = re.compile(r"\b(sol|soleado|brillante)\b", re.IGNORECASE)

# Mensaje de bienvenida
print("Chatbot: ¡Hola! ¿Cómo puedo ayudarte hoy?")

# Esperar a que el usuario introduzca un saludo para iniciar la conversación
entrada_usuario = input("Tú: ")

if saludos.search(entrada_usuario):
    print("Chatbot: ¡Hola! Puedes preguntarme sobre el clima de hoy, de mañana, o sobre el sol.")
    conteo_preguntas = 0
    
    while conteo_preguntas < 3:  # Permitir hasta 3 preguntas
        entrada_usuario = input("Tú: ")
        if pregunta_clima_hoy.search(entrada_usuario) and not pregunta_clima_manana.search(entrada_usuario) and not pregunta_sol.search(entrada_usuario):
            print("Chatbot: El clima está soleado hoy con posibilidad de lluvia por la tarde.")
        elif pregunta_clima_manana.search(entrada_usuario):
            print("Chatbot: Para mañana se espera que esté parcialmente nublado con temperaturas entre 18 y 23 grados.")
        elif pregunta_sol.search(entrada_usuario):
            print("Chatbot: Sí, el sol estará presente la mayor parte del día hoy.")
        else:
            print("Chatbot: No estoy seguro de eso. Por favor, pregunta sobre el clima de hoy, de mañana, o sobre el sol.")
        
        conteo_preguntas += 1
        
        if conteo_preguntas < 3:
            print("Chatbot: ¿Tienes otra pregunta?")
    
    print("Chatbot: ¡Fue un placer hablar contigo! ¡Que tengas un gran día!")
else:
    print("Chatbot: No reconocí un saludo. Por favor, inicia la conversación con un saludo.")
