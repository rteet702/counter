from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secrets are no fun'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'counter' not in session:
        session['counter'] = 1

    if 'view_counter' in session:
        session['view_counter'] += 1
    else:
        session['view_counter'] = 1

    if 'inc_amount' in session:
        inc_amount = session['inc_amount']
    else:
        inc_amount = 0

    return render_template('index.html', counter=session['counter'], view_counter=session['view_counter'],inc_amount=inc_amount)

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/plus_one', methods=['POST'])
def plus_one():
    session['counter'] += 1
    return redirect('/')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['counter'] += 2
    return redirect('/')

@app.route('/plus_x', methods=['POST'])
def plus_x():
    session['inc_amount'] = int(request.form['increment_amount'])
    session['counter'] += session['inc_amount']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)