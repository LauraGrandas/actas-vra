brew install pyenv

pyenv init

pyenv install 3.8.12
pyenv local 3.8.12

pip install virtualenv
virtualenv ./.venv
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs 
.venv/bin/pip install -Ir requirements.txt

streamlit run myapp.py
