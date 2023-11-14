from rediscluster import RedisCluster

# 配置Redis集群节点
startup_nodes = [
    {"host": "172.26.152.116", "port": "6379"},
    {"host": "172.26.152.116", "port": "6380"},
    {"host": "172.26.152.117", "port": "6379"}
]

# 创建RedisCluster连接
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True,password="F^uFfMv0YP^CHPpB")

# # 设置键值对
# rc.set('key', 'value')
#
# # 获取键的值
# value = rc.get('key')
# print(value)

# 删除键
ttl = rc.ttl('telecom_access_token_key')
print(rc.get('telecom_access_token_key'))
print(ttl)
