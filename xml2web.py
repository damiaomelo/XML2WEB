#!/usr/bin/python
# coding: UTF-8
'''****************************************************************************
*                  __author__ = "Levindo Gabriel Taschetto Neto"              *
*                  __email__ = "falecom@levindoneto.com"                      *
*                  __status__ = "Em produção"                                 *
*****************************************************************************'''
import xml.dom.minidom

# Abrindo o arquivo:
xmldoc = xml.dom.minidom.parse('curriculo.xml')

# Salvando em 'dados' tudo que tem a tag que esta' dentro de ("..."):
dados = xmldoc.getElementsByTagName("DADOS-GERAIS")

###############################################################################
'''             Lendo e-mail do usuario e fazendo a manipulação             '''
'''                  Para ter o emailname e o emailserver                   '''
# Rebendo e-mail do usuário via teclado
email = raw_input("Insira seu e-mail: ")

emailname = ""                 # Inicializando emailname
emailserver = ""               # Inicializando emailserver

for z in email:  
    if(z == '@'):
        break
    else:
        emailname += z      # Montando string do emailname  

aux_email = email
aux_email =  aux_email.replace(emailname + '@', "")    
emailserver = aux_email
###############################################################################

###############################################################################
'''       Função que cria uma configuação inicial para o HTML criado        '''
def criaHTML(variavel):
    # Trabalhando em cima do arquivo:
    variavel.write("<!DOCTYPE html>\n <html>\n\t<head>\n"                                      )
    variavel.write("\t\t<meta charset ='UTF-8'/> <!--Formatação para acentos e cedilha-->\n"   )
    variavel.write("\t\t<title>Página Modelo - XML2WEB Project</title>\n"                      )
    variavel.write("\t\t<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n" )
    variavel.write("\t\t<style type='text/css'>\n"                                             )
    variavel.write("\t\t</style>\n"                                                            )
    variavel.write("\t</head>\n"                                                               )
    variavel.write("\t<!-- Chamando a pasta do arquivo de folha de estilo.css           -->\n" )
    variavel.write("\t<link rel = 'stylesheet' type = 'text/css' href = 'estilo.css'/>\n"      )
    variavel.write("\t<style>\n"                                                               )
    variavel.write("\tbody\n\t{\n\t\tbackground-color: white;\n\t}\n"                          )
    variavel.write("\t</style>\n<body>\n"                                                      )
###############################################################################

###############################################################################
'''    Função que cria um cabeça para o HTML criado (utilizado nas abas)    '''
def criaHeader(variavel2):
    variavel2.write("<!DOCTYPE html>\n <html>\n\t<head>\n"                                     )
    variavel2.write("\t\t<meta charset ='UTF-8'/> <!--Formatação para acentos e cedilha-->\n"  )
    variavel2.write("\t\t<title>Página Modelo - XML2WEB Project</title>\n"                     )
    variavel2.write("\t\t<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n")
    variavel2.write("\t\t<style type='text/css'>\n"                                            )     
    variavel2.write("\t\t</style>\n"                                                           )
    variavel2.write("\t</head>\n"                                                              )
    variavel2.write("\t<!-- Chamando a pasta do arquivo de folha de estilo.css           -->\n")
    variavel2.write("\t<link rel = 'stylesheet' type = 'text/css' href = 'estilo.css'/>\n\n"   )
    variavel2.write("\t<div id='interface'>\n"                                                 )
    variavel2.write("\t\t<body>\n"                                                             )
    variavel2.write("\t\t\t<!-- Nome do professor vai aqui                           -->\n"    )
    variavel2.write("\t\t\t<header id='cabecalho'>\n"                                          )
    variavel2.write("\t\t\t\t<hgroup>                    <!--Títulos do mesmo grupo-->\n"      )
    variavel2.write("\t\t\t<!-- Iframe para o nome -->\n"                                      )
    variavel2.write("\t\t\t<iframe src='nome.html'   name='n_nome' id='nome'>     </iframe>\n" )
    variavel2.write("\t\t\t\t</hgroup>\n"                                                      )
    variavel2.write("\t\t\t</header>\n"                                                        )
    variavel2.write("\t\t\t<header id='menu_cabecalho'>\n"                                     )
    variavel2.write("\t\t\t<nav id='menu'>\n"                                                  )
    variavel2.write("\t\t\t\t<h1> Menu Principal </h1>\n"                                      )
    variavel2.write("\t\t\t\t<ul type='disc'>\n"                                               )
    variavel2.write("\t\t\t\t<li> <a href='index.html'>Página Inicial</a></li>\n"              )
    variavel2.write("\t\t\t\t<li> <a href='publicacoes.html'>Publicações</a></li>\n"           )
    variavel2.write("\t\t\t\t<li> <a href='orientacoes.html'>Orientações</a></li>\n"           )    
    variavel2.write("\t\t\t\t<li> <a href='pesquisa.html'>Pesquisa</a></li>\n"                 )
    variavel2.write("\t\t\t\t<li> <a href='contato.html'>Contato</a></li>\n"                   )
    variavel2.write("\t\t\t</nav>\n"                                                           )
    variavel2.write("\t\t</header>\n"                                                          )
