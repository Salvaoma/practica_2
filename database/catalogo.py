from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class CATEGORIA(Base):
    __tablename__ = 'CATEGORIA'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[Optional[str]] = mapped_column(String(100))

    PRODUCTO: Mapped[List['PRODUCTO']] = relationship('PRODUCTO', secondary='PRODUCTO_CATEGORIA', back_populates='CATEGORIA_')


class PRODUCTO(Base):
    __tablename__ = 'PRODUCTO'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[Optional[str]] = mapped_column(String(100))
    descripcion: Mapped[Optional[str]] = mapped_column(Text(200))

    CATEGORIA_: Mapped[List['CATEGORIA']] = relationship('CATEGORIA', secondary='PRODUCTO_CATEGORIA', back_populates='PRODUCTO')


t_PRODUCTO_CATEGORIA = Table(
    'PRODUCTO_CATEGORIA', Base.metadata,
    Column('idproducto', ForeignKey('PRODUCTO.id'), nullable=False),
    Column('idcategoria', ForeignKey('CATEGORIA.id'), nullable=False)
)
