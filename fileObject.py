obj = 1

class DocumentData:
    Legislação = obj
    Número = obj
    Modalidade = obj
    Tipo = obj
    Objeto = obj
    Abertura = obj
    Publicação = obj
    Município = obj
    Órgão = obj
    Situação = obj
    Referência = obj
    Adjudicado = obj
    Dados = {}
    pass

    def __dict__(self):
        return {
            "legislacao": 1,
            "numero":,
            "modalidade":,
            "tipo",
            "objeto",
            "abertura"
            "publicacao": date(Y-m-d), #formato americano
            "municipio",
            "orgao",
            "situacao",
            "referencia",
            "adjuticado"
            ...
            "content": { 
                "dados": {
                    "municipio":
                    "orgao":
                    "n_processo":
                    ...
                    "objeto":,
                    "referencia":,
                    "adjudicado":
                }
                "documentos": [
                {
                    "tipo",
                    "documento":
                    "cadastrado_em":
                }
                ]
                "publicidade" [{
                    "meio":
                    "especificacao": 
                    "data": 
                }]
            }
        }
    # Detalhe: obj
