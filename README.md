conda create -p env python=3.8
source activate ./env
added -e . to requirement.txt to install local packages in the env
pip install -r requirements.txt  this installs all the packages including local packages due to -e . written in it
add a new file .env and add the OPENAI_API_KEY="your key in it" It is not checked in and will be avaialble localy

if you need to reinstall entire project python setup.py install

Github provide online vscode environment for any repository just use following url https://github.dev/rkarnwal/mcqgen