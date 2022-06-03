from typing import TypeVar

from beanie import Document, Indexed, Insert, Replace, SaveChanges, before_event

DocType = TypeVar("DocType", bound="Document")


class Slug(Document):
    collection: str
    counter: int

    class Settings:
        name = "slug"

    def slug_string(self):
        return self.collection[:2].upper() + f"{self.counter}".zfill(8)


class SlugMixin:
    slug: Indexed(str, unique=True) = ""

    async def next_slug(self: DocType) -> str:
        # TODO: this function is not thread safe yet
        collection_name = self.get_settings().name
        slug = await Slug.find_one(Slug.collection == collection_name)
        if slug is None:
            slug = Slug(collection=collection_name, counter=0)
        slug.counter = slug.counter + 1
        await slug.save()
        return slug.slug_string()

    @before_event([Insert, Replace, SaveChanges])
    async def set_slug(self):
        if self.slug == "":
            self.slug = await self.next_slug()
