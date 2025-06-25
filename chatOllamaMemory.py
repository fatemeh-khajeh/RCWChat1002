
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time

template = """
    Tu es un professeur de sciences au lycée. Sois clair, concis et pédagogue. 
    Explique les réponses en utilisant des exemples simples et un langage adapté aux élèves de 16 ans.

    Voici l’historique de la conversation : {context}

    Question : {question}

    Réponse :

"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handleConversation():
    context=""
    print(" Bonjour , Je suis Alexndre, comment je peux vous aider? si vous n'avez pas de question svp ecriver 'quit'")
    while True:
        user_input = input("You :")
        if user_input.lower() == 'quit':
            break
        result = chain.invoke({"context":context , "question":user_input})
        for char in result:
            print(char, end="", flush=True)
            time.sleep(0.02)
        print()
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ =="__main__":
    handleConversation()        
        
            