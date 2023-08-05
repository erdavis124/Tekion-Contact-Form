from flask import Flask, render_template, request, redirect
import smtplib
import xml.etree.ElementTree as ET
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')

    # Create XML
    root = ET.Element("root")
    ET.SubElement(root, "firstName").text = fname
    ET.SubElement(root, "lastName").text = lname
    ET.SubElement(root, "email").text = email

    xml_string = ET.tostring(root, encoding='utf8').decode('utf8')

    # Send email
    msg = MIMEMultipart()
    msg['From'] = 'erdavis124@gmail.com'
    msg['To'] = 'edavis@tekion.com'
    msg['Subject'] = 'Contact Information'

    msg.attach(MIMEText(xml_string, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ericsalesconcierge@gmail.com', 'ericsalesconcierge12345')
    server.send_message(msg)
    server.quit()

    return redirect('/')
    

if __name__ == '__main__':
    app.run(port=8080, debug=True)