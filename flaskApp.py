from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'contact': '1234567890',
        'name': 'A', 
        'done': False,
        'id': 1
    },
    {
        'contact': '1134567890',
        'name': 'B', 
        'done': False,
        'id': 2
    },
]

@app.route("/add-data", methods=["POST"])



def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)

    contact = {
        'contact': request.json['contact'],
        'name': request.json.get('name',""), 
        'done': False,
        'id': contacts[-1]['id']+1,

    }

    contacts.append(contact)

    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

# @app.route("/get-data")

# def get_task():
#     return jsonify({
#         "data":contacts,
#     }) 


if (__name__ == "__main__"):
    app.run(debug=True)



