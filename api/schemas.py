from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    raw_id: str | None
    date: str | None
    amount: float | None
    phone: str | None
    category: str | None


class CategorySummary(BaseModel):
    category: str
    count: int
    total_amount: float
