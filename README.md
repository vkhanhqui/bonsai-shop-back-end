# Bonsai shop back end :four_leaf_clover:

## Run project
### 1 Using Docker
```
docker-compose up
```

### 2 On your machine
- Install mysql
```
docker pull mysql
docker run -p 3306:3306 --name bonsai-db -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
- Run back end app
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
- Open Browser
```
localhost:8000/bonsai-backend/docs
```