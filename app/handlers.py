
from platform import release
import uuid
from fastapi import APIRouter, Body, Depends, HTTPException
from app.forms import UserLoginForm
from app.models import connect_db, User, AuthToken
from app.utils import get_password_hash

 

router =  APIRouter()

@router.get('/')
def index():
    return {'status':'OK'}



@router.post('/login', name='user:login')
def login(user_from: UserLoginForm =Body(..., embed=True), database=(Depends(connect_db))):
    user = database.query(User).filter(User.email ==user_from.email).one_or_none()
    if not user or get_password_hash(user_from.password) != user.password:
        return {'error':'Email/Password invalid'}
    
    
    
    auth_token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    database.add(auth_token)
    database.commit()
    return {'status':'OK'}

@router.post('/user',name='user:create')
def create_user(user : UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    exist_user=database.query(User.id).filter(User.email == user.email).one_or_none()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= 'Email allready exists')

    new_user = User(
        mail=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        nickname=user.nickname
    )
    database.add(new_user)
    database.commit()
    return {'user_id':new_user.id}
