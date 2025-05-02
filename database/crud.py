from sqlalchemy.orm import Session
from catalogo import PRODUCTO, CATEGORIA
from typing import Optional, List, Type

from database.catalogo import PRODUCTO, CATEGORIA


# ---------- CATEGORIA ----------

def crear_categoria(db: Session, nombre: str) -> CATEGORIA:
    categoria = CATEGORIA(nombre=nombre)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def obtener_categorias(db: Session) -> list[Type[CATEGORIA]]:
    return db.query(CATEGORIA).all()

def obtener_categoria_por_id(db: Session, categoria_id: int) -> Optional[CATEGORIA]:
    return db.query(CATEGORIA).filter(CATEGORIA.id == categoria_id).first()

def actualizar_categoria(db: Session, categoria_id: int, nuevo_nombre: str):
    categoria = obtener_categoria_por_id(db, categoria_id)
    if categoria:
        categoria.nombre = nuevo_nombre
        db.commit()
        db.refresh(categoria)
    return categoria

def eliminar_categoria(db: Session, categoria_id: int):
    categoria = obtener_categoria_por_id(db, categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()
    return categoria

# ---------- PRODUCTO ----------

def crear_producto(db: Session, nombre: str, descripcion: str) -> PRODUCTO:
    producto = PRODUCTO(nombre=nombre, descripcion=descripcion)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

def obtener_productos(db: Session) -> list[Type[PRODUCTO]]:
    return db.query(PRODUCTO).all()

def obtener_producto_por_id(db: Session, producto_id: int) -> Optional[PRODUCTO]:
    return db.query(PRODUCTO).filter(PRODUCTO.id == producto_id).first()

def actualizar_producto(db: Session, producto_id: int, nuevo_nombre: str, nueva_desc: str):
    producto = obtener_producto_por_id(db, producto_id)
    if producto:
        producto.nombre = nuevo_nombre
        producto.descripcion = nueva_desc
        db.commit()
        db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = obtener_producto_por_id(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto
