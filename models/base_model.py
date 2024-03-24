#!/usr/bin/python3
"""
Module for creating baseClass

"""
import uuid
from datetime import datetime



class BaseModel:
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()

	def save(self):
		"""

		"""
		self.updated_at = datetime.utcnow()

	def to_dict(self):
		"""
		
		"""
		ob_dic = self.__dict__.copy()
		ob_dic["__class__"] = self.__class__.__name__
		ob_dic["created_at"] = self.created_at.isoformat()
		ob_dic["updated_at"] = self.updated_at.isoformat()
		return ob_dic
	def __str__(self):
		"""

		"""
		className = self.__class__.__name__
		return "[{}] ({}) {}".format(className, self.id, self.__dict__)

if __name__ == "__main__":
	my_model = BaseModel()
	my_model.name = "My First Model"
	my_model.my_number = 89
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
		print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
