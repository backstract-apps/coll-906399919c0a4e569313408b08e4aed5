from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/schools/')
async def get_schools(db: Session = Depends(get_db)):
    try:
        return await service.get_schools(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/schools/id')
async def get_schools_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_schools_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/schools/')
async def post_schools(raw_data: schemas.PostSchools, db: Session = Depends(get_db)):
    try:
        return await service.post_schools(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/schools/id/')
async def put_schools_id(raw_data: schemas.PutSchoolsId, db: Session = Depends(get_db)):
    try:
        return await service.put_schools_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/schools/id')
async def delete_schools_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_schools_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(raw_data: schemas.PutStudentsId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/external/apis')
async def post_external_apis(db: Session = Depends(get_db)):
    try:
        return await service.post_external_apis(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test')
async def get_test(db: Session = Depends(get_db)):
    try:
        return await service.get_test(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

