questions = {
    1: {
        "pregunta": "¿Prefieres trabajar en equipo o en solitario?",
        "opciones": ["a) En equipo", "b) En solitario", "c) Depende de la situación", "d) No estoy seguro"],
        "puntos": [2, 1, 3, 0],
    },
    2: {
        "pregunta": "¿Qué animal te indentifica mejor?",
        "opciones": ['a) León', 'b) Zorro', 'c) Delfín', 'd) Águila'],
        "puntos": [1, 2, 3, 0],
    },
    3: {
        "pregunta": "¿Eres más de seguir las reglas o de cuestionarlas?",
        "opciones": ['a) Seguir las reglas', 'b) Cuestionar las reglas', 'c) Ambas, dependiendo la situación', 'd) No estoy seguro'],
        "puntos": [1, 2, 3, 0],
    },
    4: {
        "pregunta": "¿Qué actividad te gusta más?",
        "opciones": ['a) Resolver problemas matemáticos', 'b) Leer y escribir', 'c) Dibujar o pintar', 'd) Hacer deporte'],
        "puntos": [2, 1, 3, 0],
    },
    5: {
        "pregunta": "¿Te gusta la tecnología o la informática?",
        "opciones": ['a) Sí, me apasiona', 'b) No me interesa demasiado', 'c) Me interesa, pero no tanto como otras cosas', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    6: {
        "pregunta": "¿Prefieres trabajar en un lugar tranquilo o con mucha actividad?",
        "opciones": ['a) Lugar tranquilo', 'b) Con mucha actividad', 'c) Depende la situación', 'd) No estoy seguro'],
        "puntos": [1, 2, 3, 0],
    },
    7: {
        "pregunta": "¿Qué elemento te representa mejor?",
        "opciones": ['a) Agua', 'b) Tierra', 'c) Aire', 'd) Fuego'],
        "puntos": [2, 1, 3, 0],
    },
    8: {
        "pregunta": "¿Eres más de planificar o de improvisar?",
        "opciones": ['a) Planificar', 'b) Improvisar', 'c) Ambas, dependiendo de la situación', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    9: {
        "pregunta": "¿Qué tipo de música prefieres",
        "opciones": ['a) Clásica', 'b) Rock o pop', 'c) Jazz o blues', 'd) Reggae o música latina'],
        "puntos": [1, 2, 3, 0],
    },
    10: {
        "pregunta": "¿Te gusta trabajar con las manos?",
        "opciones": ['a) Sí, me gusta mucho', 'b) No me gusta mucho', 'c) Me gusta, pero no tanto como otras cosas', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    11: {
        "pregunta": "¿Qué prefieres hacer en tu tiempo libre?",
        "opciones": ['a) Leer o ver películas', 'b) Practicar deportes o hacer ejercicio', 'c) Salir con amigos o familiares', 'd) Otros'],
        "puntos": [1, 2, 3, 0],
    },
    12: {
        "pregunta": "¿Qué tipo de situaciones te generan mayor ansiedad?",
        "opciones": ['a) Hablar en público', 'b) Conocer gente nueva', 'c) Trabajar bajo presión', 'd) No suelo sentir ansiedad'],
        "puntos": [2, 1, 3, 0],
    },
    13: {
        "pregunta": "¿Qué tipo de ambiente de trabajo prefieres?",
        "opciones": ['a) Formal y estructurado', 'b) Creativo y dinámico', 'c) Relajado y flexible', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    14: {
        "pregunta": "¿Cuál de estas descripciones te describe mejor?",
        "opciones": ['a) Soy una persona analítica y crítica', 'b) Soy una persona creativa y artística', 'c) Soy una persona empática y comprensiva', 'd) Soy una persona organizada y detallista'],
        "puntos": [1, 2, 3, 0],
    },
    15: {
        "pregunta": "¿Te gusta aprender sobre ciencias naturales y el mundo que nos rodea?",
        "opciones": ['a) Sí, me encanta', 'b) No me interesa mucho', 'c) Me interesa, pero no tanto como otras cosas', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    16: {
        "pregunta": "¿Qué tipo de libros o películas te gustan más?",
        "opciones": ['a) Drama o suspenso', 'b) Ciencia ficción o fantasía', 'c) Comedia o romance', 'd) Documentales o biografías'],
        "puntos": [1, 2, 3, 0],
    },
    17: {
        "pregunta": "¿Te gusta ayudar a los demás?",
        "opciones": ['a) Sí, mucho', 'b) No tanto', 'c) Me gusta, pero no tanto como otras cosas', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },
    18: {
        "pregunta": "¿Eres más de trabajar con la mente o con el cuerpo?",
        "opciones": ['a) Con la mente', 'b) Con el cuerpo', 'c) Ambos, dependiendo de la situación', 'd) No estoy seguro'],
        "puntos": [1, 2, 3, 0],
    },
    19: {
        "pregunta": "¿Qué habilidades crees que son tus fortalezas?",
        "opciones": ['a) Capacidad analítica', 'b) Creatividad', 'c) Empatía', 'd) Organización y atención al detalle'],
        "puntos": [2, 1, 3, 0],
    },
    20: {
        "pregunta": "¿Te interesa aprender sobre leyes y cómo funcionan los sistemas legales?",
        "opciones": ['a) Sí, me parece interesante', 'b) No me interesa mucho', 'c) Me interesa, pero no tanto como otras cosas', 'd) No estoy seguro'],
        "puntos": [2, 1, 3, 0],
    },

}

questions_size = len(questions)

welcome_message = "\n¡Bienvenido a Decide tu destino!\n\n Esta aplicación te ayudará a determinar qué carrera universitaria se adapta más \n a tus intereses y habilidades. A continuación, te haremos una serie de preguntas\n utilizando metáforas para que puedas reflexionar sobre tus preferencias y \n motivaciones. Es importante que respondas de forma honesta y sin prejuicios para \n el resultado sea lo más preciso posible. Una vez que hayas completado las \n preguntas, te diremos qué carrera es la que más se ajusta a tus respuestas. \n\n ¡Empecemos!"

questions_colors = ["#da1e37", "#52b788", "#4361ee", "#ffd60a"]

carrers = {
    "Abogado": {"min": 22, "max": 26},
    "Administración": {"min": 16, "max": 20},
    "Arquitectura": {"min": 27, "max": 31},
    "Artes Visuales para la Expresión Fotográfica": {"min": 22, "max": 26},
    "Artes Visuales para la Expresión Plástica": {"min": 22, "max": 26},
    "Biología": {"min": 27, "max": 31},
    "Ciencias y Artes Culinarias": {"min": 22, "max": 26},
    "Contaduría Pública": {"min": 16, "max": 20},
    "Cultura Física y Deportes": {"max": 16},
    "Diseño para la Comunicación Gráfica": {"min": 22, "max": 26},
    "Enfermería": {"min": 27, "max": 31},
    "Ingeniería Civil": {"min": 27, "max": 31},
    "Ingeniería en Computación": {"min": 22, "max": 26},
    "Ingeniería en Comunicación Multimedia": {"min": 22, "max": 26},
    "Ingeniería en Telemática": {"min": 22, "max": 26},
    "Ingeniería en Videojuegos": {"min": 22, "max": 26},
    "Médico Cirujano y Partero": {"min": 27, "max": 31},
    "Nutrición": {"min": 22, "max": 26},
    "Psicología": {"min": 27, "max": 31},
    "Turismo": {"max": 16}
}

button_bg = "#00f5d4"
button_fg = "black"
button_font = ("Arial", 14, "bold")

question_options_size = 4

def get_question(index):

    return questions.get(index)["pregunta"]

def get_options(index):

    return questions.get(index)["opciones"]


def get_points(index):

    return questions.get(index)["puntos"]