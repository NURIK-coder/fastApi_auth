from fastapi import APIRouter

from app.category.schema import SCategory
from app.posts.models import Category
from app.posts.schemas import SPost

router = APIRouter(prefix='/category')


@router.get('/list')
async def get_all_categories():
    categories = await Category.get_all()
    return categories


@router.get('/{cat_id}')
async def get_by_id(cat_id: int) -> SCategory:
    category = await Category.detail(record_id=cat_id)

    return category
