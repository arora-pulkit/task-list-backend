# Steps to kick start the backend

To build the image for docker, run the below command in the root folder of this project (where Dockerfile is present) -
```
docker build -t task-list-backend .
```
This will create an image named task-list-backend. You can verify this by running the `docker image ls` command.

Start the containerized process -
```
docker run --name tl-backend -it -p 5001:5000 task-list-backend
```

You can then access the resouces via localhost:5001
