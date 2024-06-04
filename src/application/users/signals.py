from datetime import datetime

from sqlalchemy import event
from sqlalchemy.orm import Session


def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()


# Attach the event listener to all subclasses of Base
@event.listens_for(Session, "before_flush")
def before_flush(session, flush_context, instances):
    for instance in session.dirty:
        if hasattr(instance, "updated_at"):
            set_updated_at(None, None, instance)
