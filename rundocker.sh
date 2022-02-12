docker run -dit \
  -v /disk2T/docker/qinglongvscode/prd_file/ql/config:/ql/config \
  -v /disk2T/docker/qinglongvscode/prd_file/ql/log:/ql/log \
  -v /disk2T/docker/qinglongvscode/prd_file/ql/db:/ql/db \
  -v $PWD/ql/repo:/ql/repo \
  -v /disk2T/docker/qinglongvscode/prd_file/ql/raw:/ql/raw \
  -v /disk2T/docker/qinglongvscode/prd_file/ql/scripts:/ql/scripts \
  -p 5700:5700 \
  -p 5722:22 \
  --name qinglong \
  --hostname qinglong \
  --restart unless-stopped \
  qinglongvscode
