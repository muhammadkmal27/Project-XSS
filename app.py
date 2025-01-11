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
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    # Start the c_breakers script in a new thread
    threading.Thread(target=run_c_breakers).start()
    # Redirect immediately to the output page
    return redirect(url_for('output'))
    
    

# XSS page
@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        url = request.form.get('url')
        output, error = run_command(f"python c_breakers.py {url}")
        return render_template('output.html', output=output, error=error)
    return render_template('xss.html')

# Payload page
@app.route('/payload', methods=['GET', 'POST'])
def payload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(f"uploads/{file.filename}")
        output, error = run_command(f"python c_breakers.py {file.filename}")
        return render_template('output.html', output=output, error=error)
    return render_template('payload.html')

# Threads page
@app.route('/threads', methods=['GET', 'POST'])
def threads():
    if request.method == 'POST':
        num_threads = request.form.get('threads')
        output, error = run_command(f"python c_breakers.py {num_threads}")
        return render_template('output.html', output=output, error=error)
    return render_template('threads.html')

# Request page
@app.route('/request', methods=['GET', 'POST'])
def request_page():
    if request.method == 'POST':
        request_num = request.form.get('request')
        output, error = run_command(f"python c_breakers.py {request_num}")
        return render_template('output.html', output=output, error=error)
    return render_template('request.html')

# Output page
@app.route('/output')
def output():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)


