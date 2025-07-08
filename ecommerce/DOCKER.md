## Phase    | What Happens
Write       | Define instructions in a Dockerfile
Build       | Convert to image using docker build
Store       | Save locally or push to a registry
Run         | Create containers from the image
Update      | Modify Dockerfile and rebuild
Clean Up    | Remove unused containers/images/layers


Dockerfile ➜ docker build ➜ Docker Image ➜ docker run ➜ Container Running Your Python App
           ↘ update & rebuild ↘
           🔁 iteration cycle

## command to delete all docker images 
docker system prune 

## jenkins 
1. docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v ~/.ssh:/var/jenkins_home/.ssh \
  jenkins/jenkins:lts

## to run jenkins with access to docker -
docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  -p 8080:8080 -p 50000:50000 \
  --name jenkins \
  jenkins/jenkins:lts

docker exec -it -u 0 1a1c7beb97ec /bin/bash
apt update && apt install -y docker.io
usermod -aG docker jenkins
chown root:docker /var/run/docker.sock
chmod 664 /var/run/docker.sock

exit 
docker restart jenkins

## to run selenium grid with chrome 
docker pull seleniarm/standalone-chromium
docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest




docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

2. to go into the docker container docker exec -it -u 0 1a1c7beb97ec /bin/bash
3. to get the updates inside the docker: apt-get update
4. to install python inside the docker: apt-get install python3
5. to install pip: apt-get install python3-pip
6. to install venv: apt install python3.11-venv


# ngrok - 563AUQCEAU73ZE5323C3TIQYL2QCJ7EB
# these are ngrok codes
AVNH7KTZSC
A9RGBGV32J
FAY766SJ46
XZ8Z8FG474
CBG94MJKGH
JV8PPWZ4FK
2TDQSXGJFF
WTTJRJDKX3
HNRSR68ZNT
76KYUP67J6



