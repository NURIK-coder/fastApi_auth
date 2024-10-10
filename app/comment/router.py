from fastapi import APIRouter, Form

from app.comment.models import Comment

router = APIRouter(prefix='/comments')


@router.post('/create')
async def create_comment(text: str = Form(), post_id: int = Form()):
    comment = await Comment.create(text=text, post_id=post_id)
    return comment


@router.patch('/update/{comment_id}')
async def update_comment(comment_id: int, text: str = Form(), post_id: int = Form()):
    comment = await Comment.update(record_id=comment_id, text=text, post_id=post_id)
    return comment


@router.delete('/delete/{comment_id}')
async def delete_comment(comment_id: int):
    comment = await  Comment.delete(filters=Comment.id == comment_id)
    return {'message': 'Success'}


@router.post('/create/{com_id}/')
async def get_comment(comment_id: int, text: str = Form()):
    comment = await Comment.detail(record_id=comment_id)
    new_comment = await comment.create(text=text)
    return new_comment
