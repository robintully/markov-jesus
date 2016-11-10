
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


import markovify
app = Flask(__name__)
Bootstrap(app)

# Get raw text as string and # Build the model.
with open("whole_bible.txt") as f:
    text = f.read()
text_model = markovify.Text(text)

with open("jesus.txt") as j:
    jesus_image = j.read()


# print(text_model.make_short_sentence(140))
@app.route('/')
def hello_world():
    message = text_model.make_short_sentence(300)
    return render_template('jesus.html', message=message)

if __name__ == "__main__":
    app.run()
