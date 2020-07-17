sudo docker run -d \
  --name postgres_dev_2 \
  -e POSTGRES_USER=dev \
  -e POSTGRES_PASSWORD=dev \
  -e POSTGRES_DB=maadb_project \
  -e POSTGRES_INITDB_ARGS="--encoding=UTF8" \
  --publish 5432:5432 \
  postgres:latest
