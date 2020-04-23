from flask import Flask,render_template

app=Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    a1 = request.args.get('a')
    b1 = request.args.get('b')
    return render_template('index.html',a=str(a1),b=str(b1))

if __name__ == "__main__":
    app.run(debug=True)
