## FastAPI Project for Login/Signup 

### Initial Setup

### Install pipenv

#### Windows
```bash
$ pip install pipenv 
```

#### Linux
```bash
#fedora
$ dnf install pipenv

# debian
$ apt install pipenv
```

### Install packages
```bash
$ pipenv shell

$ pip install -r requirements.txt

```

### install uvicorn if getting any errors
```bash
$ pip install uvicorn
```

### Start the project
```bash
# normal command
uvicorn main:app --host 0.0.0.0 --port 8080 --reload

# run from script 
./start.sh
```