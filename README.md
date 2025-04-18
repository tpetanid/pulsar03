# Pulsar

A Django-based web application built with Django 5.2 and styled with Tailwind CSS 4.1.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Install Node.js dependencies:
   ```
   npm install tailwindcss @tailwindcss/cli
   ```
5. Build the CSS:
   ```
   npm run build:css
   ```
6. Run migrations:
   ```
   python manage.py migrate
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
8. For development, you can watch for CSS changes:
   ```
   npm run watch:css
   ```

## Project Structure

- `pulsar/`: Main Django project configuration
- `main/`: Django application
- `static/css/`: CSS files including Tailwind input/output

## Frontend

This project uses Tailwind CSS for styling. The main CSS file is located at `static/css/input.css` and is compiled to `static/css/output.css` using the Tailwind CLI.

## Requirements

- Python 3.x
- Django 5.2
- Node.js 10+
- Tailwind CSS 4.1 