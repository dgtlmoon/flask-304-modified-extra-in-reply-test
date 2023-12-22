from flask import Flask, send_from_directory
from flask_compress import Compress as FlaskCompress

app = Flask(__name__)
FlaskCompress(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/static")
def static_content():
	from flask import make_response
	response = make_response(send_from_directory(directory=".", path="image.png"))
	return response

