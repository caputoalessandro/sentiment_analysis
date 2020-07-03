set -e
set -x


export MONGO_INITDB_ROOT_USERNAME="dev"
export MONGO_INITDB_ROOT_PASSWORD="dev"

sudo docker run \
  --name maadb-mongo \
  --publish 27017:27017 \
  -d \
  mongo
