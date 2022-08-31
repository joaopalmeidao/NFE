import sqlite3

db = sqlite3.connect("DataBase.db")
cursor = db.cursor()

save_nfse_db = True

# cursor.execute(
# """
# CREATE TABLE "xml_entrada" (
# 	"NFe"	TEXT,
# 	"serie"	TEXT,
# 	"data_emissao"	TEXT,
# 	"chave"	TEXT,
# 	"cnpj_emitente"	TEXT,
# 	"nome_emitente"	TEXT,
# 	"nome_fantasia"	TEXT,
# 	"valorNfe"	TEXT,
# 	"itemNota"	INTEGER,
# 	"cProd"	TEXT,
# 	"cEAN"	TEXT,
# 	"xProd"	TEXT,
# 	"ncm"	TEXT,
# 	"cest"	TEXT,
# 	"cfop"	TEXT,
# 	"ucom"	TEXT,
#     "qCom"  TEXT,
# 	"vUnCom"	NUMERIC,
# 	"vProd"	NUMERIC,
# 	"cEANTrib"	TEXT,
# 	"uTrib"	TEXT,
# 	"qTrib"	NUMERIC,
# 	"vUnTrib"	NUMERIC,
# 	"vOutro"	TEXT,
# 	"indTot"	TEXT,
# 	"xPed"	TEXT,
# 	"vTotTrib"	NUMERIC,
# 	"cstIcms"	TEXT,
# 	"vicms"	TEXT,
# 	"cstIpi"	NUMERIC,
# 	"vipi"	TEXT,
# 	"data_saida"	TEXT,
# 	"user"	TEXT
# )
# """
# )
# db.commit()

# cursor.execute(
# """
# CREATE TABLE "cad_produtos" (
# 	"NFe"	TEXT,
# 	"serie"	TEXT,
# 	"data_emissao"	TEXT,
# 	"chave"	TEXT,
# 	"cnpj_emitente"	TEXT,
# 	"nome_emitente"	TEXT,
# 	"nome_fantasia"	TEXT,
# 	"valorNfe"	TEXT,
# 	"itemNota"	INTEGER,
# 	"cProd"	TEXT,
# 	"cEAN"	TEXT,
# 	"xProd"	TEXT,
# 	"ncm"	TEXT,
# 	"cest"	TEXT,
# 	"cfop"	TEXT,
# 	"ucom"	TEXT,
#     "qCom"  TEXT,
# 	"vUnCom"	NUMERIC,
# 	"vProd"	NUMERIC,
# 	"cEANTrib"	TEXT,
# 	"uTrib"	TEXT,
# 	"qTrib"	NUMERIC,
# 	"vUnTrib"	NUMERIC,
# 	"vOutro"	TEXT,
# 	"indTot"	TEXT,
# 	"xPed"	TEXT,
# 	"vTotTrib"	NUMERIC,
# 	"cstIcms"	TEXT,
# 	"vicms"	TEXT,
# 	"cstIpi"	NUMERIC,
# 	"vipi"	TEXT,
# 	"data_saida"	TEXT,
# 	"user"	TEXT
# )
# """
# )
# db.commit()