<<<<<<< HEAD
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
=======
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
>>>>>>> 1dd51f0b6274b73d1e89e4fd1eaf8c5ff42a6ebf
STATICFILES_DIRS = [BASE_DIR / 'game/static']