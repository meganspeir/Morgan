from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
#from sqlalchemy.orm import relationship

from morgan.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    email = Column(String(128))
    pwhash = Column(String(256))

    def __init__(self,email,pwhash):
        self.email = email
        self.pwhash = pwhash

    def __repr__(self, email=None, pwhash=None):
        return '<User %r>' % self.email


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    echonest_art_id = Column(String(32))
#    rosetta_art_id = Column()
    stage = Column(String(64))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    url = Column(String(256))

    def __init__(self, name=None, artist_id=None, stage=None, start_time=None,
                 end_time=None, url=None):
        self.name = name
        self.echonest_artist_id = artist_id
        self.rosetta_artist_id = "temp"
        self.stage = stage
        self.start_time = start_time
        self.end_time = end_time
        self.url = url

    def __repr__(self):
        return '<Event %r>' % (self.name)


class Interest(Base):
    __tablename__ = 'interest'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    event_id = Column(Integer, ForeignKey('event.id'))

    def __init__(self, user_id=None, event_id=None):
        self.user_id = user_id
        self.event_id = event_id

    def __repr__():
        return '<Interest %r>' % ()


class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True)
    time_stamp = Column(DateTime)
    rating = Column(Integer)
    user_id = Column(Integer,ForeignKey('user.id'))
    event_id = Column(Integer, ForeignKey('event.id'))

    def __init__(self, time_stamp=None, rating=None, event_id=None,
                 user_id=None):
        self.time_stamp = time_stamp
        self.rating = rating
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        return '<Rating %r>' % (self.id)
