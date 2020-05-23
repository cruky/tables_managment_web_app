DROP TABLE IF EXISTS "assets";


CREATE TABLE "assets" (
    "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
    "source_id"	TEXT,
    "type"	TEXT,
    "latitude"	REAL,
    "longitude"	REAL,
    "owner" TEXT,
    "date" TEXT,
);
