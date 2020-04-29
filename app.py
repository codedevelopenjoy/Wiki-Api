from flask import Flask,render_template,request
import Scrapper

app=Flask(__name__)

KEY = {'MVwyYghfeMXlJOAP2LuYmPYuV'}

@app.route('/',methods = ['GET'])
def home():
    city = request.args.get('c')
    if k in KEY:
        try:
            data = scrap(str(city))
            return render_template('index.html',resp=json.dumps(data))
        except Exception as e:
            output={'exception' : 'Error'}
            return render_template('index.html',resp=json.dumps(output))
    else:
        output={'response' : 'Invalid Author Key'}
        return render_template('index.html',resp=json.dumps(output))

if __name__ == "__main__":
    app.run(debug=True)
