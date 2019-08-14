from elasticsearch import Elasticsearch

#连接es服务器
es = Elasticsearch(["10.10.21.140"],timeout=360)

#插入索引
data = {
    "mappings":{
        "properties":{
            "title": {
                "type": "text",
                "index": True
            },
            "keywords": {
                "type": "text",
                "index": True
            },
            "link": {
                "type": "string",
                "index": True
            },
            "content": {
                "type": "text",
                "index": True
            }
        }
    }
}

es.indices.create(index = "pythonTest",body = data)
#查看索引
#es.search()