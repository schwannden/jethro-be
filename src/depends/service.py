from awesome_exception.exceptions import NotFound

from domain.service.schema import Order


async def get_order(slug: str) -> Order:
    doc = await Order.find_one(Order.slug == slug)
    if doc is None:
        raise NotFound(f"transaction {slug} not found")

    return doc
