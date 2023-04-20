"""Modulo que provee un chat conversacional con la api de chatGPT"""
import sys
import openai

openai.api_key = "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"
TOP_P = 1
FREQ_PENALTY = 0
PRES_PENALTY = 0
STOP = None
MAX_TOKENS = 1024
TEMPERATURE = 0.75
NMAX = 1
MODEL_ENGINE = "text-davinci-003"


def get_answer(answer):
    """Funcion que retorna respuesta de la api"""

    # Se realiza un llamado a la api mediante la libreria "openai"
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=answer,
        max_tokens=MAX_TOKENS,
        n=NMAX,
        top_p=TOP_P,
        frequency_penalty=FREQ_PENALTY,
        presence_penalty=PRES_PENALTY,
        temperature=TEMPERATURE,
        stop=STOP
    )

    # Retornamos solo el texto de la respuesta
    return completion.choices[0].text


def run(prompt=""):
    """Funcion que ejecuta el codigo principal"""
    request = None
    # Declaro y asigno un valor booleano a la variable segun argumento
    is_convers = (sys.argv.count("--convers") > 0) | (prompt != "")

    # Obtengo el texto de la pregunta
    try:
        # Asigno el texto recibido del input
        request = input("You: ")
    except EOFError as error:
        print(f"Ha ocurrido un error: {error}")
        return

    # Valido y manipulo el texto de la pregunta
    try:
        # Devuelvo un error en caso de que la pregunta
        # esté vacia
        if request == "":
            raise ValueError("Cadena vacia")

        # Agrego "+You: " a la pregunta
        request = f"You: {request}"
    except ValueError as error:
        print(f"Ha ocurrido un error: {error}")
        return

    # Agrego la pregunta al prompt.
    # El prompt que comporta como un historial
    # Para el caso conversacional
    prompt += f"{request}\n"

    response = None
    try:
        # Asigno la respuesta de la api a "response"
        # En los argumentos paso el prompt en el caso
        # conversacional, o la pregunta en el caso contrario
        response = get_answer(prompt if is_convers else request)

        # Valido que la respuesta no esté vacia
        if response == "":
            raise ValueError("Respuesta vacia")

        # Manipulo la respuesta agregando "chatGPT: " y un color distintivo
        response = ":".join(response.split(":")[1:]).strip()
        response = f"chatGPT: \033[93m{response}\033[0m"
    except ValueError as error:
        print(f"Ha ocurrido un error: {error}")
        return
    except IndexError as error:
        print("Ha ocurrido un error con el índice")
        return

    # Agrego la respuesta al prompt.
    prompt += f"{response}\n"

    # Muestro en consola la respuesta
    print(response)

    # Llamo a la funcion "run" de forma recursiva.
    run(prompt if is_convers else "")


run()
