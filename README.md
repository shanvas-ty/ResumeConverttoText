Freego Project Guidelines

1. All code, artifacts has to be shared through this gitlab repository
2. Project Management Pages is at: https://docs.google.com/document/d/1tigLVSJRf9NT2OhasIGg55mearBJEItaiOpvAjHPIoU
3. Project Architecture and requirements highlevel: https://docs.google.com/document/d/1pJ9eJezgnSrh1GttboqZFFx1505hz8dECNKWKtjfW4Y

Frego is a AI engine with companion for a user for their assistance
<To be added - More details>

### To run mongodb on docker
#### Install docker by giving the command
    docker pull mongo

#### Setup the container to run the mongodb
    docker run -d --name mongodb -p 27017:27017 -v /Users/admin/workspace/mongodb:/data/db mongo

#### To start mongodb container 
    docker start mongodb

#### Connect to the container to work with mongodb (you may connect to that through port forwarding as well)
    docker exec -it mongodb bash

#### To use the client to connect to mongodb

    mongo


    

