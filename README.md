# AlertaDengueCaptura
Rotinas para captura de dados

This repo contains the code for automatic capture of climatic data by the Crawlclima app schedule by crontab.

## Deploying Crawlclima with Docker

## Requirements

Download the Data project to run the apps as the data from the demo databes.
See: https://github.com/AlertaDengue/Data

### Update and install essentials:
```bash
$ sudo apt update && sudo apt -y upgrade \
  build-essential git make wget
```
###  Get Docker:
*https://docs.docker.com/engine/install/ubuntu/*
### Install Docker Compose: 
*https://docs.docker.com/compose/install/*

## Build and run containers

```bash
$ make -f docker/crawlclima/Makefile install_alertadenguecaptura
$ make -f docker/crawlclima/Makefile configure_ci_downloader_app
$ make -f docker/crawlclima/Makefile build_crawlclima
$ make -f docker/crawlclima/Makefile deploy_crawlclima
```
