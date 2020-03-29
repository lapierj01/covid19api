# Pre-Requisites

# Install Python 3
sudo apt install python3
sudo apt install python3-venv

# Install PiP
sudo apt install python-pip

# Install Setup Tool
pip install --upgrade setuptools

# Install Pandas 
pip install pandas

# Install SQLAlchemy
pip install SQLAlchemy
pip install -U Flask-SQLAlchemy

# Install Python ODBC with ODBC header files pre-requisite
sudo apt-get install unixodbc-dev
sudo apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc 
pip install pyodbc


# Issues with Firewall
# check if accessible with ufw disable. If yes

ufw allow 5000/tcp
ufw enable