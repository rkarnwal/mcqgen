conda create -p env python=3.8
source activate ./env
added -e . to requirement.txt to install local packages in the env
pip install -r requirements.txt  this installs all the packages including local packages due to -e . written in it
add a new file .env and add the OPENAI_API_KEY="your key in it" It is not checked in and will be avaialble localy

if you need to reinstall entire project python setup.py install

Github provide online vscode environment for any repository just use following url https://github.dev/rkarnwal/mcqgen

Run the app streamlit run StreamlitApp.py 

AWS Commands
Launch Ubuntu instance with around 15 gb of data allow HTTP and HTTPS traffic
After launc from command prompt of EC2 update m/c using 
sudo apt update
sudo apt-get update
sudo apt upgrade -y
After updating VM install following 
sudo apt install git curl unzip tar make sudo vim wget -y

Now clone Git repository on this m/c
git clone https://github.com/rkarnwal/mcqgen

Now create .env file as it is not in git and add openAI key
in ubuntu pip doesn't work you need to use pip3 and install requirement.txt to set environmeny
pip3 install -r requirement.txt

run app in aws using python3 -m streamlit run StreamlitApp.py
