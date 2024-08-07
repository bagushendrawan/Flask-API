Setup Project

## Railway deployment

```shell
[commands here](https://flask-api-production-6584.up.railway.app/)
```

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

1. Install Python : https://www.python.org/downloads/
2. Ensure you have pip installed (it should comes with python packages)
3. Create python virtual environment

```shell
pip install virtualenv
python<version> -m venv <virtual-environment-name>

//example
mkdir projectA
cd projectA
python3.8 -m venv env
```

4. Run virtual environment
   
```shell
//Mac
source env/bin/activate

//Windows
 env/Scripts/activate.bat //In CMD
 env/Scripts/Activate.ps1 //In Powershel
```
6. Install required dependency
```shell
pip install -r requirements.txt
```

Here you should say what actually happens when you execute the code above.
