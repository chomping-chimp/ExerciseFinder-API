# Commands to run container locally
docker build -t app-container .
docker run -p 5000:5000 app-container