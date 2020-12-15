<!--
 * @Author: mukangt
 * @Date: 2020-12-15 14:50:11
 * @LastEditors: mukangt
 * @LastEditTime: 2020-12-15 14:50:46
 * @Description: 
-->
### 容器部署
```
podman build -t dl_grpc_model .
```
### 服务运行
```
podman run --security-opt=label=disable -p 47260:47260 -itd localhost/dl_grpc_model &
```