###############################################################################
    
###############################################################################
'''    Função que cria um rodapé para o HTML criado (utilizado nas abas)    '''
def criaFooter(variavel3):
    variavel3.write('\n\t<footer id="rodape"\n'                                                )
    variavel3.write('\t\t <><a class="menu_rodape" href="">Página Inicial            </a>\n'   )
    variavel3.write('\t\t <a class="menu_rodape" href="publicacoes.html">Publicações </a>\n'   )
    variavel3.write('\t\t <a class="menu_rodape" href="pesquisa.html">Pesquisa       </a>\n'   )
    variavel3.write('\t\t <a class="menu_rodape" href="contato.html">Contato         </a>\n'   )
    variavel3.write("\t</footer>                   <!--Aqui termina o rodapé da página-->\n"   )
    #Fechamento do documento html (daí é padrão só em abas, não em iframes)
    variavel3.write("</body>\n</html>"                                                         )
###############################################################################

###############################################################################
def bigSpace(variavel4):
    variavel4.write("<br/><br/><br/><br/><br/><br/><br/><br/>")
###############################################################################

###############################################################################
'''                             Nome do usuário                             '''
nome = open("nome.html", "w")              # Abrindo/criando o arquivo no modo escrita
criaHTML(nome)                             # Configurações iniciais do HTML
nome.write("<h1>\n")
#-> Nome
for n in dados:
    #print(n.toxml())                      # Para imprimir tudo que tem dentro da tag<> </>
    nomeUser = n.attributes["NOME-COMPLETO"].value # Para imprimir o que tem dentro dos IDs
nomeUser = nomeUser.encode('utf-8')        # Ajuste de codificação
nome.write(str(nomeUser))                  # write só trabalha com strings
nome.write(" \n</h1>\n")

nome.write("</body>\n</html>")
nome.close() # Fechando o arquivo
###############################################################################

###############################################################################
'''                        Descrição do usuário                             '''
descricao = open("descricao.html", "w")    # Abrindo/criando o arquivo no modo escrita
criaHTML(descricao)                        # Configurações iniciais do HTML
descricao.write("<p id=descricao_user>\n")
 
#-> Pegando do XML a descrição em português do usuário:
descricaoPT = xmldoc.getElementsByTagName("RESUMO-CV")
for d in descricaoPT:
    desc = d.attributes["TEXTO-RESUMO-CV-RH"].value

#print desc
desc = desc.encode('utf-8')                # Ajuste de codificação

descricao.write(str(desc))                 # write so trabalha com strings
descricao.write(" \n</p>\n")


descricao.write("</body>\n</html>")
descricao.close()                          # Fechando o arquivo
###############################################################################

###############################################################################
'''                       Publicações do usuário                            '''
###############################################################################
'''                           Aba 'PUBLICAÇÕES'                             '''
publics = open("publicacoes.html", "w")    # Abrindo/criando o arquivo no modo escrita
criaHeader(publics)

publics.write("<h3>\n\tArtigos completos publicados em periódicos\n</h3>\n")
publics.write("<!-- Iframe para os periódicos -->\n")
publics.write("\t\t\t<iframe src='periodicos.html'   name='a_periodicos' id='periodicos'>     </iframe>\n")

publics.write("<h3>\n\tTrabalhos completos publicados em anais e congressos\n</h3>\n")
publics.write("<!-- Iframe para as publicaçoes em anais e congressos -->\n")
publics.write("\t\t\t<iframe src='trab_anais.html'   name='t_anais' id='anais'>     </iframe>\n")

