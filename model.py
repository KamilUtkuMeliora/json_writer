from sqlalchemy import Boolean, Float, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Sinif(Base):
    __tablename__="siniflar"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ders = relationship("Ders",back_populates="sinif")

class Ders(Base):
    __tablename__="dersler"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sinif_id =  Column(Integer, ForeignKey("siniflar.id"))

    sinif = relationship("Sinif", back_populates="ders")
    unite = relationship("Unite", back_populates="ders")

class Unite(Base):
    __tablename__="uniteler"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sinif_id =  Column(Integer, ForeignKey("dersler.id"))

    ders = relationship("Ders", back_populates="unite")
    konu = relationship("Konu", back_populates="unite")

class Konu(Base):
    __tablename__="konular"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sinif_id =  Column(Integer, ForeignKey("uniteler.id"))

    unite = relationship("Unite", back_populates="konu")
    altkonu = relationship("Altkonu", back_populates="konu")

class Altkonu(Base):
    __tablename__="altkonular"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sinif_id =  Column(Integer, ForeignKey("konular.id"))

    konu = relationship("Konu", back_populates="altkonu")
    altaltkonu = relationship("Altaltkonu", back_populates="altkonu")

class Altaltkonu(Base):
    __tablename__="altaltkonular"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sinif_id =  Column(Integer, ForeignKey("altkonular.id"))
    altkonu = relationship("Altkonu", back_populates="altaltkonu")

class BruteQuestion(Base):
  __tablename__ = "BRUTE_QUESTION"

  id = Column(Integer, primary_key=True, index=True)
  soru = Column(String)
  cevap1 = Column(String)
  cevap2 = Column(String)
  cevap3 = Column(String)
  cevap4 = Column(String)
  sinif = Column(String)
  ders = Column(String)
  unite = Column(String)
  konu  = Column(String)
  kazanim = Column(String, nullable=True)
  alt_kazanim = Column(String, nullable=True)
  dogru_yapilma_sayisi = Column(Float)
  toplam_yapilma_sayisi = Column(Float)
  zorluk = Column(Integer)
  def __str__(self):
      return self.soru
