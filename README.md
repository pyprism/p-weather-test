# p-weather-test

#### Create config and put appropriate values
```
cp backend/config.json backend/config.local.json
```

#### Run locally
```
docker-compose up
```
#### Run test
```
docker-compose exec backend python manage.py test
```

After running docker compose frontend will be available at http://0.0.0.0:3000/
