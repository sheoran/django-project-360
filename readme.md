#### Django Project 360
A opinionated template which is conceptualized by reading many other opinionated Django Project template
proposals. Taking the best of those.
Some of the key features of this template are  
1. Developer first (minimal steps required to run/develop things)
    1. Use mac/linux/Windows as long you can run Docker
1. Docker-compose for services
1. `pipenv` to track project python dependencies. 
1. No namespace conflicts between django community and your projects.     

### Contribute code
 1. cd newly cloned repo
 1. Make sure docker and docker-compose is installed
    1. [Install docker-ce](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
    1. Enable tcp control for docker host
       * [Ubuntu 16](https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)    
 1. Make sure you `pipenv` is installed
 1. Execute `pipenv --python 3.5`
    1. Execute `pipenv shell`
    1. Execute `pipenv install -d`
 1. Get a dev env`bin/dev_box` (This might take some time if its first time on the system)
    * your username is your password if required
    * If for some reason you see errors with env_generator.py to unblock
        * copy `env_template.yaml` to `env_template_override.yaml`
        * Replace the content of each value manually yourself
 1. [Deploy local instance of yourDjangoProject](docs/dev.md#deploy-local-instance-of-yourDjangoProject)
    1. Access things on 0.0.0.0:8080
 1. Figure out 
    1. Replacement for `youNameSpace`
    1. Replacement for `yourDjangoProject`
 1. Replace all instances of these two.
 1. Create branch `git branch` and do what you are best at.

#### Future RoadMap Examples
 1. Replace sqlite db with postgres
 1. Add testing support
 1. Add celery support out of the box to template
 1. Add logging to local ELK Stack
 1. Add DRF support
 1. Add AppAdmins to templates
 1. Add DjangoDbBackup
 1. Add Production like deployment
 1. Add kubernetes support
 


### yourDjangoProject Doc Index
1. [Dev Notes](docs/dev.md)
