#FROM linuxserver/code-server:3.12.0
FROM whyour/ql:base
ARG QL_MAINTAINER="whyour"
LABEL maintainer="${QL_MAINTAINER}"
ARG QL_BRANCH=master

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    QL_DIR=/ql \
    QL_BRANCH=${QL_BRANCH}

WORKDIR ${QL_DIR}

COPY . .

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && touch ~/.bashrc \
    && cd ${QL_DIR} \
    && cp -f .env.example .env \
    && chmod 777 /ql/shell/*.sh \
    && chmod 777 /ql/docker/*.sh \
	&& chmod 777 /ql/*.sh \
    && npm install -g pnpm \
    && pnpm install -g pm2 \
    && pnpm install -g ts-node typescript tslib \
    && rm -rf /root/.npm \
    && pnpm install --prod \
    && rm -rf /root/.pnpm-store 

EXPOSE 22
EXPOSE 5700
EXPOSE 8080 
ENTRYPOINT ["./docker-entrypoint.sh"]
