from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/services')
def services():
    return render_template('services.html', title="Services")

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

@app.route('/login')
def login():
    return render_template('login.html', tittle="Login")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

if __name__ == "__main__":
    app.run(debug=True)
