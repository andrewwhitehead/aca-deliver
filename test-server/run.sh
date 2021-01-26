COMPOSE=`command -v docker-compose`

if [ -z "$COMPOSE" ]; then
    echo Docker compose is not installed
    exit 1
fi

$COMPOSE up -d
