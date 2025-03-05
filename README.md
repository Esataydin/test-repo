
# Test Repo 

## Steps


While in Project Directory, split terminal into 2 terminals



## Terminal 1 (Python):

To download libraries and activate virtual environment

```bash
  python -m venv env
```
```bash
  .\env\Scripts\activate
```
```bash
  pip install -r .\backend\requirements.txt
```
```bash
  cd .\backend\
```
```bash
  python .\manage.py runserver
```

## Terminal 2 (JavaScript):

```bash
  cd .\frontend\
```
```bash
  npm install
```
```bash
  npm run dev
```


You can check api endpoints with the link down below. (Don't forget to check "Base URL: 127.0.0.1:8000/api")

http://127.0.0.1:8000/swagger
#### frontend folder is for test, you need to change JS folder to handle the requests to Django backend