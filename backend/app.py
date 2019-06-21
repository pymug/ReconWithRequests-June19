import os
from flask import (
    Flask, redirect, url_for, render_template, request, session, 
    flash, make_response, jsonify
    )
from werkzeug import secure_filename
from flask_basicauth import BasicAuth

app = Flask(__name__, static_url_path='')

app.config['BASIC_AUTH_USERNAME'] = 'arj'
app.config['BASIC_AUTH_PASSWORD'] = '1234'

basic_auth = BasicAuth(app)

@app.route('/secret', methods=['GET', 'POST'])
@basic_auth.required
def secret_view():
    return render_template('secret.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_cookie')
def set_cookie():
    res = make_response('setting cookie...') # make_response(render_template('cookie'))
    res.set_cookie('logged_in', 'x')
    return res

@app.route('/greet')
def greet():
    return 'hi user'

@app.route('/greet_by_name', methods=['GET'])
def greet_by_name():
    name = request.args['name'] #.get()
    return 'hi user {}'.format(name)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verify_cookie_login', methods=['POST'])
def verify_cookie_login():
    if request.form['name'] == 'arj' and request.form['password'] == '1234':
        res = make_response(redirect('/protected_by_cookie'))
        res.set_cookie('logged_in', 'x')
        return res
    else:
        return redirect('/')


@app.route('/verify_login', methods=['POST'])
def verify_login():
    if request.form['name'] == 'arj' and request.form['password'] == '1234':
        return "great! you're in"
    else:
        return 'bad credentials'

@app.route('/protected')
def protected():
    if session['logged_in']:
        return render_template('protected.html')
    else:
        return redirect('/')

@app.route('/protected_by_cookie', methods=['GET'])
def cookie_protected():
    status = request.cookies.get('logged_in')
    if status == 'x':
        return render_template('protected_cookie.html')
    else:
        return redirect('/')

@app.route('/destroy_all_cookies')
def destroy_all_cookies():
    res = make_response('deleting...')
    res.delete_cookie('logged_in')
    res.delete_cookie('x')
    return res

@app.route('/info')
def req_info():
    info = {
        'ip':request.remote_addr,
        'date':request.date,
        'path':request.full_path,
        'host':request.host,
        'host url':request.host_url,
        'scheme':request.scheme
    }
    return jsonify(info)

@app.route('/all_info')
def all_req_info():
    i = []
    for _ in dir(request):
        a = getattr(request, _)
        i.append(['flask.request.'+_, str(a)])
    info = {
        'all':i
    }
    return jsonify(info)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
    
@app.route('/upload_service', methods = ['GET', 'POST'])
def upload_service():
   if request.method == 'POST':
      f = request.files['file']
      f.save('uploads/'+secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0')