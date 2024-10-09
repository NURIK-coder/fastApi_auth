import datetime
from typing import List

from fastapi import APIRouter

from app.posts.schemas import SCPost, SCPost, SPost
from app.posts.models import Post

router = APIRouter(prefix='/post')


@router.get('/all')
async def get_posts() -> List[SPost]:
    posts = await Post.get_all()
    return posts


@router.post('/create')
async def create_post(data: SCPost)->SPost:
    post = await Post.create(title=data.title, content=data.content, likes_count=data.likes_count)

    # new_post = {
    #     'title': data.title,
    #     'content': data.description,
    #     'likes_count': data.price,
    #     'created_at': datetime.datetime.now()
    # }
    return post

#
# @router.get('/{item_id}')
# async def main(item_id: int, search: str = ''):
#     return {'message': f'item: {item_id}'}

@router.patch('/update/{post_id}')
async def update_post(data: SCPost, post_id: int)->SPost:
    post = await Post.update(record_id=post_id, title=data.title, content=data.content, likes_count=data.likes_count)
    return post

@router.delete('/delete/{post_id}')
async def update_post(data: SCPost, post_id: int):
    post = await Post.delete(filters=Post.id == post_id)
    return {'message': 'Success!'}

@router.get('/{post_id}')
async def detail(post_id: int)->SPost:
    post = await Post.detail(record_id=post_id)
    return post