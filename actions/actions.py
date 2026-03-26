import os
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class ActionConsultarMallaPDF(Action):
    def name(self) -> Text:
        return "action_consultar_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pregunta_usuario = tracker.latest_message.get('text')
        
        # Leer URL desde el .env (con fallback a localhost por seguridad)
        url_fastapi = os.getenv("FASTAPI_URL", "http://localhost:8000/api/chat/consultar")

        try:
            respuesta = requests.post(url_fastapi, json={"pregunta": pregunta_usuario}, timeout=120)

            if respuesta.status_code == 200:
                data = respuesta.json()
                texto_respuesta = data.get("respuesta", "No encontré información.")
                dispatcher.utter_message(text=texto_respuesta)
            else:
                dispatcher.utter_message(text="Lo siento, el sistema de información está en mantenimiento.")

        except requests.exceptions.ConnectionError:
            dispatcher.utter_message(text="Error de conexión: El motor de Inteligencia Artificial está apagado.")
            
        except requests.exceptions.Timeout:
            dispatcher.utter_message(text="El motor de IA tardó demasiado en responder. Por favor, intenta de nuevo.")

        return []