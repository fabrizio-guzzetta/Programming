from flask import Flask, render_template, redirect, session, request, flash
from connection import connect
import json

app = Flask(__name__)
app.secret_key = "Il gatto mi ha mangiato la lingua"

@app.context_processor
def layout_data():
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses_db")
    courses = cursor.fetchall()
    cursor.close()
    categories = set(map(lambda c: c['categoria'], courses)) 
    return {
        "courses": courses,
        "categories": categories
    }
    

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chi_siamo")
def chi_siamo():
   return render_template("chi_siamo.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        for element in request.form:
            if not request.form[element]:
                return render_template("auth/register.html", message=f"Il campo {element} è richiesto")
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO users_db(nome, cognome, email, password)VALUES(%s, %s, %s, %s)""", [request.form['username'], request.form['cognome'], request.form['email'], request.form['password']])
        connect.commit()

        cursor.close()

        session['username'] = request.form['username']
        session['cognome'] = request.form['cognome']
        session['email'] = request.form['email']
        session['password'] = request.form['password']

        return redirect(f"/login/{session['username']}")
    return render_template('auth/register.html')


@app.route("/login/<username>", methods=["POST", "GET"])
def dashboard(username):
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses_db")
    courses = cursor.fetchall()
    cursor.close()
    return render_template("auth/dashboard.html", message=f"Benvenuto{username}: complimenti,registrazione avvenuta con successo", username=username, cognome=session['cognome'], email=session['email'], password=session['password'], courses=courses)


@app.route("/createcourse", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        cursor = connect.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses_db")
        courses = cursor.fetchall()
        cursor.close()
        for course in courses:
            if not courses['id']:
                cursor = connect.cursor(dictionary=True)
                cursor.execute("""INSERT INTO courses_db(corso, categoria, number_participants, descrizione)VALUES(%s, %s, %s, %s)""", [request.form['corso'], request.form['categoria'], request.form['number_participants'], request.form['descrizione']])
                connect.commit()
                cursor.close()
                return render_template("corsi_utente.html")
            else:
                return render_template("auth/creacorso.html", message="Corso già esistente")
    return render_template("auth/creacorso.html")


@app.route("/deletecourse", methods=["POST", "GET"])
def delete():
    if request.method == "POST":
        curs_id= request.form['id']
        cursor = connect.cursor(dictionary=True)
        cursor.execute("""DELETE FROM courses_db WHERE id = %s""",[curs_id])
        connect.commit()
        cursor.close()
    return render_template("elimina_corsi.html")


@app.route("/login/admin/<username>", methods=["POST", "GET"])
def dashboard_admin(username):
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users_db WHERE nome = %s", [username])
    users = cursor.fetchall()
    cursor.execute("SELECT * FROM courses_db")
    courses = cursor.fetchall()
    cursor.close()
    
    if len(users) > 0:
        return render_template("auth/dashboard_admin.html", 
                             username_admin=username, 
                             username=username,
                             cognome=users[0]['cognome'], 
                             email=users[0]['email'], 
                             password=users[0]['pwd'],
                             courses=courses)
    else:
        return redirect("/")


@app.route("/login", methods=["POST"])
def login():

    for element in request.form:
        if not request.form[element]:
            return render_template("index.html", message=f"Il campo {element} è richiesto")

    session['email'] = request.form['email']
    session['password'] = request.form['password']
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users_db WHERE email = %s", [request.form['email']])
    users = cursor.fetchall()
    cursor.close()
    
    if len(users) == 0:
        return render_template("index.html", messaggio = "Credenziali Errate")
    
    if request.form['email'] != users[0]['email'] or request.form['password'] != users[0]['pwd']:
        return render_template("index.html", messaggio = "Credenziali Errate")
    
    session['cognome'] = users[0]['cognome']
    
    if users[0]['ruolo'].upper() != "UTENTE":
        return redirect(f"/login/admin/{users[0]['nome']}") 
    else:
        return redirect(f"/login/{users[0]['nome']}")

@app.route("/corsi")
def corsi():
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses_db")
    courses = cursor.fetchall()
    cursor.close()
    return render_template("pagina_corsi.html", courses=courses)


@app.route("/contatti", methods=["GET", "POST"])
def contatti():
    if request.method == "GET":
        return render_template("contatti.html")
    
    nome = (request.form.get("nome") or "").strip()
    cognome = (request.form.get("cognome") or "").strip()
    email = (request.form.get("email") or "").strip().lower()
    motivo = (request.form.get("motivo") or "").strip()
    messaggio = (request.form.get("messaggio") or "").strip()
    
    if not nome or not cognome:
        flash("Nome e cognome sono obbligatori", "danger")
        return redirect(url_for("contatti"))
    
    if not is_valid_email(email):
        flash("Email non valida", "danger")
        return redirect(url_for("contatti"))
    
    if not motivo:
        flash("Seleziona un motivo del contatto", "danger")
        return redirect(url_for("contatti"))
    
    if not messaggio:
        flash("Il messaggio non può essere vuoto", "danger")
        return redirect(url_for("contatti"))
    
    nuovo_messaggio = {
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "motivo": motivo,
        "messaggio": messaggio,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        try:
            with open('messaggi.json', 'r', encoding='utf-8') as file:
                messaggi = json.load(file)
        except FileNotFoundError:
            messaggi = []
        
        messaggi.append(nuovo_messaggio)
        
        with open('messaggi.json', 'w', encoding='utf-8') as file:
            json.dump(messaggi, file, ensure_ascii=False, indent=4)
        
        flash("Messaggio inviato con successo!", "success")
        return redirect(url_for("index"))
        
    except Exception as e:
        flash(f"Errore nel salvataggio: {str(e)}", "danger")
        return redirect(url_for("contatti"))


@app.route("/<username>/corsi_utente")
def corsi_utente(username):
    cursor = connect.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses_db")
    courses = cursor.fetchall()
    cursor.close()
#    if course['corso'] == request.form['id']:
    return redirect("/<username>/corsi")


def is_valid_email(addr: str) -> bool:
    if not addr:
        return False
    email = addr.strip().lower()
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    local, domain = email.split("@", 1)
    if not local or not domain:
        return False
    if local[0] == "." or local[-1] == "." or domain[0] == "." or domain[-1] == ".":
        return False
    if ".." in local or ".." in domain:
        return False
    if "." not in domain:
        return False
    for label in domain.split("."):
        if not label or label[0] == "-" or label[-1] == "-":
            return False
    return True


@app.route("/admin/newsletter", methods=["POST"])
def newsletter():  
    email = (request.form.get("email") or "").strip().lower()
    
    if not is_valid_email(email):
        flash("Email non valida.", "danger")
        return redirect(url_for("index"))
    
    cursor = connect.cursor(dictionary=True)
    
    
    cursor.execute("SELECT * FROM iscritti WHERE email = %s", [email])
    email_esistente = cursor.fetchone()
    
    if email_esistente:
        cursor.close()
        flash("L'email inserita è già presente", "warning")
        return redirect(url_for("index"))
    
  
    cursor.execute("INSERT INTO iscritti(email) VALUES(%s)", [email])
    connect.commit()
    cursor.close()
    
    flash("Iscrizione completata con successo!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
