import os
import sys
from pyArango import Connection

USER = os.environ.get("USER")
PASS = os.environ.get("PASS")

DATA_TYPE = sys.argv[1]
DATA_SOURCE = sys.argv[2]

