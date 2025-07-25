from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_schools(db: Session):

    query = db.query(models.Schools)

    schools_all = query.all()
    schools_all = (
        [new_data.to_dict() for new_data in schools_all] if schools_all else schools_all
    )
    res = {
        "schools_all": schools_all,
    }
    return res


async def get_schools_id(db: Session, id: int):

    query = db.query(models.Schools)
    query = query.filter(and_(models.Schools.id == id))

    schools_one = query.first()

    schools_one = (
        (
            schools_one.to_dict()
            if hasattr(schools_one, "to_dict")
            else vars(schools_one)
        )
        if schools_one
        else schools_one
    )

    res = {
        "schools_one": schools_one,
    }
    return res


async def post_schools(db: Session, raw_data: schemas.PostSchools):
    id: int = raw_data.id
    school_name: str = raw_data.school_name
    city: str = raw_data.city
    created_at: datetime.datetime = raw_data.created_at

    record_to_be_added = {
        "id": id,
        "city": city,
        "created_at": created_at,
        "school_name": school_name,
    }
    new_schools = models.Schools(**record_to_be_added)
    db.add(new_schools)
    db.commit()
    db.refresh(new_schools)
    schools_inserted_record = new_schools.to_dict()

    res = {
        "schools_inserted_record": schools_inserted_record,
    }
    return res


async def put_schools_id(db: Session, raw_data: schemas.PutSchoolsId):
    id: int = raw_data.id
    school_name: str = raw_data.school_name
    city: str = raw_data.city
    created_at: datetime.datetime = raw_data.created_at

    query = db.query(models.Schools)
    query = query.filter(and_(models.Schools.id == id))
    schools_edited_record = query.first()

    if schools_edited_record:
        for key, value in {
            "id": id,
            "city": city,
            "created_at": created_at,
            "school_name": school_name,
        }.items():
            setattr(schools_edited_record, key, value)

        db.commit()
        db.refresh(schools_edited_record)

        schools_edited_record = (
            schools_edited_record.to_dict()
            if hasattr(schools_edited_record, "to_dict")
            else vars(schools_edited_record)
        )
    res = {
        "schools_edited_record": schools_edited_record,
    }
    return res


async def delete_schools_id(db: Session, id: int):

    query = db.query(models.Schools)
    query = query.filter(and_(models.Schools.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        schools_deleted = record_to_delete.to_dict()
    else:
        schools_deleted = record_to_delete
    res = {
        "schools_deleted": schools_deleted,
    }
    return res


async def get_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def put_students_id(db: Session, raw_data: schemas.PutStudentsId):
    id: int = raw_data.id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age
    grade: str = raw_data.grade
    school_id: int = raw_data.school_id
    enrolled_at: datetime.datetime = raw_data.enrolled_at

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {
            "id": id,
            "age": age,
            "email": email,
            "grade": grade,
            "full_name": full_name,
            "school_id": school_id,
            "enrolled_at": enrolled_at,
        }.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    id: int = raw_data.id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age
    grade: str = raw_data.grade
    school_id: int = raw_data.school_id
    enrolled_at: str = raw_data.enrolled_at

    record_to_be_added = {
        "id": id,
        "age": age,
        "email": email,
        "grade": grade,
        "full_name": full_name,
        "school_id": school_id,
        "enrolled_at": enrolled_at,
    }
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    headers = {}
    headers["Authorization"] = (
        "Bearer v4.public.eyJlbWFpbF9pZCI6ICJsYXppZHlxYWh5QHlvcG1haWwuY29tIiwgInVzZXJfaWQiOiAiODFmY2E4MzRlM2MxNGU2MjlmMGE0ZmVjMGM0MTg0ODIiLCAib3JnX2lkIjogIk5BIiwgInN0YXRlIjogInNpZ251cCIsICJyb2xlX25hbWUiOiAiTkEiLCAicm9sZV9pZCI6ICJOQSIsICJwbGFuX2lkIjogbnVsbCwgImFjY291bnRfdmVyaWZpZWQiOiAiMSIsICJhY2NvdW50X3N0YXR1cyI6ICIwIiwgInVzZXJfbmFtZSI6ICI4MWZjYTgzNGUzYzE0ZTYyOWYwYTRmZWMwYzQxODQ4MiIsICJzaWdudXBfcXVlc3Rpb24iOiAwLCAiZXhwIjogMzUwNzcxODM5Ni40OTAzNTkzLCAiZXhwaXJ5X3RpbWUiOiAzNTA3NzE4Mzk2fbLtPAgPqkrTOr0gFWSgnFNJRx3eeQWpLIBEd69JmwYc34A2fr2Mi5nyg9TEYk3R8vR7gOjh3Khp7-JhtI7sZQc"
    )
    payload = {"workspace_description": full_name, "workspace_name": full_name}
    apiResponse = requests.post(
        "https://api.beemerbenzbentley.site/sigma/api/v1/workspace/create",
        headers=headers,
        json=payload if "raw" == "raw" else None,
    )
    sadgfh = apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    res = {
        "students_inserted_record": students_inserted_record,
        "asdghjj": sadgfh,
    }
    return res


async def post_external_apis(db: Session):
    res = {}
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )

    headers = {}
    headers["Authorization"] = (
        "Bearer v4.public.eyJlbWFpbF9pZCI6ICJsYXppZHlxYWh5QHlvcG1haWwuY29tIiwgInVzZXJfaWQiOiAiODFmY2E4MzRlM2MxNGU2MjlmMGE0ZmVjMGM0MTg0ODIiLCAib3JnX2lkIjogIk5BIiwgInN0YXRlIjogInNpZ251cCIsICJyb2xlX25hbWUiOiAiTkEiLCAicm9sZV9pZCI6ICJOQSIsICJwbGFuX2lkIjogbnVsbCwgImFjY291bnRfdmVyaWZpZWQiOiAiMSIsICJhY2NvdW50X3N0YXR1cyI6ICIwIiwgInVzZXJfbmFtZSI6ICI4MWZjYTgzNGUzYzE0ZTYyOWYwYTRmZWMwYzQxODQ4MiIsICJzaWdudXBfcXVlc3Rpb24iOiAwLCAiZXhwIjogMzUwNzcxODM5Ni40OTAzNTkzLCAiZXhwaXJ5X3RpbWUiOiAzNTA3NzE4Mzk2fbLtPAgPqkrTOr0gFWSgnFNJRx3eeQWpLIBEd69JmwYc34A2fr2Mi5nyg9TEYk3R8vR7gOjh3Khp7-JhtI7sZQc"
    )
    payload = {}
    apiResponse = requests.get(
        "https://api.beemerbenzbentley.site/sigma/api/v1/workspace/list",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    dfghjj = apiResponse.json() if "dict" in ["dict", "list"] else apiResponse.text
    res = {
        "students_all": students_all,
        "sfdghjg": dfghjj,
    }
    return res


async def get_test(db: Session):

    try:
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        print(thisdict["brand"])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    test1234 = {}  # Creating new dict

    dict1: Any = "test"

    thisdict["model"] = test1234

    dict1 = thisdict.get("model")
    res = {
        "dfgdfg": thisdict,
        "fsdg": dict1,
    }
    return res
