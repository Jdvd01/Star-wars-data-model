import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True)
    favorito = relationship("favorito")
    
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(15), nullable = False, unique = False)
    nombre = Column(String(20), nullable = False, unique = False)
    apellido = Column(String(20), nullable = True)

class Favorito(Base):
    __tablename__ = "favorito"
    id = Column(Integer, primary_key = True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("usuario")

    planeta = relationship("planeta")
    planeta_id = Column(Integer, ForeignKey("planeta.id"))

    personaje = relationship("personaje")
    personaje_id = Column(Integer, ForeignKey("personaje.id"))

    vehiculo = relationship("vehiculo")
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))

    nave = relationship("nave")
    nave_id = Column(Integer, ForeignKey("nave.id"))

class Planeta(Base):
    __tablename__ = "planeta"
    id = Column(Integer, primary_key = True)
    favorito = relationship("favorito")

    nombre = Column(String(40), nullable = False, unique = True)
    clima = Column(String(20), nullable = False, unique = False)
    terreno = Column(String(20), nullable = False, unique = False)
    poblacion = Column(Integer, nullable = True)

class Personaje(Base):
    __tablename__ = "personaje"
    id = Column(Integer, primary_key = True)

    nombre = Column(String(20), nullable = False, unique = False)
    genero = Column(String(10), nullable = True)
    edad = Column(Integer, nullable = False, unique = False)

class Vehiculo(Base):
    __tablename__ = "vehiculo"
    id = Column(Integer, primary_key = True)

    nombre = Column(String(30), nullable = False, unique= True)
    modelo = Column(String(30), nullable = False, unique = True)
    costo = Column(Integer, nullable = False, unique = False)
    pasajeros = Column(Integer, nullable = True)


class Nave(Base):
    __tablename__ = "nave"
    id = Column(Integer, primary_key = True)

    nombre = Column(String(30), nullable = False, unique = False)
    modelo = Column(String(30), nullable = False, unique = False)
    costo = Column(Integer, nullable = False, unique = False)
    pasajeros = Column(Integer, nullable = False, unique = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')