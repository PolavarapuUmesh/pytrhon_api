from fastapi import FastAPI
app=FastAPI()
@app.get('/user/data')
def read():
        return{'data':'user_data'}
print("success")
