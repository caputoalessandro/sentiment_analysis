docker run -d \
  --name postgres_dev \
  -e POSTGRES_USER=dev \
  -e POSTGRES_PASSWORD=dev \
  -e POSTGRES_DB=maadb_project \
  --publish 5432:5432 \
  postgres:latest

ps
#systemctl start docker
#docker start postgres_dev