from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu_email@example.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    #Enviando e-mail
    msg = Message('Assunto do E-mail', sender='seu_email@example.com', recipients=[email])
    msg.body = f'Olá {name}, este é um exemplo de e-mail enviado pelo Flask-Mail.'
    mail.send(msg)

    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