publics.write("<h3>\n\tResumos expandidos publicados em anais de congressos\n</h3>\n")
publics.write("<!-- Iframe para os periódicos -->\n")
publics.write("\t\t\t<iframe src='periodicos.html'   name='a_periodicos' id='periodicos'>     </iframe>\n")

publics.write("<h3>\n\tResumos publicados em anais de congressos\n</h3>\n")
publics.write("<!-- Iframe para os periódicos -->\n")
publics.write("\t\t\t<iframe src='periodicos.html'   name='a_periodicos' id='periodicos'>     </iframe>\n")

publics.write("<h3>\n\tArtigos aceitos para publicação\n</h3>\n")
publics.write("<!-- Iframe para os periódicos -->\n")
publics.write("\t\t\t<iframe src='periodicos.html'   name='a_periodicos' id='periodicos'>     </iframe>\n")

publics.write("<h3>\n\tOutras produções bibliográficas\n</h3>\n")
publics.write("<!-- Iframe para os periódicos -->\n")
publics.write("\t\t\t<iframe src='periodicos.html'   name='a_periodicos' id='periodicos'>     </iframe>\n")





'''            >>> ARTIGOS EM PERIODICOS  <<< 
artigos = xmldoc.getElementsByTagName("DADOS-BASICOS-DO-ARTIGO")
dicionario_de_artigos = {}                 # Inicializando lista de artigos
contadorArtigos = 1                        # Contador de artigos

publics.write("<br/>")

for a in artigos:
    # Dados para o dicionário(Título e Ano de cada artigo)
    # Cada nome de artigo tambem ficará na formatação UTF-8    
    titulo_do_artigo = (a.attributes["TITULO-DO-ARTIGO"].value).encode('utf-8')
    ano_do_artigo = a.attributes["ANO-DO-ARTIGO"].value

    link_do_artigo = a.attributes["HOME-PAGE-DO-TRABALHO"].value
    
    link_do_artigo = str(link_do_artigo)    
    
    link_do_artigo =  link_do_artigo.replace("doi:", "http://dx.doi.org/")
    #Removendo '[' e ']'   
    link_do_artigo =  link_do_artigo.replace("[", "")    
    link_do_artigo =  link_do_artigo.replace("]", "")
    
    # Armazenando no formato de tupla: "titulo_do_artigo":"ano_do_artigo"
    dicionario_de_artigos.update({str(titulo_do_artigo):str(ano_do_artigo)})
    # Formato: Nome do Artigo (ANO)
    
    publics.write('<a target="blank" ')
    publics.write("href='" + str(link_do_artigo)  + "'")    
    
    publics.write(' > ' + str(titulo_do_artigo) + ' (' + str(ano_do_artigo) + ') ')
    publics.write('</a> <br/>\n')    
    
    #publics.write("\n<br/>\n")            # Quebra de linha  
    contadorArtigos += 1
    #lista.sort()                          # Para ordenar a lista (list(dicionario_de_artigos))
                                           # Ordenação pode ser feita pelo keys.sort tambem

autores = xmldoc.getElementsByTagName("AUTORES")

for au in autores:
        autor = au.attributes["NOME-PARA-CITACAO"].value
        print autor
        print "********************"
'''


bigSpace(publics)
criaFooter(publics)
publics.write(" \n</p>\n")
publics.close()                             # Fechando o arquivo
###############################################################################

###############################################################################
'''                  Publicações de destaque do usuário                     '''
# Artigos (Destaque -> FLAG-RELEVANCIA="SIM")

relevantes = open("relevantes.html", "w")    # Abrindo/criando o arquivo no modo escrita
criaHTML(relevantes)                         # Configurações iniciais do HTML

artigosDestaque = xmldoc.getElementsByTagName("DADOS-BASICOS-DO-ARTIGO")
artigos_com_destaque = {}                    # Inicializando dicionário de artigos com destaque
flagImprimirDestaques = 0                    # Flag para ver se tem algum destaque nos artigos para ser impresso
contadorArtigosR = 1                         # Contador de artigos

