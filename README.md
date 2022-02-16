<p align="center">
  <a href="https://github.com/whyour/qinglong">
    <img width="150" src="https://z3.ax1x.com/2021/11/18/I7MpAe.png">
  </a>
</p>

<h1 align="center">青龙</h1>

<div align="center">

青龙面板 + 集成 code server
</div>



## 部署



### docker 部署

0. docker 基础镜像打包（打包whyour/ql:base 镜像）

```bash
cd $HOME/qinglong-code-server/mydocker/base
sh builddocker.sh
```

1. docker 打包 qinglong-code-server 镜像

```bash
cd $HOME/qinglong-code-server/
sh builddocker.sh
```

2. 启动容器

```bash
cd $HOME/qinglong-code-server/
sh builddocker.sh
```

3. 启动容器

```bash
sh rundocker.sh
```

## 使用

0.端口使用情况
- 打开你的浏览器，访问青龙面板 http://127.0.0.1:5700 <br>
admin/111111
- ssh，ssh root@host -p5722 <br>
password=111111
- code server访问地址 http://127.0.0.1:8080 <br>
password=111111

1. 内置命令

```bash
# 更新并重启青龙
ql update                                                    
# 运行自定义脚本extra.sh
ql extra                                                     
# 添加单个脚本文件
ql raw <file_url>                                             
# 添加单个仓库的指定脚本
ql repo <repo_url> <whitelist> <blacklist> <dependence> <branch>   
# 删除旧日志
ql rmlog <days>                                              
# 启动tg-bot
ql bot                                                       
# 检测青龙环境并修复
ql check                                                     
# 重置登录错误次数
ql resetlet                                                  
# 禁用两步登录
ql resettfa                                                  

# 依次执行，如果设置了随机延迟，将随机延迟一定秒数
task <file_path>                                             
# 依次执行，无论是否设置了随机延迟，均立即运行，前台会输出日，同时记录在日志文件中
task <file_path> now                                         
# 并发执行，无论是否设置了随机延迟，均立即运行，前台不产生日，直接记录在日志文件中，且可指定账号执行
task <file_path> conc <env_name> <account_number>(可选的) 
# 指定账号执行，无论是否设置了随机延迟，均立即运行 
task <file_path> desi <env_name> <account_number>         
```

2. 参数说明

* file_url: 脚本地址
* repo_url: 仓库地址
* whitelist: 拉取仓库时的白名单，即就是需要拉取的脚本的路径包含的字符串
* blacklist: 拉取仓库时的黑名单，即就是需要拉取的脚本的路径不包含的字符串
* dependence: 拉取仓库需要的依赖文件，会直接从仓库拷贝到scripts下的仓库目录，不受黑名单影响
* branch: 拉取仓库的分支
* days: 需要保留的日志的天数
* file_path: 任务执行时的文件路径
* env_name: 任务执行时需要并发或者指定时的环境变量名称
* account_number: 任务执行时指定某个环境变量需要执行的账号序号

## 链接

- [qinglong](https://github.com/whyour/qinglong)
- [code-server](https://github.com/coder/code-server)
- [martinussuherman/alpine-code-server](https://github.com/martinussuherman/alpine-code-server/blob/master/code-server)
- [nevinee](https://gitee.com/evine)
- [crontab-ui](https://github.com/alseambusher/crontab-ui)
- [Ant Design](https://ant.design)
- [Ant Design Pro](https://pro.ant.design/)
- [Umijs3.0](https://umijs.org)
- [darkreader](https://github.com/darkreader/darkreader)
- [admin-server](https://github.com/sunpu007/admin-server)




