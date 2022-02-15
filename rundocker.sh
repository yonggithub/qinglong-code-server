docker run -dit \
  -v /disk2T/docker/qinglongvscode/:/ql \
  -v $PWD/ql/repo:/ql/repo \
  -p 5700:5700 \
  -p 5722:22 \
  -p 8443:8443 \
  --name qinglong \
  --hostname qinglong \
  --restart unless-stopped \
  qinglongvscode:latest
