# aws-ai-agents

AI Agents using AWS ecosystem

## Running application locally

1. Create a docker image

```
  docker -t aws/streamlit:latest .
```

2. Start a new docker container in detached mode on local port 8510

```
  docker run -d -p 8510:8501 aws/streamlit
```

3. Access application using URL: http://localhost:8501

## Deploying application on AWS EC2 ubuntu instance

1. Login to AWS console
2. Create a new EC2 instance using ubuntu
3. Login to EC2 instance using ssh or EC2 connect and run following commands:

   - sudo apt-get update -y
   - sudo apt-get upgrade
   - curl -fsSL https://get.docker.com -o get-docker.sh
   - sudo sh get-docker.sh
   - sudo usermod -aG docker ubuntu
   - newgrp docker
   - git clone <This repository>
   - docker build -t aws/streamlit:latest .
   - docker images -a
   - docker run -d -p 8501:8501 entbappy/stapp
   - docker ps

4. Access the application using: http://< Public IP address of EC2 instance >:8501
