with open('/tmp/cookiecutter.log', 'a+') as f:
    f.write("{{cookiecutter.celery}}\n")
print "{{cookiecutter.celery}}"
