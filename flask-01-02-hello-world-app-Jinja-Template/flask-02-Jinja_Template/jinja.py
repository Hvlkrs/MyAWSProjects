from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template('index.html', number1 = 20, number2 = 40)

@app.route("/mult")
def number():
    var1, var2 = 30, 70
    return render_template('body.html', num1=var1, num2=var2, mul=var1*var2)


#It works on localhost/5000 as default
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
#It works on localhost/5000 as default
    #app.run(debug=True)