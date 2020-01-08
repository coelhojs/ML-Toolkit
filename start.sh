conda env create -f environment.yml
conda activate vera
gunicorn --timeout 300 --workers=4 --bind 0.0.0.0:5000 wsgi:app