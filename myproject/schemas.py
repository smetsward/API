from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    item_owner_id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    model: str | None = None

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    product_owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    products: list[Product] = []

    class Config:
        orm_mode = True
