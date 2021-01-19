# AlertaDengueCaptura
Routines for data capture.<br>
This repo contains the code for automatic capture of climatic data by the Crawlclima app schedule by crontab.

## Deploying Crawlclima with Docker

#### Requirements

Download the Data project to run the apps as the data from the demo databes.
See: https://github.com/AlertaDengue/Data

#### Update and install essentials
```bash
$ sudo apt update && sudo apt -y upgrade \
  build-essential git make wget
```
####  Get Docker
*https://docs.docker.com/engine/install/ubuntu/*
### Install Docker Compose: 
*https://docs.docker.com/compose/install/*

#### Build and run containers
> Use make from the repository root::<br>
> AlertaDengueCaptura$ make -f docker/crawlclima/Makefile
```bash
$ make -f docker/crawlclima/Makefile install_alertadenguecaptura
$ make -f docker/crawlclima/Makefile configure_ci_downloader_app
$ make -f docker/crawlclima/Makefile build_crawlclima
$ make -f docker/crawlclima/Makefile deploy_crawlclima
```

### Others Make commands

###### build services to images docker
```bash
$ make -f docker/crawlclima/Makefile build_crawlclima
```
###### Run containers and start app
```bash
$ make -f docker/crawlclima/Makefile deploy_crawlclima
```
###### Entry into container for crawlclima app
```bash
$ make -f docker/crawlclima/Makefile exec_crawlclima
```
###### Stop an remove containers
```bash
$ make -f docker/crawlclima/Makefile stop_crawlclima
```
###### Restart containers
```bash
$ make -f docker/crawlclima/Makefile restart_crawlclima
```
###### Configure project and install requirements dev
```bash
$ make -f docker/crawlclima/Makefileinstall_alertadenguecaptura
```

###### Clean containers
```bash
$ make -f docker/crawlclima/Makefile clean
```
###### Run tests into container

```bash
make -f docker/satellite/Makefile flake8_downloader_app:
make -f docker/satellite/Makefile test_downloader_app:
```
