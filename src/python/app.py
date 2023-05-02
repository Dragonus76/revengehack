from flask import Flask, request, jsonify
import search_tool
import decryption_algorithm

app = Flask(__name__)

@app.route('/search_target_articles', methods=['POST'])
def search_target_articles_route():
    target_names = request.json.get('target_names')
    search_engine_api_key = request.json.get('search_engine_api_key')
    articles = search_tool.search_target_articles(target_names, search_engine_api_key)
    return jsonify(articles)

@app.route('/decrypt_password', methods=['POST'])
def decrypt_password_route():
    target_data = request.json.get('target_data')
    target_data_bytes = bytes.fromhex(target_data)  # Convertir target_data en bytes
    min_length = request.json.get('min_length')
    max_length = request.json.get('max_length')
    random_key, decrypted_password = decryption_algorithm.enhanced_decrypt_password(target_data_bytes, min_length, max_length)
    return jsonify({"random_key": random_key, "decrypted_password": decrypted_password})
@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
