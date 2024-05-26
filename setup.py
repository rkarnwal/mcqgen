from setuptools import find_packages, setup

setup(
    name='mcqgenerator' ,
    version='0.0.1',
    author='rkarnwal',
    author_email='rajat_karnwal@yahoo.com',
    install_requires=['openai', 'langchain','langchain_community','streamlit', 'python-dotenv', 'PyPDF2' ],
    packages=find_packages()
)