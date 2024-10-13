from flask import Flask, request, render_template_string

app = Flask(__name__)

# Template for the calculator page
html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Calculatrice Flask</title>
  </head>
  <body>
    <h1>Calculatrice Simple</h1>
    <form method="post" action="/">
      <input type="text" name="num1" placeholder="Nombre 1" required>
      <select name="operation">
        <option value="add">+</option>
        <option value="subtract">-</option>
        <option value="multiply">*</option>
        <option value="divide">/</option>
      </select>
      <input type="text" name="num2" placeholder="Nombre 2" required>
      <button type="submit">Calculer</button>
    </form>
    {% if result is not none %}
      <h2>Résultat: {{ result }}</h2>
    {% endif %}
  </body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Erreur: Division par zéro'
        except ValueError:
            result = 'Erreur: Entrée invalide'

    return render_template_string(html_template, result=result)


if __name__ == '__main__':
    app.run(debug=True)
