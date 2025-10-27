from flask import Blueprint, request, render_template

# Importa la funzione che gestisce la logica di creazione del corso
from controllers.courses import handle_creation


# Crea un Blueprint, cioè un modulo riutilizzabile di Flask, per la gestione della creazione dei corsi
course_create_blueprint = Blueprint('course_create', __name__)


# Definisce una route per la creazione di un corso
@course_create_blueprint.route('/create', methods=['POST'])
def create():
    # Estrae i dati dal form inviato tramite POST
    data = {
        'name': request.form['name'],   # Nome del corso
        'class': request.form['class']  # Classe associata al corso
    }

    # Passa i dati alla funzione che gestisce la creazione del corso
    result = handle_creation(data)

    # Se la creazione è andata a buon fine...
    if result is True:
        # ...renderizza la pagina "courses.html" con un messaggio di successo
        return render_template('courses.html', message='success')

    # Altrimenti, mostra la stessa pagina con un messaggio di errore
    return render_template('courses.html', message='error')

