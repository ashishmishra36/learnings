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
