show dbs
use ds_open_subwayPassengersDb
show collections
db.db_open_subwayTable.find()
db.db_open_subwayTable.find_one({"CardSubwayTime.row.SUB_STA_NM": "서울역"})
