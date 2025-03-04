from flask import Flask, request
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    filter_type = request.form['filter']
    s3.upload_fileobj(file, 'winempresas-bucket', f"images/{file.filename}")
    return {'message': f'Imagen subida con filtro {filter_type}'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
