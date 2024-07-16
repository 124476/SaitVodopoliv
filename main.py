import requests
from flask import Flask, render_template, redirect, make_response, request, send_file
from flask_restful import abort, Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route("/")
def index():
    return render_template("index.html", bg="img", isMain="isMain")


@app.route("/vopros_1")
def vopros_1():
    return render_template("vopros_1.html", bg="img")


@app.route("/vopros_2")
def vopros_2():
    return render_template("vopros_2.html", bg="img")


@app.route("/vopros_3")
def vopros_3():
    return render_template("vopros_3.html", bg="img")


@app.route("/vopros_4", methods=['GET', 'POST'])
def vopros_4():
    if request.method == 'GET':
        return render_template("vopros_4.html", bg="img")

    count = int(request.form.get('count'))

    if count == 1:
        count = 150
    elif 2 <= count <= 5:
        count = 150 + 70 * (count - 1)
    else:
        count = 150 + 70 * 5 + 50 * (count - 6)

    return render_template("otvet.html", bg="img", count=count)


if __name__ == '__main__':
    app.run()
