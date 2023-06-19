from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou_page():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('thankyou.html', name = name, email = email, subject = subject, message = message)

@app.errorhandler(404)
def error_page(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)