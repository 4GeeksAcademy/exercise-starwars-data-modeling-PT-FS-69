import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

    favorites = relationship('Favorite', back_populates='user')

class Characters(Base):
    __tablename__ = 'Characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    height = Column(String(150))
    Mass = Column(String(150))
    Hair_Color = Column(String(150))
    Skin_Color = Column(String(150))
    Birth_Year = Column(String(150))
    Gende = Column(String(150))
     
    favorites = relationship('Favorite', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(80), nullable=False)
    Climate = Column(String(80) )
    Terrain = Column(String(120) )
    Population = Column(String(80))

    favorites = relationship('Favorite', back_populates='planet')
    
class Favorites(Base):
  __tablename__ = 'favorites'
    # # Here we define columns for the table person
    # # Notice that each column is also a normal Python instance attribute.
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer,ForeignKey('user.id'), nullable=False)
  characters_id = Column(Integer,ForeignKey('characters.id'), nullable=True )
  planet_id = Column(Integer,ForeignKey('planet.id'), nullable=True )
        
  user =relationship('user', back_populates= 'favorites')
  characters =relationship('characters', back_populates= 'favorites')
  planet =relationship('planet', back_populates= 'favorites')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.