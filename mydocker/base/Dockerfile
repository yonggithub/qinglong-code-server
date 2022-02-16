FROM martinussuherman/alpine-code-server:latest
ARG QL_MAINTAINER="whyour"
LABEL maintainer="${QL_MAINTAINER}"

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=zh_CN.UTF-8 \
    SHELL=/bin/bash \
    PS1="\u@\h:\w \$ " \
    PASSWORD="111111"

#COPY package.json /

RUN set -x \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update -f \
    && apk upgrade \
    && apk --no-cache add -f bash \
                             coreutils \
                             moreutils \
                             git \
                             curl \
                             wget \
                             tzdata \
                             perl \
                             openssl \
                             nginx \
                             python3 \
                             jq \
                             openssh \
                             py3-pip \
                             python2 \
                             g++ \
                             make \
			     libc6-compat \
			     jq \
			     npm \
    && rm -rf /var/cache/apk/* \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && touch ~/.bashrc \
    && sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  \
    && ssh-keygen -t dsa -P "" -f /etc/ssh/ssh_host_dsa_key  \
    && ssh-keygen -t rsa -P "" -f /etc/ssh/ssh_host_rsa_key  \
    && ssh-keygen -t ecdsa -P "" -f /etc/ssh/ssh_host_ecdsa_key  \
    && ssh-keygen -t ed25519 -P "" -f /etc/ssh/ssh_host_ed25519_key  \
    && echo "root:111111" | chpasswd \
    && npm install -g pnpm \
    && pnpm install -g pm2 \
    && pnpm install -g ts-node typescript tslib \
    && apk --purge del python2 g++ make \
    && rm -rf /root/.npm \
    && rm -rf /root/.pnpm-store \
    && rm -rf /root/.cache 


#ENV PASSWORD="111111"
#RUN echo "root:111111" | chpasswd
ENTRYPOINT ["/usr/bin/node", "/usr/lib/code-server", "--bind-addr", "0.0.0.0:8080"]