for j in artigosDestaque:
    link_do_artigoR = j.attributes["HOME-PAGE-DO-TRABALHO"].value
    
    link_do_artigoR = str(link_do_artigoR)    
    
    link_do_artigoR =  link_do_artigoR.replace("doi:", "http://dx.doi.org/")
    #Removendo '[' e ']'   
    link_do_artigoR =  link_do_artigoR.replace("[", "")    
    link_do_artigoR =  link_do_artigoR.replace("]", "")    

     
    flagRelevancia = j.attributes["FLAG-RELEVANCIA"].value
    titulo_do_artigoR = j.attributes["TITULO-DO-ARTIGO"].value
    ano_do_artigoR = j.attributes["ANO-DO-ARTIGO"].value

    #print(flagRelevancia)

    if flagRelevancia == "SIM":
        relevantes.write('<a target="blank" ')
        relevantes.write("href='" + link_do_artigoR  + "'")    
    
        relevantes.write(' > ' + str(titulo_do_artigoR) + ' (' + str(ano_do_artigoR) + ') ')
        relevantes.write('</a> <br/>\n')          
        
        #relevantes.write("\n<br/>\n")             # Quebra de linha  
        contadorArtigosR += 1
        flagImprimirDestaques = 1           # Usado para testes
    else:
        flagImprimirDestaques = 0

###############################################################################
'''                          Endereço do usuário                            '''
endereco = open("endereco.html", "w")           # Abrindo/criando o arquivo no modo escrita
criaHTML(endereco)                              # Configurações iniciais do HTML
endereco.write("<p>\n")   

'''            Buscando dados de endereço no arquivo .xml        '''
contato = xmldoc.getElementsByTagName("ENDERECO-PROFISSIONAL")
for c in contato:
    # Nome da instituição:
    instituicao = c.attributes["NOME-INSTITUICAO-EMPRESA"].value

    # Instituto:
    instituto = c.attributes["NOME-ORGAO"].value

    # Departamento:
    departamento = c.attributes["NOME-UNIDADE"].value

    # Localização:
    local = c.attributes["LOGRADOURO-COMPLEMENTO"].value

    # Bairro:
    bairro = c.attributes["BAIRRO"].value

    # CEP:
    cep = c.attributes["CEP"].value

    # Cidade:
    cidade = c.attributes["CIDADE"].value

    # Estado:
    estado = c.attributes["UF"].value

    # País:
    pais = c.attributes["PAIS"].value

    # Caixa Postal: 
    caixa_postal = c.attributes["CAIXA-POSTAL"].value
    
    # E-mail:
    estado = c.attributes["UF"].value
    
    '''---------------------------------------------------------------------'''

    # Telefone (Sem ramal):
    telefone = "(" + c.attributes["DDD"].value + ") " + c.attributes["TELEFONE"].value

'''            Imprimindo dados de endereço no arquivo .html        '''
#Instituição
instituicao = instituicao.encode('utf-8')           # Ajuste de codificação    
endereco.write("</p>")
endereco.write("\n")
endereco.write('<section id = "endereco_p">')       # Seção para organização do paragrafo
endereco.write("\n")
endereco.write("\t")
endereco.write(str(instituicao))
endereco.write(", ")
#Instituto
instituto = instituto.encode('utf-8')               # Ajuste de codificação
endereco.write(str(instituto))
endereco.write("\n<br/>\n")
#Departamento
departamento = departamento.encode('utf-8')         # Ajuste de codificação
endereco.write("\t")
endereco.write(str(departamento)) 
endereco.write("\n<br/>\n")                         # Quebra de linha  
#Localização
local = local.encode('utf-8')                       # Ajuste de codificação
endereco.write("\t")
endereco.write(str(local))
endereco.write("\n<br/>\n")                         # Quebra de linha
#Bairro
bairro = bairro.encode('utf-8')                     # Ajuste de codificação
endereco.write("\t")
endereco.write(str(bairro))
endereco.write("\n<br/>\n")                         # Quebra de linha
#CEP
endereco.write("\t")
endereco.write("CEP: ")
endereco.write(str(cep))
endereco.write(", ")
#Cidade
cidade = cidade.encode('utf-8')                     # Ajuste de codificação
endereco.write(str(cidade))
endereco.write(", ")

#Estado
estado = estado.encode('utf-8')                     # Ajuste de codificação
endereco.write(str(estado))
endereco.write(", ")

#País
pais = pais.encode('utf-8')                         # Ajuste de codificação
endereco.write(str(pais))
endereco.write(", ")

#Caixa postal
caixa_postal = caixa_postal.encode('utf-8')         # Ajuste de codificação
endereco.write("Caixa postal: ")
endereco.write(str(caixa_postal))
endereco.write("\n<br/>\n")

endereco.write("\n<br/>\n")
 
#Telefone com DDD
endereco.write("Telefone: ")
endereco.write(str(telefone))

endereco.write("\n<br/>\n")

