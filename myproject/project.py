from flask import *
from flask_cors import CORS
import smtplib
# import threading

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def members():
    some_members = {'members': ['members1', 'members2', 'members3']}
    return jsonify(some_members)

@app.route('/applicants', methods=['POST'])
def applicant(): 
    data = request.json
    response_data = {'message': 'Data received!', 'data': data}
    # print(data)
    login(data)
    return jsonify(response_data)

#SMTP server start
def login(data):
    smtp_server = 'smtp.gmail.com'
    port = 587 #port for emails and SSL protocol
    myServer = smtplib.SMTP(smtp_server, port) #initialize server

    #host email and password
    host_email = 'akpannetwork@gmail.com'
    password = 'hqelfmbluipdsrsy'
    #client email 
    client_email = 'isedemidiong@gmail.com'

     #start SMTP server
    try:
        myServer.starttls()
        print('[Server Started]')
    except Exception as e:
        print(f'Error {e}')
        exit()

    #log in to email
    try:
        myServer.login(host_email, password)
        print('Login successful')
    except Exception as e:
        print(e)
        exit()
    send_application(myServer, host_email, client_email, data)

def send_application(myServer, host_email, client_email, data):
    # myServer, host_email, client_email = login()  

    #compose email
    subject = ('New Applicant')
    body = (data)
    composed_email = f'Subject: {subject}\n\n{body}'

    #send email
    try:
        myServer.sendmail(host_email, client_email, composed_email)
        print('Email Sent!')
    except Exception as e:
        print(e)
        exit()
        
    #close server
    myServer.quit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
