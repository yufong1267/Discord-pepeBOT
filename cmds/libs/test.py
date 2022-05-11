import wikipedia

def send_email(sendto, subject, text):
    username = "b10517025@gemail.yuntech.edu.tw" # Change this!
    password = "b10517025" # Change this!
    for i in range(3):
        try:
            print("Sending Email to {} (trial {})...".format(sendto, i+1))
            import smtplib
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            msg = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail(username, sendto, msg)
            server.quit()
            print("Email sent!")
            break
        except Exception as e:
            print("Failed to send email due to Exception:")
            print(e)

if __name__=='__main__':
    send_email("a2583669@gmail.com", "EmailTitle", "EmailBody")
    