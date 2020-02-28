# conda
import sys
!conda install --yes --prefix {sys.prefix} xgboost

# pip
import sys
!{sys.executable} -m pip install xgboost
