# puppy queries


"""
1. Query all of the puppies and return the results in ascending alphabetical order

2. Query all of the puppies that are less than 6 months old organized by the youngest first

3. Query all puppies by ascending weight

4. Query all puppies grouped by the shelter in which they are staying
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def queryAll():
	"""1. Query all of the puppies and return the
	results in ascending alphabetical order
	"""
	names = session.query(Puppy).order_by(Puppy.name).all()

	# for name in names:
	# 	print name.name

	return names


def lessThanSixMo():
	"""2. Query all of the puppies that are less than
	6 months old organized by the youngest first
	"""

	# calculatie 6 months
	today = datetime.date.today()
	sixmonths = datetime.timedelta(weeks = 26)
	cutoff = today - sixmonths

	result = session.query(Puppy).filter(Puppy.dateOfBirth > diff)\
		.order_by(Puppy.dateOfBirth.desc())

	return result



def puppiesByWeight():
	"""3. Query all puppies by ascending weight
	"""
	pups = session.query(Puppy).order_by(Puppy.weight).all()
	return pups


def pupsGroupByShelter():
	"""4. Query all puppies grouped by the shelter
	in which they are staying
	"""
	pups = session.query(Puppy).order_by(Puppy.shelter_id).all()
	return pups


