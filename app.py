from flask import Flask, request, jsonify
import os
import cohere

app = Flask(__name__)

cohere_client = cohere.Client(os.getenv('COHERE_API_KEY'))

@app.route('/generate-novel', methods=['POST'])
def generate_novel():
    data = request.get_json()
    keywords = data.get('keywords', '')
    genres = data.get('genres', [])
    
    prompt = f"Keywords: {keywords}\nGenres: {', '.join(genres)}\nGenerate a novel based on these keywords and genres:"
    
    response = cohere_client.generate(
        model='commandR',
        prompt=prompt,
        max_tokens=500
    )
    
    novel = response.generations[0].text.strip()
    
    return jsonify({'novel': novel})

if __name__ == '__main__':
    app.run(debug=True)
