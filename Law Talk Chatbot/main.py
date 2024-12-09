from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

client = MongoClient('mongodb://localhost:27017/')  
db = client['lawtalk_db']
users_collection = db['users']
history_collection = db['history']

data = pd.read_csv('legal_data.csv')

data['combined'] = data['query'] + " " + data['response'] + " " + data['article_number'] + " " + data['usage']

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined'])

def get_response(query):
    query_tfidf = tfidf_vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_tfidf, tfidf_matrix)
    best_match_idx = similarity_scores.argmax()
    return data.iloc[best_match_idx]

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_collection.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        if users_collection.find_one({'username': username}):
            error = 'Username already exists!'
        else:
            users_collection.insert_one({'username': username, 'password': hashed_password})
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))

    return render_template('register.html', error=error)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('home'))

    history = []
    if request.method == 'POST':
        user_query = request.form['query']

        history_collection.insert_one({'username': session['username'], 'entry': user_query})

        result = get_response(user_query)

        history_records = history_collection.find({'username': session['username']})
        history = [record['entry'] for record in history_records]

        return render_template('index.html', query=user_query, history=history, response=result['response'], article_number=result['article_number'], usage=result['usage'])

    history_records = history_collection.find({'username': session['username']})
    history = [record['entry'] for record in history_records]

    return render_template('index.html', history=history)

@app.route('/clear_history')
def clear_history():
    if 'username' in session:
        history_collection.delete_many({'username': session['username']})
        flash('History cleared successfully!')
    return redirect(url_for('index'))

@app.route('/download_book', methods=['GET'])
def download_book():
    if 'username' not in session:
        return redirect(url_for('home'))

    lang = request.args.get('lang', 'english')  

    if lang == 'tamil':
        path = os.path.join(os.getcwd(), "static", "law_books", "சட்ட புத்தகம்.pdf") 
    else:
        path = os.path.join(os.getcwd(), "static", "law_books", "English Version Law Book.pdf") 

    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
