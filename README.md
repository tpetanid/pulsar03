# Pulsar

A Django-based web application built with Django 5.2.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

- `pulsar/`: Main Django project configuration
- `main/`: Django application

## Requirements

- Python 3.x
- Django 5.2 