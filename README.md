```sh
# setup python virtual env
python -m venv venv
source venv/bin/activate
deactivate
# start localhost
uvicorn main:app --reload
```