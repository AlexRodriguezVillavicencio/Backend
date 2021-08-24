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




para django:
>python manage.py migrate
>python manage.py runserver

en el directorio setting agregar:
'rest_framework',
    'rest_framework.authtoken'

luego hacer el migrate para que se carguen las nuevas tablas:
<python manage.py migrate>

ahora creamos un superusuario:
>python manage.py createsuperuser
alexander alex12345




instalamos:
>pip install requests


