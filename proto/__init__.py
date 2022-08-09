import sys
from pathlib import Path
# grpcのツールが__init__.pyを吐いてくれないので、自前で実装。
sys.path.append(str(Path(__file__).parent))