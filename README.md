# AlertaDengueCaptura
Routines for data capture.<br>
This repo contains the code for automatic capture of climatic data by the Crawlclima app schedule by crontab.

## Deploying Crawlclima with Docker

#### Requirements

Download the Data project to run the apps as the data from the demo databes.<br>
See: https://github.com/AlertaDengue/Data

#### Configure environment
Copy the example_env file by renaming it to .env into the docker / crawlclima directory:
```bash
cp example_env_file /docker/crawclima/.env
```
Modify the variables of file system and database connection according to needs

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
|------------------------------------------------------------------|
| <h6><b> build services to images docker </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile build_crawlclima ``` |
| <h6><b> Run containers and start services </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile deploy_crawlclima ``` |
| <h6><b> Entry into container for crawlclima </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile exec_crawlclima ``` |
| <h6><b>  Stop an remove containers </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile stop_crawlclima ``` |
| <h6><b> Restart containers </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile restart_crawlclima ``` |
| <h6><b> Configure project and install requirements dev </b></h6> |
| ``` $ make -f docker/crawlclima/Makefileinstall_alertadenguecaptura ``` |
| <h6><b> Clean containers </b></h6> |
| ``` $ make -f docker/crawlclima/Makefile clean ``` |
| <h6><b> Run tests into container </b></h6> |
| ``` $ make -f docker/satellite/Makefile flake8_downloader_app ``` |
| ``` $ make -f docker/satellite/Makefile test_downloader_app ``` |
