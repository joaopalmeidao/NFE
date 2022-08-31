from .readxml import Read_xml
from .database import *

def nfeData():

    xml = Read_xml(r'NFe\\XML Entrada\\')
    all = xml.all_files()
    for i in all:
        forn_xml = xml.fornecedor_data(i)
        forn_xml = forn_xml[0]
        try:
            cursor.execute(
                        f"""
                        INSERT INTO fornecedores VALUES(
                        '{forn_xml[0]}',
                        '{forn_xml[1]}',
                        '{forn_xml[2]}',
                        '{forn_xml[3]}',
                        '{forn_xml[4]}',
                        '{forn_xml[5]}',
                        '{forn_xml[6]}',
                        '{forn_xml[7]}',
                        '{forn_xml[8]}',
                        '{forn_xml[9]}',
                        '{forn_xml[10]}'
                        )
                        """
                    )
            db.commit()
        except:
            pass
        nota_xml = xml.nfe_data(i)
        for n in nota_xml:
            uTrib = n[20]
            vUnTrib = n[22]
            vUnCom = n[17]
            qCom = n[16]
            qCom = qCom.split(",")
            qCom = qCom[0]
            ucom = n[15]
            xProd = n[11]
            vUnCom = vUnCom.replace(",",".")
            vUnTrib = vUnTrib.replace(",",".")

            if "FARDO" in uTrib:
                print("FARDO")
                if "x1" in xProd:
                    qt = xProd.find("x")
                    qt = xProd[(qt-2):qt]
                    qt = qt.replace(" ","")
         
                    vUnTrib = float(vUnTrib) / int(qt)
                    

                    
                elif "X1" in xProd:
                    qt = xProd.find("X")
                    qt = xProd[(qt-2):qt]
                    qt = qt.replace(" ","")
                    

                    vUnTrib = float(vUnTrib) / int(qt)
                
                qCom = int(qCom)*int(qt)
                    
                    
            print(f"{xProd}, {int(qCom)}, {float(vUnTrib):.2f}")
            

                    
            notassql = f"""
            '{n[0]}',
            '{n[1]}',
            '{n[2]}',
            '{n[3]}',
            '{n[4]}',
            '{n[5]}',
            '{n[6]}',
            '{n[7]}',
            '{n[8]}',
            '{n[9]}',
            '{n[10]}',
            '{n[11]}',
            '{n[12]}',
            '{n[13]}',
            '{n[14]}',
            '{n[15]}',
            '{n[16]}',
            '{n[17]}',
            '{n[18]}',
            '{n[19]}',
            '{n[20]}',
            '{n[21]}',
            '{n[22]}',
            '{n[23]}',
            '{n[24]}',
            '{n[25]}',
            '{n[26]}',
            '{n[27]}',
            '{n[28]}',
            '{n[29]}',
            '{n[30]}',
            '{n[31]}',
            '{n[32]}'            
            """
            if save_nfse_db == True:
                try:
                    cursor.execute(
                        f"""
                        INSERT INTO xml_entrada VALUES(
                        {notassql}
                        )
                        """
                    )
                    db.commit()
                except:
                    pass
            else:
                pass
            try:
                cursor.execute(
                    f"""
                    INSERT INTO cad_produtos VALUES(
                    {notassql}
                    )
                    """
                )
                db.commit()
            except:
                pass
            