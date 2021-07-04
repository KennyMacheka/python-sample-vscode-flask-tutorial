import requests
from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route('/messages', methods=['GET', 'POST'])
def ms_teams():
    send_post_request()
    return {"type" : "message", "text" : "Hello there, Mr Kenobi"}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


def send_post_request():
    null = None
    data = {"type" : "message",
            "attachments": [ {
                 "contentType":"application/vnd.microsoft.card.adaptive",
         "contentUrl":null,
         "content":{
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard",
            "version":"1.2",
            "body":[
                {
                "type": "TextBlock",
                "text": "For Samples and Templates, see [https://adaptivecards.io/samples](https://adaptivecards.io/samples)"
                }
            ]
         }
    }] }

    requests.post("https://kennymacheka.webhook.office.com/webhookb2/4aefee57-dba7-4cd6-9c14-4a2ca2755c6d@8103d5db-e42e-4c9c-af0b-4cee9bd0879e/IncomingWebhook/a869f391d77643c1b2284189b19972d0/b63c907a-d913-484a-823a-5a7e8dbb43f3",
                  data = data)