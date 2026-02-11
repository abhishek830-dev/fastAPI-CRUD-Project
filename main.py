import os
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Product, ProductResponse
from database import SessionLocal, engine
import database_models
from mockData import products


# ============================
#       APP INSTANCE
# ============================

app = FastAPI()


# ============================
#           CORS
# ============================

# Explicitly allow your frontend URLs
origins = [
    "http://localhost:5173",  # Local Vite frontend
    "https://fast-api-crud-project.vercel.app",  # Production Vercel frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================
#        STARTUP EVENT
# ============================

@app.on_event("startup")
def startup_event():
    print("🚀 App Starting...")
    database_models.Base.metadata.create_all(bind=engine)
    init_db()


@app.get("/")
def greet():
    return {"message": "API is running 🚀 after new Cors Changes"}


# ============================
#     DATABASE DEPENDENCY
# ============================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================
#       INIT DATABASE
# ============================

def init_db():
    db = SessionLocal()
    try:
        count = db.query(database_models.Product).count()
        if count == 0:
            for product in products:
                db.add(database_models.Product(**product.model_dump()))
            db.commit()
            print("✅ Mock data inserted")
    except Exception as e:
        print("DB INIT ERROR:", e)
    finally:
        db.close()


# ============================
#           ROUTES
# ============================

@app.get("/products", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/products/{id}", response_model=ProductResponse)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@app.post("/products", response_model=ProductResponse)
def add_product(product: Product, db: Session = Depends(get_db)):
    new_product = database_models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.put("/products/{id}", response_model=ProductResponse)
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db_product.category = product.category

    db.commit()
    db.refresh(db_product)

    return db_product


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted successfully"}
