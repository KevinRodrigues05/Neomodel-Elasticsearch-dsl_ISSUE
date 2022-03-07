from neomodel import (config,
                      StructuredNode,
                      StringProperty,
                      IntegerProperty,
                      UniqueIdProperty,
                      RelationshipTo,
                      StructuredRel,
                      ArrayProperty)

class Function(StructuredNode):
  index = StringProperty()
  name = StringProperty()
  type = StringProperty()
  description = StringProperty()

  @property
  def serialize(self):
      return {'node_properties': {
          'id': self.id,
          'name': self.name,
          'type':"Method",
          'description': self.description,
      },
      }
