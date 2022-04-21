from http import server
import smtplib
from email.mime.text import MIMEText
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from .CreateHTMLTable import CreateHTMLTable
class SendEmail:

    email = 'bhaaface@gmail.com'
    password = 'tuoiyqmibkzwslcf'
    
    def send_email(self,subject,items,sender,receiver):
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(self.email,self.password)
        html = """
            <html><body><p>"""+subject+"""</p>
            <p>Here is your data:</p>
            """+CreateHTMLTable().html_table(items)+"""
            <p>Regards,</p>
            <p>Me</p>
            </body></html>
            """
        html = html.format(table=tabulate(items, headers="firstrow", tablefmt="html"))
        message = MIMEMultipart(
            "alternative", None, [ MIMEText(html,'html')])
        message['Subject'] = subject

        server.sendmail(sender,receiver,message.as_string())
        server.quit()
    
