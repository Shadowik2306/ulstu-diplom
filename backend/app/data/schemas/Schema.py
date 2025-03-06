from pydantic import BaseModel


class PaginationSchema(BaseModel):
    page: int
    size: int
    total_pages: int
