import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)



class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
  #  planet_climate = relationship(favoritePlanet)
   
class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    planet_id = Column(Integer,ForeignKey("planet.id"))

   #  ForeignKey("planets.id,user.id")
    person = relationship(User)
    planet = relationship(Planet)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
  #  planet_climate = relationship(favoritePlanet)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    character_id = Column(Integer,ForeignKey("character.id"))

   #  ForeignKey("planets.id,user.id")
    person = relationship(User)
    character = relationship(Character)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
  #  planet_climate = relationship(favoritePlanet)

class FavoriteVehicler(Base):
    __tablename__ = 'favorite_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    vehicle_id = Column(Integer,ForeignKey("vehicle.id"))

   #  ForeignKey("planets.id,user.id")
    person = relationship(User)
    vehicle = relationship(Vehicle)

#class Vehicle(Base):
 #   __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #name = Column(Integer, primary_key=True)
    #model = Column(String(250))
    #manufacturer = Column(String(250))
    #cost_in_credits = Column(String(250), nullable=False)
    #crew = Column(Integer)
  #  cargo_capacity = relationship(user,favoriteVehicle)




#class FavoriteVehicle(Base):
    # __tablename__ = 'favoritevehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
   ## id = Column(Integer, primary_key=True)
   # Character_name = Column(String(250))
   # Character_height = Column(String(250))
   # Character_gender = Column(String(250), nullable=False)
   #· Character_haircolor = Column(String(250), ForeignKey("vehicles.id,user.id"))
   # person = relationship(vehicles)
    
#class FavoriteCharacter(Base):
 #   __tablename__ = 'favoritecharacter'
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
    # Here we define columns for the table address.
   # Character_name = Column(String(250))
    #Character_height = Column(String(250))
   # Character_gender = Column(String(250), nullable=False)
    #Character_haircolor = Column(String(250), ForeignKey("characters.id,user.id"))
  #  person = relationship(characters,user)
    
    
#class Character(Base):
 #   __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
   # Character_name = Column(String(250))
    #Character_height = Column(String(250))
 #   Character_gender = Column(String(250), nullable=False)
  #  Character_haircolor = Column(String(250))
   # person = relationship(user,favoriteCharacters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
