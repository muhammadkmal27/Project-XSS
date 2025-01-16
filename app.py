from flask import Flask, render_template, request, redirect, url_for
import subprocess
import threading

app = Flask(__name__)

# Function to run c_breakers.py in a separate thread
def run_c_breakers():
    try:
        subprocess.run("python c_breakers.py", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running scan: {str(e)}")

@app.route('/')
def home():
    return render_template('login_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/url')
def url():
    return render_template('url.html')

@app.route('/threads')
def threads():
    return render_template('threads.html')

@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/payload')
def payload():
    return render_template('payload.html')

@app.route('/scanning')
def scanning():
    return render_template('scanning.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/scan', methods=['POST'])
def scan():
    # Start the c_breakers script in a new thread
    threading.Thread(target=run_c_breakers).start()
    # Redirect immediately to the output page
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)


