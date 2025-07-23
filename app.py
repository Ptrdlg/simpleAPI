from flask import Flask, request, jsonify
#comment
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Witaj w moim API!"}

@app.route("/mojastrona")
def moja_strona():
    return "To jest moja strona!"

@app.route("/hello")
def hello():
    name = request.args.get("name")  
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route("/api/v1.0/predict")
def predict():
    arg1 = float(request.args.get("num1"))  
    arg2 = float(request.args.get("num2"))  
    response = 1 if arg1+arg2>5.8 else 0
    return jsonify({"prediction": response, "features": {"num1": arg1, "num2": arg2}})


if __name__ == "__main__":
    app.run()
