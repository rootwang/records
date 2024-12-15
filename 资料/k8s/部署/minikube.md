# 前言

minikube : local k8s

# mac

https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Fx86-64%2Fstable%2Fbinary+download

1）安装

```
curl -LO https://github.com/kubernetes/minikube/releases/download/v1.34.0/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube
```

如果上面的方法慢，也可以用下面的方法，可以换下面的方法

```
wget https://objects.githubusercontent.com/github-production-release-asset-2e65be/56353740/5179bc9b-9594-442c-8d0e-aed77282bcd6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240626%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240626T085536Z&X-Amz-Expires=300&X-Amz-Signature=e8ef8486817f6bb5993d31519b24417fb3e5a560dfaf9cf80dc0d98fd812bd5f&X-Amz-SignedHeaders=host&actor_id=5188320&key_id=0&repo_id=56353740&response-content-disposition=attachment%3B%20filename%3Dminikube-darwin-amd64.tar.gz&response-content-type=application%2Foctet-stream

tar -zxvf minikube-darwin-amd64.tar.gz
cd out
mv minikube-darwin-amd64 /usr/local/bin/minikube
```

校验

```
gwm@SHJS-C02DV070MD6P out % minikube version
minikube version: v1.33.1
commit: 5883c09216182566a63dff4c326a6fc9ed2982ff
```

2）启动

```
minikube start       
```
结果报错：
```
wangxin@wangxindeMacBook-Pro minikube % minikube start 

😄  Darwin 15.1.1 (arm64) 上的 minikube v1.34.0
👎  无法选择默认驱动程序。以下是按优先顺序考虑的内容：
💡  或者你也可以安装以下驱动程序：
    ▪ docker: Not installed: exec: "docker": executable file not found in $PATH
    ▪ hyperkit: Not installed: exec: "hyperkit": executable file not found in $PATH
    ▪ parallels: Not installed: exec: "prlctl": executable file not found in $PATH
    ▪ qemu2: Not installed: exec: "qemu-system-aarch64": executable file not found in $PATH
    ▪ virtualbox: Not installed: unable to find VBoxManage in $PATH
    ▪ vfkit: Not installed: exec: "vfkit": executable file not found in $PATH
    ▪ podman: Not installed: exec: "podman": executable file not found in $PATH
    
❌  因 DRV_NOT_DETECTED 错误而退出：未检测到可用的驱动程序。尝试指定 --driver，或查看 https://minikube.sigs.k8s.io/docs/start/
```
这个问题是因为没有安装docker

## 使用

```
minikube kubectl -- get po -A # 会下载一个适当的kubectl版本
alias kubectl="minikube kubectl --"
```

## 开启dashboard

1、minikube dashboard

```
# 开启dashboard
minikube dashboard
🤔  正在验证 dashboard 运行情况 ...
🚀  正在启动代理...
🤔  正在验证 proxy 运行状况 ...

❌  因 SVC_URL_TIMEOUT 错误而退出：http://127.0.0.1:50292/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ 不可访问：Temporary Error: unexpected response code: 503
```

原因排查

```
gwm@SHJS-C02DV070MD6P Downloads % kubectl get pods -A
NAMESPACE              NAME                                        READY   STATUS             RESTARTS        AGE
kube-system            coredns-7db6d8ff4d-btxzn                    1/1     Running            0               7h18m
kube-system            etcd-minikube                               1/1     Running            0               7h18m
kube-system            kube-apiserver-minikube                     1/1     Running            0               7h18m
kube-system            kube-controller-manager-minikube            1/1     Running            0               7h18m
kube-system            kube-proxy-9pjbg                            1/1     Running            0               7h18m
kube-system            kube-scheduler-minikube                     1/1     Running            0               7h18m
kube-system            storage-provisioner                         1/1     Running            1 (7h18m ago)   7h18m
kubernetes-dashboard   dashboard-metrics-scraper-b5fc48f67-krbmm   0/1     ImagePullBackOff   0               135m
kubernetes-dashboard   kubernetes-dashboard-779776cb65-92kbn       0/1     ImagePullBackOff   0               135m

gwm@SHJS-C02DV070MD6P Downloads %  kubectl describe --namespace=kubernetes-dashboard po kubernetes-dashboard-779776cb65-92kbn
Name:             kubernetes-dashboard-779776cb65-92kbn
Namespace:        kubernetes-dashboard
Priority:         0
Events:
  Type     Reason   Age                  From     Message
  ----     ------   ----                 ----     -------
  Warning  Failed   17h                  kubelet  Failed to pull image "docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93": error pulling image configuration: download failed after attempts=6: dial tcp 69.171.224.36:443: i/o timeout
  Warning  Failed   16h                  kubelet  (combined from similar events): Failed to pull image "docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93": error pulling image configuration: download failed after attempts=6: dial tcp 157.240.2.50:443: i/o timeout
  Warning  Failed   16h (x4 over 17h)    kubelet  Failed to pull image "docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93": error pulling image configuration: download failed after attempts=6: dial tcp 157.240.16.50:443: i/o timeout
  Warning  Failed   16h (x7 over 18h)    kubelet  Failed to pull image "docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93": rpc error: code = Canceled desc = context canceled
  Normal   BackOff  16h (x336 over 18h)  kubelet  Back-off pulling image "docker.io/kubernetesui/dashboard:v2.7.0@sha256:2e500d29e9d5f4a086b908eb8dfe7ecac57d2ab09d65b24f588b1d449841ef93"
```

无法下载 docker.io/kubernetesui/dashboard:v2.7.0，换成国内镜像
```
minikube ssh
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/dashboard:v2.7.0
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/dashboard:v2.7.0 docker.io/kubernetesui/dashboard:v2.7.0
```

另外还有个问题:kubernetes-dashboard   dashboard-metrics-scraper-b5fc48f67-krbmm   0/1     ImagePullBackOff

--javascripttypescriptshellbashsqljsonhtmlcssccppjavarubypythongorustmarkdown

```
kubectl describe --namespace=kubernetes-dashboard po dashboard-metrics-scraper-b5fc48f67-krbmm
Events:
  Type     Reason   Age                     From     Message
  ----     ------   ----                    ----     -------
  Warning  Failed   2d7h                    kubelet  Failed to pull image "docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c": error pulling image configuration: download failed after attempts=6: dial tcp 104.244.46.63:443: i/o timeout
  Normal   Pulling  2d7h (x150 over 3d1h)   kubelet  Pulling image "docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c"
  Warning  Failed   2d7h (x133 over 2d23h)  kubelet  (combined from similar events): Failed to pull image "docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c": error pulling image configuration: download failed after attempts=6: dial tcp 66.220.146.94:443: i/o timeout
  Normal   BackOff  2d6h (x3238 over 3d1h)  kubelet  Back-off pulling image "docker.io/kubernetesui/metrics-scraper:v1.0.8@sha256:76049887f07a0476dc93efc2d3569b9529bf982b22d29f356092ce206e98765c"

minikube ssh
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-scraper:v1.0.8
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/metrics-scraper:v1.0.8 docker.io/kubernetesui/metrics-scraper:v1.0.8
```

# Linux

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```