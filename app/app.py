from flask import Flask,render_template,request,redirect
import youtube_dl
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/download',methods=["POST","GET"])
def Download():
    url = request.form["url"]
    print("You are trying to dowmnload :",url)
    with youtube_dl.YoutubeDL() as ydl:
            url =  ydl.extract_info(url,download=False)
            download_link = (url["formats"][-1]["url"])
            return redirect(download_link+"&dl=1")
        
@app.route('/developer')
def developer():
    return render_template("developer.html")

@app.route('/Terms-conditions')
def Terms_conditions():
    return render_template("Terms-conditions.html")

if __name__ == '__main__' :
    app.run(debug=True)
