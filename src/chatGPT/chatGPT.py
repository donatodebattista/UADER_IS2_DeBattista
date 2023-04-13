""" ESTE MODULO PERMITE AL USUARIO REALIZAR CONSULTAS Y OBTENER RESPUESTAS UTILIZANDO LA API DE ChatGPT """

import sys
import openai

# Key de openai
openai.api_key = "API key aqui"

# PARAMETROS DE INICIACION
params = {
    "TOP_P" : 1,
    "FREQ_PENALTY" : 0,
    "PRES_PENALTY" : 0,    
    "STOP": ["You:","chatGPT:"],
    "MAX_TOKENS" : 1024,   # Longitud de la respuesta
    "TEMPERATURE" : 0.75,  # Parametro que determina la frecuencia de repeticion de las respuestas
    "NMAX": 1,             # Cantidad de respuestas generadas
    "MODEL_ENGINE" : "text-davinci-003"     # Modelo utilizado
}


def get_response(consulta, parametros):
    """ Crea el objeto de la clase openai en base a la consulta ingresada """
    completion = openai.Completion.create(engine = parametros ["MODEL_ENGINE"],
                                            prompt = consulta,
                                            max_tokens =parametros["MAX_TOKENS"],
                                            n =parametros["NMAX"],
                                            top_p =parametros["TOP_P"],
                                            frequency_penalty =parametros["FREQ_PENALTY"],
                                            presence_penalty =parametros["PRES_PENALTY"],
                                            temperature =parametros["TEMPERATURE"],
                                            stop =parametros["STOP"]
                                            )
    return completion



def start_chat(convers, historial_de_conversacion, parametros):
    """ Solicita una consulta y muestra en pantalla la respuesta obtenida luego de la llamada a la api """
    user_text = ""
    try: # Control del ingreso de la consulta del usuario

        user_text = input("Ingresa una consulta: ")
        print(f"You: {user_text}")

        # Se actualiza el historial de conversación
        historial_de_conversacion += f"You: {user_text}\n"

        if not user_text:
            # Error especifico de ingreso de cadena vacía
            raise ValueError("No puede ingresar una consulta vacía!")

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit()


# LLAMADA A LA FUNCION PARA OBTENER RESPUESTA
    try:
        if convers:  # en modo conversacion
            # se obtiene la respuesta en base a historial_de_conversacion
            respuesta = get_response(historial_de_conversacion, parametros)

        else:   # sin modo conversacion
            # se obtiene la respuesta en baso al texto ingresado
            respuesta = get_response(user_text, parametros)

    except Exception as error:
        print(f"Error: {error}")
        sys.exit()


# PREPARACIÖN DE LA RESPUESTA.
    try:
        respuesta = respuesta.choices[0].text

        # Se actualiza el historial de conversación:
        historial_de_conversacion += f"ChatGPT: {respuesta}"

        # Se eliminan posibles string no deseados al comienzo de la respuesta
        respuesta = respuesta.replace("Bot: ", "")
        respuesta = respuesta.replace("bot: ", "")
        respuesta = respuesta.replace("Interlocutor: ", "")
        respuesta = respuesta.replace("ChatGPT: ", "")

        print("ChatGPT: ", respuesta)


    except Exception as error:
        print(f"Error: {error}")
        sys.exit()

    return historial_de_conversacion



# INICIO DE LA EJECUCION DEL PROGRAMA
conversation_history = "\n"

if  len(sys.argv) == 2 and sys.argv[1] == "--convers": # Si se ingresa el argumento --convers
    print("MODO CONVERSACION ACTIVO")
    while True:
        conversation_history = start_chat(True, conversation_history, params)
else:
    while True:
        response = start_chat(False, "", params)
