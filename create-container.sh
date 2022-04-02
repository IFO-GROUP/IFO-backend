docker run \
  --detach \
  --env POSTGRES_HOST="$POSTGRES_HOST" \
  --env POSTGRES_USER="$POSTGRES_USER" \
  --env POSTGRES_DB="$POSTGRES_DB" \
  --env POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
  --volume=$MEDIA_HOST_PATH:/app/media \
  --network="main" \
  --name="ifo-backend" \
  container-registry:5000/${DRONE_REPO,,}:${DRONE_BUILD_NUMBER}
