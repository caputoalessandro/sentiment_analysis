#sudo docker run -d \
#  --name postgres_dev \
#  -e POSTGRES_USER=dev \
#  -e POSTGRES_PASSWORD=dev \
#  -e POSTGRES_DB=  \
#  --publish 5432:5432 \
#  postgres:latest

systemctl start docker
sudo docker start postgres_dev