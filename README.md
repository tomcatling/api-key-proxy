##

## Setup

### Run

```bash
docker-compose up --build
```

### Apply Migrations

```bash
docker exec -it api-key-proxy-web python manage.py makemigrations
docker exec -it api-key-proxy-web python manage.py migrate
```


### Create a User
```bash
docker exec -it api-key-proxy-web python manage.py createsuperuser
```

### Get Certificate

```bash
curl -x localhost:8080 http://mitm.it/cert/pem -o mitm-cert.pem
```

### Install Certificate

```bash
sudo apt-get install -y ca-certificates
sudo cp mitm-cert.pem /usr/local/share/ca-certificates/mitm-cert.crt
sudo update-ca-certificates
```

### Check

```bash
curl -x localhost:8080 https://api.openai.com/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: not-a-valid-key"   -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
        "role": "user",
        "content": "Compose a poem that explains the concept of recursion in programming."
      }
    ]
  }'
```