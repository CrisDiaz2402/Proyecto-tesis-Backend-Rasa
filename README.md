como activar rasa correctamente:
py -3.10 -m venv venv-rasa

.\venv-rasa\Scripts\activate

python --version

python -m rasa train

Esta de aqui es para hacer pruebas en consola: python -m rasa shell

Esta de aqui es para ejecutar como servidor: python -m rasa run --enable-api --cors "*"