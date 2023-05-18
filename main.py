from flask import Flask, render_template, request, flash, redirect

import smtplib
import email.message

app = Flask(__name__)
app.config['SECRET_KEY']= "PALAVRA-SECRETA"
@app.route("/")
def home():
    # return redirect("/")
    return render_template("html/login.html")

@app.route("/login", methods=['POST'])
def login():
    laboratorio = request.form.get('laboratorio')
    data = request.form.get('data')
    horario = request.form.get('horario')
    quantidade = request.form.get('quantidade')
    programa = request.form.get('programa')
    
    if (not laboratorio or not data or not horario or not quantidade or not programa):
        flash('Todos os campos sao obrigatórios.')
        return redirect("/")
    
    print(laboratorio)
    print(data)
    print(horario)
    print(quantidade)
    print(programa)

    # 
    corpo = """
    <h1>Laboratório Reservado</h1>
    <div> <b>Laboratorio: {{laboratorio}}</b> </div>
    <div> <b>Lata: {{data}}</b> </div>
    <div> <b>Lorario: {{horario}}</b> </div>
    <div> <b>Luantidade: {{quantidade}}</b> </div>
    <div> <b>Lrograma: {{programa}}</b> </div>
    """
    try:
        flash('Enviando formulário...')
        msg = email.message.Message()
        msg['Subject'] = "Assunto"
        msg['From'] = "" # preencher
        msg['To'] = "" # preencher
        password = "" # gerar senha nas configs do gmail. Ref: min 6:30 do video https://www.youtube.com/watch?v=N97q96BygUg&ab_channel=HashtagPrograma%C3%A7%C3%A3o 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo)

        s= smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'], password)
        s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    except Exception as e:
        print("Erro ao enviar e-mail:", str(e))
        flash('Erro ao enviar e-mail.')
        return redirect("/")
    print('email enviado')

    return render_template("html/acesso.html", laboratorio=laboratorio, data=data, horario=horario, quantidade=quantidade, programa=programa)

if __name__ in '__main__':
    app.run(debug=True)