#Fax com DDD
endereco.write("\n<br/>\n")
endereco.write("\n")
endereco.write("<section/>\n")

endereco.write("</body>\n</html>")
endereco.close() # Fechando o arquivo
''' 
  Formato: Universidade, Instituto, Departamento
           Localização
           Bairro
           CEP - Cidade, Estado - País - Caixa Postal: Aqui vai a caixa postal
           
           Telefone: Aqui vai o telefone (Com ddd)
'''
###############################################################################

###############################################################################
'''                            Foto do usuario                              '''
foto = open("foto.html", "w")                         # Abrindo/criando o arquivo no modo escrita
criaHTML(foto)

foto.write("<img id='foto_index' src='perfil.png' height='150' width='110'>")

foto.write("</body>\n</html>")
foto.close()                                         # Fechando o arquivo
###############################################################################

###############################################################################
'''                               Logotipos                                 '''
logos = open("logos.html", "w")                      # Abrindo/criando o arquivo no modo escrita
criaHTML(logos)

#Logo 01
logos.write("<img id='logo_01' src='logo01.gif' height='120' width='120'>")
#Logo 02
logos.write("<img id='logo_02' src='logo02.gif' height='90' width='144'>")

logos.write("</body>\n</html>")
logos.close()                                         # Fechando o arquivo
###############################################################################

###############################################################################
'''                              Aba 'CONTATO'                              '''
contato = open("contato.html", "w")                   # Abrindo/criando o arquivo no modo escrita
criaHeader(contato)

contato.write("<br\n><h3>Endereço</h3>")

contato_aba = xmldoc.getElementsByTagName("ENDERECO-PROFISSIONAL")
for v in contato_aba:
    # Nome da instituição:
    instituicao2 = v.attributes["NOME-INSTITUICAO-EMPRESA"].value

    # Instituto:
    instituto2 = v.attributes["NOME-ORGAO"].value

    # Departamento:
    departamento2 = v.attributes["NOME-UNIDADE"].value

    # Localização:
    local2 = v.attributes["LOGRADOURO-COMPLEMENTO"].value

    # Bairro:
    bairro2 = v.attributes["BAIRRO"].value

    # CEP:
    cep2 = v.attributes["CEP"].value

    # Cidade:
    cidade2 = v.attributes["CIDADE"].value

    # Estado:
    estado2 = v.attributes["UF"].value

    # País:
    pais2 = v.attributes["PAIS"].value

    # Caixa Postal: 
    caixa_postal2 = v.attributes["CAIXA-POSTAL"].value
    
    # E-mail:
    estado2 = v.attributes["UF"].value
    
    '''---------------------------------------------------------------------'''

    # Telefone (Sem ramal):
    telefone2 = "(" + v.attributes["DDD"].value + ") " + v.attributes["TELEFONE"].value

'''            Imprimindo dados de endereço no arquivo .html        '''
#Instituição
instituicao2 = instituicao2.encode('utf-8')           # Ajuste de codificação    
contato.write("</p>")
contato.write("\n")
contato.write('<section id = "contatoAba">')       # Seção para organização do paragrafo
contato.write("\n")
contato.write("\t")
contato.write(str(instituicao2))
contato.write(", ")

#Instituto
instituto2 = instituto2.encode('utf-8')            # Ajuste de codificação
contato.write(str(instituto2))
contato.write("\n<br/>\n")

#Departamento
departamento2 = departamento2.encode('utf-8')         # Ajuste de codificação
contato.write("\t")
contato.write(str(departamento2)) 
contato.write("\n<br/>\n")                         # Quebra de linha  

#Localização
local2 = local2.encode('utf-8')                       # Ajuste de codificação
contato.write("\t")
contato.write(str(local2))
contato.write("\n<br/>\n")                         # Quebra de linha

#Bairro
bairro2 = bairro2.encode('utf-8')                     # Ajuste de codificação
contato.write("\t")
contato.write(str(bairro2))
contato.write("\n<br/>\n")                         # Quebra de linha

#CEP
contato.write("\t")
contato.write("CEP: ")
contato.write(str(cep2))
contato.write(", ")

#Cidade
cidade2 = cidade2.encode('utf-8')                     # Ajuste de codificação
contato.write(str(cidade2))
contato.write(", ")

#Estado
estado2 = estado2.encode('utf-8')                     # Ajuste de codificação
contato.write(str(estado2))
contato.write(", ")

