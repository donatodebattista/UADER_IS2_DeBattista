#API key: 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

import openai
openai.api_key = "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"
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"


userText = input("Ingrese su consulta: ")

if(len(userText) > 0):
    print("You:", userText)
    completion = openai.Completion.create(engine=MODEL_ENGINE, 
                                          prompt=userText, 
                                          max_tokens=MAX_TOKENS, 
                                          n=NMAX, 
                                          top_p=TOP_P, 
                                          frequency_penalty=FREQ_PENALTY, 
                                          presence_penalty=PRES_PENALTY,
                                          temperature=TEMPERATURE,
                                          stop=STOP
                                          )
    print("ChatGPT:", completion.choices[0].text)
else:
    print("No puede ingresar una consulta vacía!")