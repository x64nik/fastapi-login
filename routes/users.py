import uvicorn
from fastapi import FastAPI, APIRouter, Body, HTTPException, Depends, Request,status

from modles.model import PostSchema, UserSchema, UserLoginSchema
from config.db import conn
from schemas.users import serializeDict, serializeList

from fastapi.security import OAuth2PasswordRequestForm
from auth.oauth import get_current_user
from auth.hashing import Hash
from auth.jwttoken import create_access_token






user = APIRouter()

@user.get("/")
def index(current_user : UserSchema = Depends(get_current_user)):
	return {"data":"Hello OWrld"}

    
    
# Signup 
@user.post("/signup", tags=["user"])
async def user_signup(user : UserSchema = Body(default=None)):
    # users.append(user)
    
    hashed_pass = Hash.bcrypt(user.password)
    user_object = dict(user)
    user_object["password"] = hashed_pass
    conn.user.insert_one(user_object)
    
    return {"msg": "user created"}
    
        
# Login
@user.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends()):
	user = conn.user.find_one({"username":request.username})
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
	if not Hash.verify(user["password"],request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
	access_token = create_access_token(data={"sub": user["username"] })
	return {"access_token": access_token, "token_type": "bearer"}
            





