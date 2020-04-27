from flask import Flask,render_template,request
import wikipedia
import json

app=Flask(__name__)

KEY = {'MVwyYghfeMXlJOAP2LuYmPYuV'}

@app.route('/',methods = ['GET'])
def home():
    k = request.args.get('k')
    l = request.args.get('l')
    q = request.args.get('q')
    if k in KEY:
        try:
            output = {}
            wikipedia.set_lang(str(l))
            summary = wikipedia.summary(str(q))
            output["content"] = summary
            images = wikipedia.page(str(q)).images
            img = {}
            index = 1
            for image in images:
                if image[-3:] in ['jpg','peg','bmp','png']:
                    img["img"+str(index)] = image
                    index=index+1
                    if index == 7:
                        break
            output["images"] = img
            output["code"] = '1'
            o = json.dumps(output)
            return render_template('index.html',resp=o)
        except wikipedia.exceptions.DisambiguationError as e:
            output = {}
            temp1 = {}
            index = 1
            for option in e.options:
                temp1['o'+str(index)] = option
                index=index+1
                if index == 10:
                	break
            output['options'] = temp1
            output['code'] = '2'
            o = json.dumps(output)
            return render_template('index.html',resp=o)
        except wikipedia.exceptions.PageError as e:
            output={'code' : '3','response' : 'Not Found'}
            o = json.dumps(output)
            return render_template('index.html',resp=o)
        except Exception as e:
            output={'code' : '4','response' : 'Error : '+str(e)}
            o = json.dumps(output)
            return render_template('index.html',resp=o)
    else:
        output={'code' : '5','response' : 'Invalid Author Key'}
        o = json.dumps(output)
        return render_template('index.html',resp=o)

if __name__ == "__main__":
    app.run(debug=True)
