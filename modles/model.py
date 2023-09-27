from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    
    class Config:
        schema_extra = {
            "post_demo" : {
                "title": "some title about animals",
                "content": "some content about animals"
            }
        }
        
class UserSchema(BaseModel):
    username : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    
    class Config:
        schema_extra = {
            "user_demo": {
                "username": "nik",
                "email": "test@test.com",
                "password": "anything"
            }
        }
    

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    
    class Config:
        schema_extra = {
            "user_demo": {
                "email": "test@test.com",
                "password": "anything"
            }
        }
    
    
    