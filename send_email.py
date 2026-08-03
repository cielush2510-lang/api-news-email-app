import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "cielush2510@gmail.com"
    password = "ygxbauweewzdiutm"

    receiver = "cielush2510@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    send_email("Hello World")
