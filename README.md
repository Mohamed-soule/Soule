# Personal Portfolio Website

A professional personal portfolio website built with Flask and Python.

## Features
- Home page with hero section
- About page with skills and experience
- Projects showcase
- Contact page
- Responsive design
- Modern styling with CSS

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

The website will be available at `http://localhost:5000`

## Customization

### Edit Personal Information
1. **navbar** - Change "YourName" in `templates/base.html`
2. **About section** - Update `templates/about.html` with your bio, skills, and experience
3. **Projects** - Modify the projects list in `app.py` route
4. **Contact info** - Update email, phone, and social links in `templates/contact.html`
5. **Colors** - Customize colors in `static/style.css` (see `:root` section)

### Add New Projects
Edit the `projects_list` in the `/projects` route in `app.py`:
```python
projects_list = [
    {
        'title': 'Your Project',
        'description': 'Project description',
        'technologies': ['Tech1', 'Tech2'],
        'link': 'https://your-project-link.com'
    },
    ...
]
```

## File Structure
```
Med/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css         # CSS styling
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── projects.html     # Projects page
│   └── contact.html      # Contact page
└── README.md            # This file
```

## Features to Add Later
- Contact form backend functionality
- Blog section
- Download resume button
- Portfolio image gallery
- Dark mode toggle
