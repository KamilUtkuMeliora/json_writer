import model
from database import engine, SessionLocal
import json

json_bilgi= {"wrong_counter": 0, "genel": 3, "ozel": {}}
model.Base.metadata.create_all(bind=engine)
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() 
db = SessionLocal() 

print("================================Siniflar[0/7]==============================================")
input_list = db.query(model.Sinif).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    json_bilgi["ozel"][isim.name] = 5.3
print("================================Siniflar[1/7]==============================================")

print("================================Dersler[1/7]==============================================")
input_list = db.query(model.Ders).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    parent = db.query(model.Sinif).filter(isim.sinif_id == model.Sinif.id).first().name
    if type(json_bilgi["ozel"][parent]) == float:
        json_bilgi["ozel"][parent] = {}
    json_bilgi["ozel"][parent][isim.name] = 5.3
print("================================Dersler[2/7]==============================================")

print("================================Unite[2/7]==============================================")
input_list = db.query(model.Unite).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    ders = db.query(model.Ders).filter(isim.sinif_id == model.Ders.id).first()
    sinif = db.query(model.Sinif).filter(ders.sinif_id == model.Sinif.id).first()
    if type(json_bilgi["ozel"][sinif.name][ders.name]) == float:
        json_bilgi["ozel"][sinif.name][ders.name] = {}
    json_bilgi["ozel"][sinif.name][ders.name][isim.name] = 5.3
print("================================Unite[3/7]==============================================")

print("================================Konu[3/7]==============================================")
input_list = db.query(model.Konu).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    unite = db.query(model.Unite).filter(isim.sinif_id == model.Unite.id).first()
    ders = db.query(model.Ders).filter(unite.sinif_id == model.Ders.id).first()
    sinif = db.query(model.Sinif).filter(ders.sinif_id == model.Sinif.id).first()
    if type(json_bilgi["ozel"][sinif.name][ders.name][unite.name]) == float:
        json_bilgi["ozel"][sinif.name][ders.name][unite.name] = {}
    json_bilgi["ozel"][sinif.name][ders.name][unite.name][isim.name] = 5.3
print("================================Konu[4/7]==============================================")

print("================================Kazanim[4/7]==============================================")
input_list = db.query(model.Altkonu).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    konu = db.query(model.Konu).filter(isim.sinif_id == model.Konu.id).first()
    unite = db.query(model.Unite).filter(konu.sinif_id == model.Unite.id).first()
    ders = db.query(model.Ders).filter(unite.sinif_id == model.Ders.id).first()
    sinif = db.query(model.Sinif).filter(ders.sinif_id == model.Sinif.id).first()
    if type(json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name]) == float:
        json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name] = {}
    json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name][isim.name] = 5.3
print("================================Kazanim[5/7]==============================================")

print("================================Kazanim[6/7]==============================================")
input_list = db.query(model.Altaltkonu).all()
for i, isim in enumerate(input_list):
    print("{}/{}".format(i+1,len(input_list)))
    kazanim = db.query(model.Altkonu).filter(isim.sinif_id == model.Altkonu.id).first()
    konu = db.query(model.Konu).filter(kazanim.sinif_id == model.Konu.id).first()
    unite = db.query(model.Unite).filter(konu.sinif_id == model.Unite.id).first()
    ders = db.query(model.Ders).filter(unite.sinif_id == model.Ders.id).first()
    sinif = db.query(model.Sinif).filter(ders.sinif_id == model.Sinif.id).first()
    if type(json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name][kazanim.name]) == float:
        json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name][kazanim.name] = {}
    json_bilgi["ozel"][sinif.name][ders.name][unite.name][konu.name][kazanim.name][isim.name] = 5.3
print("================================Kazanim[7/7]==============================================")

print(json_bilgi["ozel"])
# Serializing json
json_object = json.dumps(json_bilgi, indent=4)
 
# Writing to sample.json
with open("kamilutkumavi0.json", "w") as outfile:
    outfile.write(json_object)
