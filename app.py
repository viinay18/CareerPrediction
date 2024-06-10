from flask import Flask, render_template, request, redirect, url_for, flash
from prediction import career_prediction

app = Flask(__name__)
app.secret_key = 'helloworld'

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/predict', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        try:
            user_input = [request.form['choice1'],request.form['choice2'],request.form['choice3']] 
            prediction = career_prediction(user_input)
            return render_template('prediction.html', prediction=prediction)
        except Exception as e:
            flash('Options cannot be empty. Please try again', category="danger")
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)