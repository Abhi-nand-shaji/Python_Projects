import smtplib


sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"  # Replace with your actual password or use environment variables
subject = "Python email test"
body = "I wrote an email! :D"

# Header
message = f"""From: Abhinand Shaji <{sender}>
To: Roopchand Shaji <{receiver}>
Subject: {subject}\n
{body}
"""

# Use environment variables or a configuration file for sensitive information
# password = os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()

    try:
        server.login(sender, password)
        print("Logged in...")
        server.sendmail(sender, receiver, message)
        print("Email has been sent!")

    except smtplib.SMTPAuthenticationError:
        print("Unable to sign in")




