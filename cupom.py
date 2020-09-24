# coding: utf-8

def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):
    # Implemente aqui
    if (nome_loja == "" or nome_loja == None):
        raise Exception("O campo nome da loja é obrigatório")
    if (logradouro == "" or logradouro == None):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (numero == 0):
        numero = "s/n"
    if (municipio == "" or municipio == None):
        raise Exception("O campo município do endereço é obrigatório")
    if (estado == "" or estado == None):
        raise Exception("O campo estado do endereço é obrigatório")
    if (cnpj == "" or cnpj == None):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (inscricao_estadual == "" or inscricao_estadual == None):
        raise Exception("O campo inscrição estadual da loja é obrigatório")
        
    _COMPLEMENTO = ""
    if (complemento != "" and complemento != None):
        _COMPLEMENTO = " " + complemento


    _BAIRRO = ""
    if (bairro != "" and bairro != None) :
        _BAIRRO = bairro + " - "


    _CEP = ""
    _TELEFONE = ""

    if (cep != "" and cep != None) :
        _CEP = "CEP:" + cep
        if (telefone != "" and telefone != None):
            _TELEFONE = " Tel " + telefone
    else :
        _CEP = ""
        if (telefone != "" and telefone != None):
            _TELEFONE = "Tel " + telefone

    _OBSERVACAO = ""

    if(observacao != "" and observacao != None):
        _OBSERVACAO = observacao


    _NUMERO = ""
    if (numero != 0):
        _NUMERO = numero


    if (numero == 0):
        _NUMERO = "s/n"



    show = f'''{nome_loja}
{logradouro}, {_NUMERO}{_COMPLEMENTO}
{_BAIRRO}{municipio} - {estado}
{_CEP}{_TELEFONE}
{_OBSERVACAO}
CNPJ: {cnpj}
IE: {inscricao_estadual}'''
    return show
