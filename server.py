from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secrets are no fun'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)