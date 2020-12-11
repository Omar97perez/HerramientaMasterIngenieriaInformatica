#-*- coding: utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd

class File:
    def __init__(self, file, fichero):
        self.file = file
        self.fichero = fichero

class Csv(File):
  def collect(self):
        return pd.read_csv(self.file)

class Json(File):
  def collect(self):
    df = pd.read_json(self.file)
    df.to_csv(self.fichero, encoding='utf-8', index=False)
    return pd.read_csv(self.fichero)

class Xlsx(File):
  def collect(self):
    df = pd.read_excel(self.file, index_col=0)  
    df.to_csv(self.fichero, encoding='utf-8', index=False)
    return pd.read_csv(self.fichero)