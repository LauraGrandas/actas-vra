pyenv init

pyenv install 3.8.12
pyenv local 3.8.12

pip install virtualenv
virtualenv ./.venv

venv/bin/pip install -Ir requirements.txt

streamlit run myapp.py
