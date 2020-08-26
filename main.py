#main.py에서 calculation.py 정의한 함수 불러오기

# -*- coding: utf-8 -*-

from Arithmetic import plus as pl
from Arithmetic import subtract as sub
from dataprocessing import processing
from dataprocessing import importData

a = 3
b = 4

def main():
  print("~~ 사칙 연산을 시작합니다 ~~ ")
  print("a + b =", sub.minus(a, b))
  print("a - b =", pl.add(a, b))
  print("~~ 사칙 연산을 종료합니다 ~~ ")

  ## 데이터 전처리 시작
  data = importData.readData()
  processing.process_data(data)

if __name__ == "__main__":
  main()