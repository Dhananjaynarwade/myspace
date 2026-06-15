# MySpace — Personal Links & Notes PWA

A clean personal PWA built with Django to save important links and notes (with screenshots).

---

## 🚀 Setup (Run Locally)

### 1. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Generate placeholder PWA icons (one-time)
```bash
python manage.py shell -c "
from PIL import Image, ImageDraw
for size in [192, 512]:
    img = Image.new('RGB', (size, size), color='#6366f1')
    d = ImageDraw.Draw(img)
    img.save(f'static/icons/icon-{size}.png')
"
```

### 5. Start the server
```bash
python manage.py runserver
```

Open → http://127.0.0.1:8000

---

## 📱 Install as PWA

- **Chrome (Desktop):** Click the install icon in the address bar
- **Android:** Tap "Add to Home Screen" from Chrome menu
- **iPhone/iPad:** Open in Safari → Share → "Add to Home Screen"

---

## 📁 Project Structure

```
myspace/
├── manage.py
├── requirements.txt
├── myspace/           # Project config (settings, urls)
├── links/             # Links app (model, views, urls)
├── notes/             # Notes app (model, views, urls)
├── templates/         # HTML templates
│   ├── base.html
│   ├── links/
│   └── notes/
├── static/
│   ├── manifest.json  # PWA manifest
│   ├── sw.js          # Service worker
│   └── icons/         # PWA icons
└── media/             # Uploaded screenshots
```

---

## 🌐 Deploy to Render (Free)

1. Push project to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn myspace.wsgi`
5. Add env variable: `DJANGO_SETTINGS_MODULE=myspace.settings`
6. Deploy!

> For production: set `DEBUG=False` and use a real `SECRET_KEY` via environment variable.
