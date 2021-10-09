

from sqlalchemy import Column, Numeric
from sqlalchemy import String

from . import BASE, SESSION


class NOLogPMs(BASE):
    __tablename__ = "no_log_pms"
    chat_id = Column(Numeric, primary_key=True)

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id


NOLogPMs.__table__.create(checkfirst=True)

class KRead(BASE):
    __tablename__ = "kread"
    groupid = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.groupid = str(sender)


KRead.__table__.create(checkfirst=True)


def is_approved(chat_id):
    try:
        return SESSION.query(NOLogPMs).filter(NOLogPMs.chat_id == chat_id).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def approve(chat_id):
    adder = NOLogPMs(chat_id)
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(NOLogPMs).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def is_kread():
    try:
        return SESSION.query(KRead).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def kread(chat):
    adder = KRead(str(chat))
    SESSION.add(adder)
    SESSION.commit()


def unkread(chat):
    rem = SESSION.query(KRead).get(str(chat))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()



