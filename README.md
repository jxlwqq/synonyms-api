# synonyms-api

> synonyms 可以用于自然语言理解的很多任务：文本对齐，推荐算法，相似度计算，语义偏移，关键字提取，概念提取，自动摘要，搜索引擎等。

本项目基于 [Synonyms](https://github.com/chatopera/Synonyms) 和 [Flask](https://github.com/pallets/flask) 构建了一个 Web 中文近义词服务。

## 部署

#### 本地环境
```shell
pip3 install -r requirements.txt
python3 app.py
```

访问：
```shell
curl http://127.0.0.1:5000/synonyms/人脸?size=10
```

#### Docker

```shell
docker pull jxlwqq/synonyms-api
docker run -p 5000:5000 jxlwqq/synonyms-api
```

访问：

```shell
curl http://127.0.0.1:5000/synonyms/人脸?size=10
```

#### Kubernetes

```shell
kubectl apply -f ./kubernetes/deploy.yaml
```

在集群中访问：

```shell
curl synonyms-svc:5000/synonyms/人脸?size=10
```
