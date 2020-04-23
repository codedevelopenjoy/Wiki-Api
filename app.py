from flask import Flask,render_template,request
import wikipedia

app=Flask(__name__)

KEY = {'MVwyYghfeMXlJOAP2LuYmPYuV'}

@app.route('/',methods = ['GET'])
def home():
    k = request.args.get('k')
    l = request.args.get('l')
    q = request.args.get('q')
    if k in KEY:
        wikipedia.set_lang(str(l))
        summary = wikipedia.summary(str(q))
        return render_template('index.html',resp=str(summary))
    else:
        return render_template('index.html',resp='INVALID KEY')

if __name__ == "__main__":
    app.run(debug=True)
