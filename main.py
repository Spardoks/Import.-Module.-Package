from datetime import datetime


from art import tprint


from application.salary import calculate_salarys
from application.db.people import get_employees


if __name__ == '__main__':
    tprint("UTC")
    tprint(str(datetime.utcnow().time()))
    tprint(str(datetime.utcnow().date()))
    calculate_salarys()
    get_employees()
