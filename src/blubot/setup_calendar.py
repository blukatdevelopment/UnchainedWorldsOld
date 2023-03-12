# Run this to set up in-world calendar data
import sys
sys.path.append('./uw/')
from database import Db
from uw.world import populate_calendar

def main():
    db = Db()
    populate_calendar(db)

main()