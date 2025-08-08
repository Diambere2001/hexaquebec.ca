from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'ton_secret_key'

# Configuration mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'diamberek30@gmail.com'
app.config['MAIL_PASSWORD'] = 'zbymdnfxwrnjcezz'  

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')

        if not nom or not email or not message:
            flash('Veuillez remplir tous les champs', 'warning')
            return redirect(url_for('index'))

        msg = Message(subject=f"Nouveau message de {nom}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['hexaquebec80@gmail.com'])
        msg.body = f"Nom: {nom}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash('Message envoyé avec succès !', 'success')
        except Exception as e:
            flash(f'Erreur lors de l\'envoi : {str(e)}', 'danger')

        return redirect(url_for('index'))

    return render_template('index.html')


    

if __name__ == '__main__':
    app.run(debug=True)
