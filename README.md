# synonyms-api

> synonyms 可以用于自然语言理解的很多任务：文本对齐，推荐算法，相似度计算，语义偏移，关键字提取，概念提取，自动摘要，搜索引擎等。

本项目基于 [Synonyms](https://github.com/chatopera/Synonyms) 和 [Flask](https://github.com/pallets/flask) 构建了一个 Web 中文近义词服务。

## 部署

### 本地环境

```shell
pip3 install -r requirements.txt
python3 app.py
```

访问：

```shell
curl http://127.0.0.1:5000/synonyms/人脸?size=10
```

返回：

```json5
{
  "nearby": [ // 同义词
    "图片",
    "图像",
    "通过观察",
    "数字图像",
    "几何图形",
    "脸部",
    "图象",
    "放大镜",
    "面孔",
    "Mii"
  ],
  "scores": [ // 分数
    0.597284,
    0.580373,
    0.568486,
    0.535674,
    0.531835,
    0.530095,
    0.525344,
    0.524009,
    0.523101,
    0.516046
  ],
  size: 10, // 返回数量
  "word": "人脸" // 原始字词
}
```

### Docker

镜像地址：https://hub.docker.com/repository/docker/jxlwqq/synonyms-api

```shell
docker pull jxlwqq/synonyms-api
docker run -p 5000:5000 jxlwqq/synonyms-api
```

访问：

```shell
curl http://127.0.0.1:5000/synonyms/人脸?size=10
```

### Kubernetes

```shell
kubectl apply -f ./kubernetes/deploy.yaml
```

在集群中访问：

```shell
curl synonyms-svc:5000/synonyms/人脸?size=10
```
