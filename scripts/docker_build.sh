#!/usr/bin/env bash

echo "*** Performing environment clean-up... ***"
sh scripts/cleanup.sh


env="dev"
extra_command=""

for arg in "$@"
do
    if [ "$arg" = "--production" ] || [ "$arg" = "-p" ]
    then
        env="prod"
    else
      extra_command="${extra_command} ${arg}"
    fi
done

if [ "$env" = "prod" ]
then
    echo "========= Running Production Compose file ============"
    docker-compose -f "docker-compose-$env.yml" $extra_command
else
    echo "========= Running Development Compose file ============"
    docker-compose -f "docker-compose.yml" -f "docker-compose-$env.yml" $extra_command
fi