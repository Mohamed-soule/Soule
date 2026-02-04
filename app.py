from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Project 1',
            'description': 'A brief description of your first project',
            'technologies': ['Python', 'Flask'],
            'link': '#'
        },
        {
            'title': 'Project 2',
            'description': 'A brief description of your second project',
            'technologies': ['JavaScript', 'React'],
            'link': '#'
        },
        {
            'title': 'Project 3',
            'description': 'A brief description of your third project',
            'technologies': ['Python', 'Django'],
            'link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
