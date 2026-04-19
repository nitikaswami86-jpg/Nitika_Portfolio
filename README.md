# 🌟 Nitika Swami - Full Stack Portfolio

A complete Full Stack Portfolio Website built with **Python Django** (Backend) + **HTML, CSS, Bootstrap, JavaScript** (Frontend).

---

## 👩‍💻 Developer Info
- **Name:** Nitika Swami
- **Email:** nitikaswami86@gmail.com
- **Phone:** +91 8699200185
- **Location:** Chandigarh, Mohali
- **GitHub:** https://github.com/nitikaswami

---

## 🛠️ Tech Stack Used

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Python 3.x, Django 4.2  |
| Frontend    | HTML5, CSS3, Bootstrap 5|
| JavaScript  | Vanilla JS (ES6+)       |
| Database    | SQLite3                 |
| Version Ctrl| Git & GitHub            |
| Editor      | VS Code                 |

---

## 🚀 Features

- ✅ **Responsive Design** - Works on all screen sizes
- ✅ **Hero Section** - Animated typing effect, floating tech badges
- ✅ **About Section** - Personal info card with all contact details
- ✅ **Skills Section** - Animated progress bars for all skills
- ✅ **Projects Section** - Filter by category (Frontend / Python / Full Stack)
- ✅ **Contact Form** - Django backend saves messages to database (AJAX)
- ✅ **Admin Panel** - View all contact messages at `/admin/`
- ✅ **Smooth Animations** - Scroll-triggered animations throughout
- ✅ **Dark Theme** - Professional dark purple theme

---

## 📦 Project Structure

```
nitika_portfolio/
│
├── manage.py                    # Django entry point
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # Database (auto-created)
│
├── nitika_portfolio/            # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolio_app/               # Main Django app
│   ├── models.py                # Contact, Project, Skill models
│   ├── views.py                 # Page views + contact form handler
│   ├── forms.py                 # ContactForm with validation
│   ├── urls.py                  # URL routing
│   └── admin.py                 # Admin panel config
│
├── templates/
│   └── index.html               # Main portfolio template
│
└── static/
    ├── css/
    │   └── style.css            # Full custom CSS
    └── js/
        └── main.js              # JavaScript (typing, animations, AJAX)
```

---

## ⚙️ Setup & Run Instructions

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
```bash
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```
> Enter username, email, and password when prompted.

### Step 6: Run Development Server
```bash
python manage.py runserver
```

### Step 7: Open in Browser
```
Portfolio: http://127.0.0.1:8000/
Admin:     http://127.0.0.1:8000/admin/
```

---

## 🎯 Key Django Concepts Used

| Concept              | Where Used                         |
|----------------------|------------------------------------|
| Models               | Contact, Project, Skill models     |
| Views (FBV)          | home(), contact_submit()           |
| URLs                 | URL routing for pages & API        |
| Templates            | index.html with template tags      |
| Forms                | ContactForm with validation        |
| Admin                | Registered all models in admin     |
| CSRF Protection      | Contact form uses {% csrf_token %} |
| Static Files         | CSS, JS served via Django static   |
| ORM                  | form.save() saves to SQLite        |
| JSON Response        | AJAX contact form response         |

---

## 📝 Interview Q&A Prep

**Q: Why did you use Django for this project?**
> Django is a batteries-included Python web framework. It handles routing, ORM, admin, forms, and security (CSRF) out of the box, making it perfect for full-stack development.

**Q: How does the contact form work?**
> The form submits via JavaScript AJAX (fetch API) to a Django view. The view validates using Django's ModelForm, saves to SQLite via ORM, and returns a JSON response. No page reload needed.

**Q: How is static file serving handled?**
> In development, Django serves static files from the /static/ directory configured in settings.py via STATICFILES_DIRS.

**Q: What is CSRF and how is it handled?**
> CSRF (Cross-Site Request Forgery) protection is built into Django. I use {% csrf_token %} in the form and Django middleware validates it on every POST request.

---

## 👩‍🎓 About the Developer

Nitika Swami is a Full Stack Developer and BA Graduate from Chandigarh, Mohali. She is passionate about building clean, functional web applications using Python Django and modern frontend technologies.

---

*Built with ❤️ using Python Django + Bootstrap*
