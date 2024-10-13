from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route pour afficher le formulaire HTML
@app.route('/')
def index():
    form_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Submit your name</title>
    </head>
    <body>
        <h1>Submit your name</h1>
        <form action="/greet" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(form_html)

# Route pour traiter le formulaire et afficher le message
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)

