import os
import shutil

if "{{cookiecutter.celery}}".lower() in ('false', ''):
    os.remove('../{{cookiecutter.repo_name}}/example_project/config/celery.py')
    os.remove('../{{cookiecutter.repo_name}}/{{cookiecutter.app_name}}/tasks.py')

if "{{cookiecutter.templates}}".lower() in ('false', ''):
    shutil.rmtree('../{{cookiecutter.repo_name}}/{{cookiecutter.app_name}}/templates')

if "{{cookiecutter.static}}".lower() in ('false', ''):
    shutil.rmtree('../{{cookiecutter.repo_name}}/{{cookiecutter.app_name}}/static')
