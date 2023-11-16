import subprocess

if __name__ == "__main__":
    subprocess.call(["gunicorn", "-c", "gunicorn_config.py", "test_project.wsgi:application"])
