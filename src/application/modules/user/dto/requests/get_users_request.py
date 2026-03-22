from pydantic import BaseModel

from src.application.common.shared.pagination.base_pagination import BasePagination


class GetUsersRequest(BaseModel, BasePagination):
    pass