#País
pais2 = pais2.encode('utf-8')                         # Ajuste de codificação
contato.write(str(pais2))
contato.write(", ")

#Caixa postal
caixa_postal2 = caixa_postal2.encode('utf-8')         # Ajuste de codificação
contato.write("Caixa postal: ")
contato.write(str(caixa_postal2))
contato.write("\n<br/>\n")

contato.write("\n<br/>\n")
 
#Telefone com DDD
contato.write("\t")
contato.write("Telefone: ")
contato.write(str(telefone2))

contato.write("\n<br/><br/>")
contato.write("\n<h3>E-mail</h3>\n")

#Impressão do e-mail em CSS para evitar Spams
contato.write("<style>\n")
contato.write("  my-email::after {\n")
contato.write("    content: attr(data-domain);\n")
contato.write("  }\n")
contato.write("  my-email::before {\n")
contato.write("    content: attr(data-user);\n")
contato.write("  }\n")
contato.write("</style>\n")
contato.write("\n")
contato.write('\n<section id="email_contato">\n')
contato.write("<my-email data-user='" + emailname + "'" +  " data-domain= '"+ emailserver + "'>@</my-email>")
contato.write("\n</section>")
contato.write("\n<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>\n")

bigSpace(contato)
criaFooter(contato)
contato.close()                                         # Fechando o arquivo
###############################################################################

###############################################################################
'''                            Aba 'PESQUISA'                               '''
pesquisa = open("pesquisa.html", "w")                   # Abrindo/criando o arquivo no modo escrita
criaHeader(pesquisa)

pesquisa.write("<h3>\n\tProjetos de pesquisa\n</h3>\n")
pesquisa.write("<!-- Iframe para os projetos de pesquisa -->\n")
pesquisa.write("\t\t\t<iframe src='projetos_pesquisa.html'   name='proj_pesq' id='p_pesq'>     </iframe>\n")

bigSpace(pesquisa)
criaFooter(pesquisa)
pesquisa.close()                                         # Fechando o arquivo
###############################################################################

'''        Iframes para as abas pesquisa,MAS VA publicações e orientações         '''
###############################################################################
'''           Iframe - projetos_pesquisa.html ( Aba Pesquisa )              '''
projetos_pesquisa = open("projetos_pesquisa.html", "w")                   # Abrindo/criando o arquivo no modo escrita

criaHTML(projetos_pesquisa)                             # Configurações iniciais do HTML 
#-> Pegando do XML os projetos de pesquisa
projPesq = xmldoc.getElementsByTagName("PROJETO-DE-PESQUISA")
for proj in projPesq:
    nome_projeto = proj.attributes["NOME-DO-PROJETO"].value
    nome_projeto = nome_projeto.encode('utf-8')    
    desc_projeto = proj.attributes["DESCRICAO-DO-PROJETO"].value    
    desc_projeto = desc_projeto.encode('utf-8')
    ano_inicio_proj = proj.attributes["ANO-INICIO"].value
    ano_fim_proj = proj.attributes["ANO-FIM"].value
    if ano_fim_proj == "":
        ano_fim_proj = "Atual"        
    
    projetos_pesquisa.write("<p class=nome_projeto>" + str(nome_projeto) + " (" + str(ano_inicio_proj) + " - " + str(ano_fim_proj) + ")" + "</p>" + "\n")
    projetos_pesquisa.write("<p class='desc_projeto'>" + str(desc_projeto) + "</p>" + "</br>" + "\n\n")
#print desc
#desc = desc.encode('utf-8')                # Ajuste de codificação

projetos_pesquisa.write("</body>\n</html>")
projetos_pesquisa.close()    
###############################################################################

###############################################################################
'''                          Aba 'ORIENTACOES'                              '''
orientacoes = open("orientacoes.html", "w")                   # Abrindo/criando o arquivo no modo escrita
criaHeader(orientacoes)

orientacoes.write("<h3>\n\tOrientações de Doutorado\n</h3>\n")
orientacoes.write("<!-- Iframe para as orientações de doutorado -->\n")
orientacoes.write("\t\t\t<iframe src='orientacoes_doutorado.html'   name='o_dout' orient_d'>     </iframe>\n")

orientacoes.write("<h3>\n\tOrientações de Mestrado\n</h3>\n")
orientacoes.write("<!-- Iframe para as orientações de mestrado -->\n")
orientacoes.write("\t\t\t<iframe src='orientacoes_mestrado.html'   name='o_mest' id='orient_m'>     </iframe>\n")

