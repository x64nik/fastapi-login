import uvicorn
from fastapi import APIRouter, Body, Depends
from modles.model import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer


posts = [
    {
        "id": 1,
        "title": "red",
        "text": "red color it is"
        
    },
    {
        "id": 2,
        "title": "green",
        "text": "green color it is"
        
    },
    {
        "id": 3,
        "title": "blue",
        "text": "blue color it is"
    }
]


users = []

user = APIRouter()

@user.get("/", tags=["test"])
def index():
    # return {"Hello": "world!"}
    return { 
        "data": users
    }


@user.get("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def get_posts():
    return {"data": posts}

@user.get("/posts/{id}", tags=["posts"])
def get_one_posts(id : int):
    if id == 0 or id > len(posts):
        return {
            "error": "Post id not exist!"
        }
        
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
            

@user.post("/posts", tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    
    return {
        "info": "Post Added!"
    }
    
   

    
    
# Signup 
@user.post("/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False
# Login
@user.post("/login", tags=["user"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        print(user.email)
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid Login details!"
        }

            





