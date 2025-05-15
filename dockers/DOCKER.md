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
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