orientacoes.write("<h3>\n\tBolsistas de Iniciação Científica\n</h3>\n")
orientacoes.write("<!-- Iframe para os bolsistas de IC -->\n")
orientacoes.write("\t\t\t<iframe src='bolsistas_ic.html'   name='b_ic' id='orient_ic'>     </iframe>\n")


orientacoes.write("</body>\n</html>")
orientacoes.close()  
###############################################################################

###############################################################################
'''          Iframe - orientacoes_mestrado.html (Aba Orientações)           '''
orientacoes_mestrado = open("orientacoes_mestrado.html", "w")             # Abrindo/criando o arquivo no modo escrita

hhh = 0

#orientacoes_mestrado.write("<p> AQUI </p>")
#DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO   ORIENTACOES-CONCLUIDAS-PARA-MESTRADO
mestrado_titulo = xmldoc.getElementsByTagName("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO")
for hhh in mestrado:
    titulo_mestrado = hhh.attributes["TITULO"].value
    titulo_mestrado = titulo_mestrado.encode('utf-8')
    
    
mestrado_nome = xmldoc.getElementsByTagName("DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO")
for mest_n in mestrado:
    nome_mestrando = mest_n.attributes["NOME-DO-ORIENTADO"].value    
    nome_mestrando = nome_mestrando.encode('utf-8')
    
    
    


orientacoes_mestrado.write("</body>\n</html>")
orientacoes_mestrado.close()  

###############################################################################


###############################################################################
'''          Iframe - orientacoes_doutorado.html (Aba Orientações)          '''
orientacoes_doutorado = open("orientacoes_doutorado.html", "w")             # Abrindo/criando o arquivo no modo escrita

orientacoes_doutorado.write("<p> AQUI </p>")

orientacoes_doutorado.write("</body>\n</html>")
orientacoes_doutorado.close()  

###############################################################################

###############################################################################
'''               Iframe - bolsistas_ic.html (Aba Orientações)              '''
bolsistas_ic = open("bolsistas_ic.html", "w")             # Abrindo/criando o arquivo no modo escrita

bolsistas_ic.write("<p> AQUI </p>")

bolsistas_ic.write("</body>\n</html>")
bolsistas_ic.close()  
###############################################################################

###############################################################################
'''               Iframe - periodicos.html (Aba Publicações)              '''
periodicos = open("periodicos.html", "w")             # Abrindo/criando o arquivo no modo escrita

periodicos.write("<p> AQUI </p>")

periodicos.write("</body>\n</html>")
periodicos.close()  
###############################################################################

###############################################################################
'''               Iframe - trab_anais.html (Aba Publicações)              '''
trab_anais = open("trab_anais.html", "w")             # Abrindo/criando o arquivo no modo escrita

trab_anais.write("<p> AQUI </p>")

trab_anais.write("</body>\n</html>")
trab_anais.close()  
###############################################################################

###############################################################################
'''               Iframe - resumos_expandidos.html (Aba Publicações)              '''
resumos_expandidos = open("resumos_expandidos.html", "w")             # Abrindo/criando o arquivo no modo escrita

resumos_expandidos.write("<p> AQUI </p>")

resumos_expandidos.write("</body>\n</html>")
resumos_expandidos.close()  
###############################################################################

###############################################################################
'''               Iframe - resumos_publicados.html (Aba Publicações)              '''
resumos_publicados = open("resumos_publicados.html", "w")             # Abrindo/criando o arquivo no modo escrita

resumos_publicados.write("<p> AQUI </p>")

resumos_publicados.write("</body>\n</html>")
resumos_publicados.close()  
###############################################################################

###############################################################################
'''               Iframe - artigos_aceitos.html (Aba Publicações)              '''
artigos_aceitos = open("artigos_aceitos.html", "w")             # Abrindo/criando o arquivo no modo escrita

artigos_aceitos.write("<p> AQUI </p>")

artigos_aceitos.write("</body>\n</html>")
artigos_aceitos.close()  
###############################################################################

###############################################################################
'''               Iframe - outras_producoes.html (Aba Publicações)              '''
outras_producoes = open("outras_producoes.html", "w")             # Abrindo/criando o arquivo no modo escrita

outras_producoes.write("<p> AQUI </p>")

outras_producoes.write("</body>\n</html>")
outras_producoes.close()  
###############################################################################
