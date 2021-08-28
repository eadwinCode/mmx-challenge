# Momox Project


### Setup and Installation
_Note: make sure docker and docker-compose are installed_


## Development Server

### Step 1
Build the containers
```shell script
sh scripts/docker_build.sh build
```

### Step 2
Run the containers
```shell script
sh scripts/docker_build.sh up
```

or build and run with a single command
```shell script
sh scripts/docker_build.sh up --build
```

### Extras
To run unit tests
```shell script
docker exec momox_api_dev sh run_test.sh
```
Note: all docker-compose commands works after the script
Eg: `kill`, `stop`, `--no-cache` etc.
```shell script
sh scripts/docker_build.sh down
```
```shell script
sh scripts/docker_build.sh kill
```
```shell script
sh scripts/docker_build.sh build --no-cache
```
```shell script
sh scripts/docker_build.sh run -d
```

## Staging Server

### Step 2
Build the containers
```shell script
sh scripts/docker_build.sh -s --build
```

### Step 3
Run the containers
```shell script
sh scripts/docker_build.sh -s
```

### Step 4
Open your web browser and view the application using the following urls
```
API Docs:  localhost:8001/
```

Run unit test
```shell script
docker exec momox_api_dev sh run_test.sh
```