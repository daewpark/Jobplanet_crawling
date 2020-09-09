# 기본 라이브러리 호출
import pandas as pd
import numpy as np
import sqlite3

# sqlite3 db 만들기
with sqlite3.connect ('jobplanet.db') as conn :
    cursor = conn.cursor()


# 웹크롤링을 위한 준비
