from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/disease-prediction')
def disease_prediction():
    return redirect("http://localhost:5001")  # URL for the disease prediction app


@app.route('/chatbot')
def chatbot():
    return redirect("http://localhost:5002")  # URL for the chatbot app


@app.route('/video-chat')
def video_chat():
    return redirect("http://localhost/Video-consultation/index.php")  # URL for the chatbot app

if __name__ == '__main__':
    app.run(port=5000, debug=True)



