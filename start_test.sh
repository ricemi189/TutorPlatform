
echo "docker-compose down"
/usr/local/bin/docker-compose -f docker-compose-test.yml down

echo "docker-compose up"
/usr/local/bin/docker-compose -f docker-compose-test.yml up -d