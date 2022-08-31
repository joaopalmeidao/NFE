import os
import xml.etree.ElementTree as Et
from datetime import date

class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory) 
        if arq.lower().endswith(".xml")]

    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace(".",",")
            except:
                return var.text

    def format_cnpj(self,cnpj):
        try:
            cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
            return cnpj
    
        except:
            return ""

    def format_codbarras(self,codbarras):
        if codbarras == "SEM GTIN":
            return ""
        else:
            return codbarras

    def fornecedor_data(self,xml):
        fornecedores = []
        root = Et.parse(xml).getroot()
        nsNFe = {"ns":"http://www.portalfiscal.inf.br/nfe"}
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNFe))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFe))
        nome_fantasia = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xFant", nsNFe))
        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        # endereco 
        rua = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xLgr", nsNFe))
        nro = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:nro", nsNFe))
        xBairro = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xBairro", nsNFe))
        xMun = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:xMun", nsNFe))
        uf = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:UF", nsNFe))
        cep = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:cep", nsNFe))
        fone = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:enderEmit/ns:fone", nsNFe))
        ie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:IE", nsNFe))
        dados = [
            cnpj_emitente,#0
            nome_emitente,#1
            nome_fantasia,#2
            rua,#3
            nro,#4
            xBairro,#5
            xMun,#6
            uf,#7
            cep,#8
            fone,#9
            ie#10
        ]
        fornecedores.append(dados)
        return fornecedores

    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNFe = {"ns":"http://www.portalfiscal.inf.br/nfe"}

        #dados da NFE
        NFe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFe))
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNFe))
        data_emissao = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNFe))
        data_emissao = F"{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[:4]}"
        
        #dados emitente
        chave = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNFe))
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNFe))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFe))
        nome_fantasia = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xFant", nsNFe))

        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valorNfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNFe))
        data_importacao = date.today()
        data_importacao = data_importacao.strftime("%d/%m/%Y")
        data_saida = ""
        user = ""
        
        itemNota = 1
        notas = []

        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):

            #dados item
            cProd = self.check_none(item.find(".ns:prod/ns:cProd", nsNFe))
            cEAN = self.check_none(item.find(".ns:prod/ns:cEAN", nsNFe))
            cEAN = self.format_codbarras(cEAN)
            xProd = self.check_none(item.find(".ns:prod/ns:xProd", nsNFe))
            ncm = self.check_none(item.find(".ns:prod/ns:NCM", nsNFe))
            cest = self.check_none(item.find(".ns:prod/ns:CEST", nsNFe))
            cfop = self.check_none(item.find(".ns:prod/ns:CFOP", nsNFe))
            uCom = self.check_none(item.find(".ns:prod/ns:uCom", nsNFe))
            qCom = self.check_none(item.find(".ns:prod/ns:qCom", nsNFe))
            vUnCom = self.check_none(item.find(".ns:prod/ns:vUnCom", nsNFe))
            vProd = self.check_none(item.find(".ns:prod/ns:vProd", nsNFe))
            cEANTrib = self.check_none(item.find(".ns:prod/ns:cEANTrib", nsNFe))
            cEANTrib = self.format_codbarras(cEANTrib)
            uTrib = self.check_none(item.find(".ns:prod/ns:uTrib", nsNFe))
            qTrib = self.check_none(item.find(".ns:prod/ns:qTrib", nsNFe))         
            vUnTrib = self.check_none(item.find(".ns:prod/ns:vUnTrib", nsNFe))
            vOutro = self.check_none(item.find(".ns:prod/ns:vOutro", nsNFe))
            indTot = self.check_none(item.find(".ns:prod/ns:indTot", nsNFe))
            xPed = self.check_none(item.find(".ns:prod/ns:xPed", nsNFe))
            # imposto 
            vTotTrib = self.check_none(item.find(".ns:imposto/ns:vTotTrib", nsNFe))
            #icms
            cstIcms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS/ns:ICMS10/ns:CST", nsNFe))
            vicms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS/ns:ICMS10/ns:vICMS", nsNFe))
            # ipi
            cstIpi = self.check_none(item.find(".ns:imposto/ns:IPI/ns:IPITrib/ns:CST", nsNFe))
            vipi = self.check_none(item.find(".ns:imposto/ns:IPI/ns:IPITrib/ns:vIPI", nsNFe))

            dados = [
                NFe, #0
                serie, #1
                data_emissao, #2
                chave,#3
                cnpj_emitente,#4
                nome_emitente,#5
                nome_fantasia,#6
                valorNfe, #7
                itemNota, #8
                cProd,#9
                cEAN,#10
                xProd,#11
                ncm,#12
                cest,#13
                cfop,#14
                uCom,#15
                qCom,#16
                vUnCom,#17
                vProd,#18
                cEANTrib,#19
                uTrib,#20
                qTrib,#21
                vUnTrib,#22
                vOutro,#23
                indTot,#24
                xPed,#25
                vTotTrib,#26
                cstIcms,#27
                vicms,#28
                cstIpi,#29
                vipi,#30
                data_saida,#31
                user#32
                ]    

            notas.append(dados)
            itemNota += 1
        return notas



if __name__=="__main__":

    folder = r"xml entradas\\"
    xml = Read_xml(folder)
    all = xml.all_files()

    for i in all:
        result = xml.nfe_data(i)
        print(result)