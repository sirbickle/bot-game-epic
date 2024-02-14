import email.message
import smtplib
import pyautogui

def ExistsOnScreen(image):
    try:
        pyautogui.locateOnScreen(image)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def SendMailPossui():
    corpo_email = """
    <p>Você já possui esse jogo<p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Jogo já na biblioteca"
    msg['From'] = 'lima.ll621@gmail.com'
    msg['to'] = 'lima.ll621@gmail.com'
    senha = 'oivjughbdmgsocyq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(msg['From'], senha)
    server.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))
    print('email enviado')
    
def SendMailNaoPossui():
    corpo_email = """
    <p>Você adquiriu um novo jogo<p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Novo jogo adquirido"
    msg['From'] = 'lima.ll621@gmail.com'
    msg['to'] = 'lima.ll621@gmail.com'
    senha = 'oivjughbdmgsocyq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(msg['From'], senha)
    server.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))
    print('email enviado')

def SendMailErro():
    corpo_email = """
    <p>Algo deu errado<p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Erro"
    msg['From'] = 'lima.ll621@gmail.com'
    msg['to'] = 'lima.ll621@gmail.com'
    senha = 'oivjughbdmgsocyq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(msg['From'], senha)
    server.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))
    print('email enviado')