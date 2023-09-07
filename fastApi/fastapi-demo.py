from fastapi import FastAPI
import uvicorn
import pymysql

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": f"接口id：{item_id}"}

@app.post("/hot_search")
async def read_hot_search():
    # 创建连接
    cnx = pymysql.connect(host='127.0.0.1', user='root',
                          password='123456', db='weibo_data')
    # 创建游标
    cursor = cnx.cursor()
    # 执行查询
    query = ("SELECT * FROM cop_callback_0825")
    cursor.execute(query)
    # 获取查询结果
    result = cursor.fetchall()
    # 关闭游标和连接
    cursor.close()
    cnx.close()
    # 返回查询结果
    return result
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8066)
