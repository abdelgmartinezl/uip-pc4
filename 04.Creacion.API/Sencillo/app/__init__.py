from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [
    {
        'id': 1,
        'titulo': u'Comprar cerveza',
        'descripcion': u'Corona, Atlas',
        'terminado': True 
    },
    {
        'id': 2,
        'titulo': u'Hacer tareas',
        'descripcion': u'Que pereza Python',
        'terminado': False
    }
]

@app.route('/vagancia/api/v1.0/tareas', methods=['GET', 'POST'])
def get_tareas():
    if request.method == "GET":
        print(request.environ)
        return jsonify(tareas)
    else:
        if not request.json or not 'titulo' in request.json:
            return jsonify({'error': 'No hay datos'})
        tarea = {
            'id': tareas[-1]['id'] + 1,
            'titulo': request.json['titulo'],
            'descripcion': request.json.get('descripcion', ""),
            'terminado': False
        }
        tareas.append(tarea)
        return jsonify({'tarea': tarea}), 201

if __name__ == "__main__":
    app.run()