from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
        1: "Hello World"
    }

users = {
        1: {
            "name": "Alex",
            "age": 25
        },
        
        2: {
            "name": "Max",
            "age": 28
        },

        3: {
            "name": "Egor",
            "age": 15
        }
    }

@app.route('/hello_world', methods=['GET'])
def say_hello():
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def user_info():
    try:
        id = int(request.args.get("id"))
        return jsonify(users[id])
    except:
        return "srry"

@app.route('/auth', methods=['POST'])
def auth():
    login = request.form.get('login')
    pswd = request.form.get('password')

    if login == "admin" and pswd == "admin":
        return "correct"
    else:
        return "incorrect"

if __name__ == "__main__":
    app.run(debug=True)