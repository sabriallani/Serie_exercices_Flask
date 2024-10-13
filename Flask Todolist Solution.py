from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Faire les courses", "description": "Acheter du lait, des oeufs, du pain", "done": False},
    {"id": 2, "title": "Apprendre Flask", "description": "Créer une API REST avec Flask", "done": False}
]

# GET /tasks - Obtenir la liste des tâches
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# GET /tasks/<id> - Obtenir une tâche par ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tâche non trouvée"}), 404
    return jsonify(task)

# POST /tasks - Ajouter une nouvelle tâche
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not "title" in request.json:
        return jsonify({"error": "Titre manquant"}), 400
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT /tasks/<id> - Mettre à jour une tâche
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tâche non trouvée"}), 404
    if not request.json:
        return jsonify({"error": "Requête invalide"}), 400
    task["title"] = request.json.get("title", task["title"])
    task["description"] = request.json.get("description", task["description"])
    task["done"] = request.json.get("done", task["done"])
    return jsonify(task)

# DELETE /tasks/<id> - Supprimer une tâche
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tâche non trouvée"}), 404
    tasks.remove(task)
    return jsonify({"result": "Tâche supprimée avec succès"})

if __name__ == '__main__':
    app.run(debug=True)
