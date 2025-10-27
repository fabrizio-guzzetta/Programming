# Importa Blueprint da Flask: serve per organizzare e raggruppare le rotte dell’app
from flask import Blueprint

# Importa i blueprint secondari relativi ai corsi:
# - 'course_index_blueprint' gestisce la visualizzazione dei corsi
# - 'course_create_blueprint' gestisce la creazione di nuovi corsi
from .index import course_index_blueprint
from .create import course_create_blueprint


# Crea un "blueprint principale" per tutte le rotte che riguardano i corsi
# 'url_prefix' specifica che tutte le rotte registrate avranno il prefisso '/courses'
course_blueprint = Blueprint('course', __name__, url_prefix='/courses')

# Registra il blueprint che gestisce la pagina principale (lista dei corsi)
course_blueprint.register_blueprint(course_index_blueprint)

# Registra il blueprint che gestisce la creazione dei corsi
course_blueprint.register_blueprint(course_create_blueprint)
