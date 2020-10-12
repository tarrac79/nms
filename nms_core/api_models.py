from typing import Optional, Generic, List, Union, Dict

from dataclasses import dataclass

from .base_api import RT
from .models.findparam import FindParams


@dataclass
class RequestBody:
    action: str
    object: Optional[str] = None
    from_: Optional[int] = None
    to_: Optional[int] = None
    find: Optional[FindParams] = None
    id: Optional[int] = None


@dataclass
class Request:
    request: Optional[RequestBody]
    data: Optional[Dict] = None


@dataclass
class ResponseResult:
    errno: int
    message: str
    id: Optional[Union[List[int], int]]
    type: Optional[str]


@dataclass
class Response(Generic[RT]):
    result: Optional[ResponseResult]
    data: Optional[RT]
