@echo off
echo Starting Edu Carnival Backend...
call venv\Scripts\activate
python manage.py runserver
pause
