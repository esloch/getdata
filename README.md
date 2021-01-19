# AlertaDengueCaptura
Routines for data capture.<br>
This repo contains the code for automatic capture of climatic data by the Crawlclima app schedule by crontab.

## Deploying Crawlclima with Docker

#### Requirements

Download the Data project to run the apps as the data from the demo databes.<br>
See: https://github.com/AlertaDengue/Data

#### Update and install essentials
```bash
$ sudo apt update && sudo apt -y upgrade \
  build-essential git make wget vim
```
####  Get Docker
*https://docs.docker.com/engine/install/ubuntu/*
#### Install Docker Compose: 
*https://docs.docker.com/compose/install/*

#### Build and run containers
> Use make from the repository root:<br>
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile install_alertadenguecaptura
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile configure_ci_downloader_app
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile build_crawlclima
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile deploy_crawlclima
```
> The crontab schedule can be edited manually in the file:<br>
```bash
AlertaDengueCaptura$ vim docker/crawlclima/cron_tasks
```
> After modifying the crontab you will need to do a new build and deploy. <br>
> It is also possible to modify it using the "crontab -e" page inside the Crawlclima app container.<br>

### Others Make commands

###### build services to images docker
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile build_crawlclima
```
###### Run containers and start services
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile deploy_crawlclima
```
###### Entry into container for crawlclima
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile exec_crawlclima
```
###### Stop an remove containers
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile stop_crawlclima
```
###### Restart containers
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile restart_crawlclima
```
###### Configure project and install requirements dev
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefileinstall_alertadenguecaptura
```

###### Clean containers
```bash
AlertaDengueCaptura$ make -f docker/crawlclima/Makefile clean
```
###### Run tests into container

```bash
AlertaDengueCaptura$ make -f docker/satellite/Makefile flake8_downloader_app
AlertaDengueCaptura$ make -f docker/satellite/Makefile test_downloader_app
```
