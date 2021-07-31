Este es mi repositorio donde colocaré todos mis avances, sobre Backend, en el transcurso del bootcamp.


pip install { }  para instalar una libreria 
pip freeze       para saber que librerias tengo instalado
python -m venv { }   para crear un entorno virtual
deactivate   para salir del entorno virtual


para cmd:
.\vcodigo\Scripts\activate     para entrar a mi escritorio virtual
pip install bs4     (instalando bs4)
pip install requests     (instalando requests)

para linux:
source vcodigo/bin/activate

para git bash:
source vcodigo/scripts/activate
---------------------------------------------
import requests
from bs4 import BeautifulSoup  (mejor opción, hace menos pesado)



para levantar flask en la web de manera de desarrollo:
export FLASK_APP=main.py
export FLASK_ENV=development
flask run