import datetime #<- will be used to set default dates on models
from pyramid_blogr.models.meta import Base  #<- we need to import our sqlalchemy metadata from which model classes will inherit
from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field
)
from webhelpers2.text import urlify #<- will generate slugs
from webhelpers2.date import distance_of_time_in_words #<- human friendly dates


class BlogRecord(Base):
    """ The space of blog record names to database table. """
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(60), nullable=False) # <- Sale or Buy Wheat grade III
    amount = Column(Unicode(10), nullable=False) # <- 500 (T)
    price = Column(Unicode(10), nullable=False)  # <- 4750 (грн.)
    vat = Column(Unicode(30)) # <- First trade agent
    # delivery terms: CPT
    delivery_terms = Column(Unicode(3))
    # grain terminal "MSP NICK-TERA" LLC port "Nikolaev MTP"
    address_delivery = Column(UnicodeText(155), nullable=False, default=u'')
    body = Column(UnicodeText(255), default=u'') # <-  details
    created = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def slug(self):
        return urlify(self.title)

    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created,
                                         datetime.datetime.utcnow())
