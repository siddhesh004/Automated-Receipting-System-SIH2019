from subprocess import Popen, PIPE

# Popen(["python", "manage.py", "runserver"], stdout=PIPE, stderr=PIPE).communicate()
Popen(["python", "manage.py", "process_tasks"], stdout=PIPE, stderr=PIPE).communicate()
