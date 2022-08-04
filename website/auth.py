from flask import Blueprint, render_template, request, flash



# Creating a blueprint object.
auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/register', methods= ['GET', 'POST'])
def register():
    return render_template('register.html')

@auth.route('/submit', methods= ['POST'])
def submit():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')
        
        if fname == '' or lname == '' or email == '' or password == '' or password_confirmation == '':
            print('it works')
            # render_template('register.html', message='Please enter required fields')
            return render_template('register.html', status='danger', message="Enter required fields")
        
        if password != password_confirmation:
            return render_template('register.html', status='danger', message="Password doesn't match")
            
    
        return render_template('register.html', status='success', message="Works")
    
        
@auth.route('/logout')
def logout():
    return "<h1>logout works</h1>"