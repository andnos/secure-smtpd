import smtplib

msg = """From: foobar@vmimage
To: ben@vmimage

Here's my message!
"""

server = smtplib.SMTP_SSL('vmimage', port=465)
server.set_debuglevel(1)
server.login('bcoe', 'foobar')
server.sendmail('foobar@localhost', ['ben@vmimage'], msg)
server.quit()