import flask
from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateBook(FlaskForm):
    name = StringField("Название: ", validators=[DataRequired()])
    creator = StringField("Издатель: ", validators=[DataRequired()])
    submit = SubmitField("Создать")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'help me, i wanna sleep'


@app.route('/')
def wellcome_view():
    return flask.render_template('wellcome.html')


@app.route('/create/', methods=['GET', 'POST'])
def create_view():
    form = CreateBook()
    if flask.request.method == "GET":
        return flask.render_template('create.html', form=form)

    return '<body bgcolor="black">' \
           '<div style="color: yellow; font-size: 1.7rem; font-family: Trebuchet MS, Verdana, sans-serif">Книга: {}' \
           '</div>' \
           '<div style="color: white; font-size: 1.1rem;">' \
           '<br> Через пять лет его книга превзошла все ожидания, она стала популярнее чем видео' \
           ' >Я не умру в туалете<.<br> Более десяти миллионов людей раскупили ее за месяц и он стал' \
           ' первым миллиамногодером!<br> Скорей же, бросайте все ваши заботы, работу, учебу и скорей получать Кайф.' \
           '<br>Книги это КрУтО!' \
           '</div>'\
           '<div style="color: pink; font-style : oblique; transform: translate(22em, 1em); opacity: 0.6;"' \
           '>Издатель Книги: {}</div>' \
           '</body>'.format(form.name.data, form.creator.data)


if __name__ == '__main__':
    app.run(debug=True)
