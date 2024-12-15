# 部署与安装

请[参考](https://kubesphere.io/zh/blogs/deploy-kubesphere-on-debian12/)如下内容

## 问题记录

### conntrack is required

kubesphere 部署 报错 conntrack is required，那就安装吧
```
sudo apt-get update
# 报错
Please use apt-cdrom to make this CD-ROM recognized by APT. apt-get update cannot be used to add new CD-ROMs
Reading package lists... Done
E: The repository 'cdrom://[Debian GNU/Linux 12.7.0 _Bookworm_ - Official amd64 DVD Binary-1 with firmware 20240831-10:40] bookworm Release' does not have a Release file.
```

解决：
```
vim /etc/apt/sources.list
# 将其中CD-ROM的条目注释掉，并添加
deb https://deb.debian.org/debian bookworm main contrib
```

接着执行就好了
```
sudo apt-get update
sudo apt-get install conntrack
```

### 忘记admin密码
```shell
kubectl patch users admin -p '{"spec":{"password":"P@88w0rd"}}' --type='merge' && kubectl annotate users admin iam.kubesphere.io/password-encrypted-
```
# 使用

## 登录

[http://192.168.22.32:30880/dashboard](http://192.168.22.32:30880/dashboard)

# 参考

[官网](https://kubesphere.io/zh/docs/v3.3/quick-start/)
