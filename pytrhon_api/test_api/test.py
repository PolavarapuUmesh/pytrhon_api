from fastapi import FastAPI,HTTPException,security
# from fastapi.security import HTTPBasic,HTTPBearer,OAuth2PasswordBearer
from fastapi.responses import JSONResponse
# from pydantic import BaseModel
app=FastAPI()

# seurity = HTTPBasic()

# class user(BaseModel):
#     username:str
#     password:str

# users=[
#     user(username='user1',password='password1'),
#     user(username='user2',password='paswword2')
# ]

# def authenticate_user(username:str,password:str):
#     for user in users:
#         if user.username==username and user.password==password:
#             return users
#         return None
# def authentication_user_pass(username):
#     for user in :
        
#get_user
@app.get('/')
def health_check():
    return JSONResponse(content={"status":"Running"})

#post_user
@app.post('/user/data')
def user_data():
    response={"user_id":1000,
            "user_data":"student1"}           
    return JSONResponse(content=response)

#put_user
@app.put('/add/user/data')
def add_user_data():
    insert_data=[{"user_id":1001,"user_data":"student2"} ,{"user_id":1002,"user_data":"student3"}]
    return JSONResponse(content=insert_data)

#delete_user
@app.delete("/user/data/{user_id}")
def delete_user_data(user_id:int):
    remove_data={"user_id":user_id,"user_data":"student1"}    
    return JSONResponse(content=remove_data)

result=user_data()
result_1=add_user_data()
result_2=delete_user_data(1000)
print("Response_POST_Method",result.body)
print("Response_PUT_Method",result_1.body)
print("Response_DELETE_Method",result_2.body)
print("success_code")