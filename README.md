
conda env create -f environment.yml
conda activate vera

set FLASK_APP=app.py
python -m flask run