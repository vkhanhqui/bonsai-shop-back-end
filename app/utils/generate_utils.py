
from ksuid import Ksuid
from datetime import datetime


def generate_ksuid() -> str:
    kid = str(Ksuid(datetime.now()))
    return kid
