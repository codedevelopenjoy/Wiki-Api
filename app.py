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
        resp = ''
        options = list()
        try:
            resp = wikipedia.summary(str(q))
            return render_template('index.html',code='1',resp=resp)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            for x in options:
                resp += x + '<br>'
            return render_template('index.html',code='2',resp=resp)
        except wikipedia.exceptions.PageError as e:
            resp = 'Not Found'
            return render_template('index.html',code='3',resp=resp)
        except Exception as e:
            pass
            return render_template('index.html',code='4',resp='Error')
    else:
        return render_template('index.html',code='5',resp='INVALID KEY')

if __name__ == "__main__":
    app.run(debug=True)
