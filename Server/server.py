from flask import Flask, request
import sys
import webbrowser

import simple_doctor as sd
import level_generator as lg

WEB_DIRECTORY = "../WebApp/"

if 'darwin' == sys.platform:
    LEVEL_PATH = "../Client/ScienceBirds.app/Contents/Resources/Data/StreamingAssets/Levels/level-4.xml"
else:
    LEVEL_PATH = "../Client/ScienceBirds_Data/StreamingAssets/Levels/level-4.xml"


app = Flask(__name__, static_folder=WEB_DIRECTORY)

# Render Web app
@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# Receive the image and save it.
@app.route('/uploadSketch', methods=['POST'])
def receive():
    # predict
    predict = request.form['result'] or 'none'
    predict = sd.generate_sentences("things", predict)

    # sketch
    file = request.files['sketch']
    if file:
        file.save('temp.png')
        lg.generate(LEVEL_PATH)

    return predict

if __name__ == '__main__':
    app.run(debug=True, port=5000)