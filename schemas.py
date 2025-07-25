from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Schools(BaseModel):
    school_name: str
    city: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadSchools(BaseModel):
    school_name: str
    city: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Students(BaseModel):
    full_name: str
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None


class ReadStudents(BaseModel):
    full_name: str
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True




class PostSchools(BaseModel):
    id: Optional[int]=None
    school_name: Optional[str]=None
    city: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutSchoolsId(BaseModel):
    id: Optional[int]=None
    school_name: Optional[str]=None
    city: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutStudentsId(BaseModel):
    id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[str]=None

    class Config:
        from_attributes = True

