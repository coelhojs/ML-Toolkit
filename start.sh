conda env create -f environment.yml
conda activate vera
gunicorn --timeout 300 --workers=4 --bind 0.0.0.0:5000 wsgi:app

set FLASK_APP=app.py
waitress-serve --call 'app.py:create_app'


# TESTES:
# TF-CPU: Detecção 5 imagens: 29s
# TF-GPU: Detecção 5 imagens: 16s