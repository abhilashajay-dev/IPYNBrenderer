echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.10"
python -m venv env 
echo [$(date)]: "Activating  env"
source env/Scripts/activate
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"