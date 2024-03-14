import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def ask_for_number():
    return '<h1>Choose a number between 0 and 9.</h1><br>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route("/<int:number>")
def check(number):
    if random_number == number:
        return '<h1 style="color: green">You guessed it right!</h1><br>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif random_number < number:
        return f'<h1 style="color: purple">{number} is too high!</h1><br>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return f'<h1 style="color: red">{number} is too low!</h1><br>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
