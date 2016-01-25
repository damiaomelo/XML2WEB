#!/usr/bin/python
# coding: UTF-8
'''****************************************************************************
*                  __author__ = "Levindo Gabriel Taschetto Neto"              *
*                  __email__ = "falecom@levindoneto.com"                      *
*                  __status__ = "Finalizado"                                 *
*****************************************************************************'''
from operator import itemgetter           # Para ordenar o dicionário de listas
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
contato.write("    content: attr(data-user);\nn")
contato.write("  }")
contato.write("</style>\n")
contato.write("\n")
contato.write('\n<section id="email_contato">\n')
contato.write("<my-email data-user='" + emailname + "'" +  " data-domain= '"+ emailserver + "'>@</my-email>")
contato.write("\n</section>")
contato.write("\n<br/><br/><br/><br/><br/><br/><br/>\n")
contato.write("\n<br/><br/><br/>\n")
bigSpace(contato)
criaFooter(contato)
contato.close()                                         # Fechando o arquivo
###############################################################################

###############################################################################
'''                              Aba 'INDEX'                                '''
index = open("index.html", "w")                   # Abrindo/criando o arquivo no modo escrita
criaHeader(index)

index.write("\n\t<section id='corpo' </p>\n")
index.write("\t\t\t<!-- Iframe para a descrição retirada do currículo lattes -->\n")
index.write("\t\t\t<iframe src='descricao.html'   name='n_descricao' id='descricao'>     </iframe>\n")
index.write("\t\t\t<h1> Publicações com destaque </h1>\n")
index.write("\t\t\t<!-- Iframe para as publicações mais relevantes           -->\n")
index.write('\t\t\t<iframe src="relevantes.html" name="n_relevantes" id="relevantes">    </iframe>\n')
index.write("\t</section>            <!--Aqui termina o corpo principal da página-->\n")
index.write("\t<aside id='lateral' </p> \n")
index.write("\t\t\t<!-- Iframe para a foto de perfil do usuário              -->\n")
index.write("\t\t\t<iframe src='foto.html' name='n_foto' id='foto'>                      </iframe>\n\n")
index.write("\t</aside> <!--Aqui termina a parte lateral da página-->\n")
index.write("<!-- lateral_rodape é onde fica os endereços e contato dos professores na parte inferior da página --> \n")
index.write("\t<footer id='rodape_infos'        </p>\n")
index.write("\t\t\t<!-- Lado esquerdo: Endereço e contato -->\n")
index.write("\t\t\t<section id='rodape_esq' </p>\n")
index.write("\t\t\t\t<!-- Iframe para o endereço                           -->\n")
index.write("\t\t\t\t<iframe src='endereco.html' name='n_endereco' id='endereco'>      </iframe>\n")
index.write("\t\t\t</section>\n")
index.write("\t\t\t\t<!-- Lado direito: Logos -->\n")
index.write("\t\t\t<section id='rodape_dir' </p>\n")
index.write("\t\t\t\t\t<!-- Iframe para os logos                         -->\n")
index.write("\t\t\t\t\t<iframe src='logos.html' name='n_logos' id='logos'>           </iframe>\n")
index.write("\t\t\t</section>\n")
index.write("\t</footer>                                      <!-- Fim do rodapé -->  \n\n")
index.write("\t<!-- Aqui é onde fica o menu de rodapé(menu inferior de acesso)   -->\n")
index.write("\t<footer id='rodape'\n")
index.write("\t\t\t\t\t<><a class='menu_rodape' href="">Página Inicial                </a>\n")
index.write("\t\t\t\t\t<a class='menu_rodape' href='publicacoes.html'>Publicações     </a>\n")
index.write("\t\t\t\t\t<a class='menu_rodape' href='pesquisa.html'>Pesquisa           </a>\n")
index.write("\t\t\t\t\t<a class='menu_rodape' href='contato.html'>Contato             </a>\n")
index.write("\t</footer>                      <!--Aqui termina o rodapé da página-->\n\n")
index.write("\t</div>\n</body>\n</html>")

criaFooter(index)
index.close()                                         # Fechando o arquivo
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
orientacoes.write("\t\t\t<iframe src='orientacoes_doutorado.html'   name='o_dout' id='orient_d'>     </iframe>\n")

orientacoes.write("<h3>\n\tOrientações de Mestrado\n</h3>\n")
orientacoes.write("<!-- Iframe para as orientações de mestrado -->\n")
orientacoes.write("\t\t\t<iframe src='orientacoes_mestrado.html'   name='o_mest' id='orient_m'>     </iframe>\n")

orientacoes.write("<h3>\n\tOrientação de graduação\n</h3>\n")
orientacoes.write("<!-- Iframe para os bolsistas de IC -->\n")
orientacoes.write("\t\t\t<iframe src='orientacoes_graduacao.html'   name='b_ic' id='orient_ic'>     </iframe>\n")

criaFooter(orientacoes)
orientacoes.write("</body>\n</html>")
orientacoes.close()  
###############################################################################


###############################################################################
'''                            Orientações                                  '''
###############################################################################

###############################################################################
'''          Iframe - orientacoes_doutorado.html (Aba Orientações)          '''
orientacoes_doutorado = open("orientacoes_doutorado.html", "w")       # Abrindo/criando o arquivo no modo escrita
criaHTML(orientacoes_doutorado)                                       # Configurações iniciais do HTML

# Inicializando as listas de dados para as orientações de doutorado
lista_nome_doutorado = []
lista_ano_doutorado = []
lista_titulo_doutorado = []
contDoutorado = 0                  # Contador do número de orientações de doutorado

basico_doutorado = xmldoc.getElementsByTagName("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO")
for dddb in basico_doutorado:
    titulo_doutorado = dddb.attributes["TITULO"].value              # Título do doutorando
    titulo_doutorado = titulo_doutorado.encode('utf-8')
    titulo_doutorado = str(titulo_doutorado)
    lista_titulo_doutorado.append(titulo_doutorado)

    ano_doutorado = dddb.attributes["ANO"].value              # Ano do doutorado
    ano_doutorado = ano_doutorado.encode('utf-8')
    ano_doutorado = str(ano_doutorado)
    lista_ano_doutorado.append(ano_doutorado)

    contDoutorado += 1

detalhamento_doutorado = xmldoc.getElementsByTagName("DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO")
for ddd in detalhamento_doutorado:
    doutorando = ddd.attributes["NOME-DO-ORIENTADO"].value              # Nome do doutorando
    doutorando = doutorando.encode('utf-8')
    doutorando = str(doutorando)
    lista_nome_doutorado.append(doutorando)

lista_nome_doutorado.reverse()
lista_ano_doutorado.reverse()
lista_titulo_doutorado.reverse()

for phd in range(contDoutorado):
    orientacoes_doutorado.write('<p>' + str(lista_nome_doutorado[phd]) + ' (' + str(lista_ano_doutorado[phd]) + ') </p>' + '\n')
    orientacoes_doutorado.write('<p class="titulo_orientacoes">' + str(lista_titulo_doutorado[phd]) + '</p>')

orientacoes_doutorado.write("</body>\n</html>")
orientacoes_doutorado.close()

###############################################################################

###############################################################################
'''          Iframe - orientacoes_mestrado.html (Aba Orientações)           '''
orientacoes_mestrado = open("orientacoes_mestrado.html", "w")     # Abrindo/criando o arquivo no modo escrita
criaHTML(orientacoes_mestrado)                                    # Configurações iniciais do HTML

# Inicializando as listas de dados para as orientações de mestrado
lista_nome_mestrado = []
lista_ano_mestrado = []
lista_titulo_mestrado = []
contMestrado = 0                     # Contador do número de orientações de mestrado

basico_mestrado = xmldoc.getElementsByTagName("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO")
for mmmb in basico_mestrado:
    titulo_mestrado = mmmb.attributes["TITULO"].value                 # Título do mestrando
    titulo_mestrado = titulo_mestrado.encode('utf-8')
    titulo_mestrado = str(titulo_mestrado)
    lista_titulo_mestrado.append(titulo_mestrado)

    ano_mestrado = mmmb.attributes["ANO"].value                       # Ano do mestrando
    ano_mestrado = ano_mestrado.encode('utf-8')
    ano_mestrado = str(ano_mestrado)
    lista_ano_mestrado.append(ano_mestrado)

    contMestrado += 1

detalhamento_mestrado = xmldoc.getElementsByTagName("DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO")
for mmm in detalhamento_mestrado:
    mestrando = mmm.attributes["NOME-DO-ORIENTADO"].value              # Nome do mestrando
    mestrando = mestrando.encode('utf-8')
    mestrando = str(mestrando)
    lista_nome_mestrado.append(mestrando)

lista_nome_mestrado.reverse()
lista_ano_mestrado.reverse()
lista_titulo_mestrado.reverse()

for mest in range(contMestrado):
    orientacoes_mestrado.write('<p>' + str(lista_nome_mestrado[mest]) + ' (' + str(lista_ano_mestrado[mest]) + ') </p>' + '\n')
    orientacoes_mestrado.write('<p class="titulo_orientacoes">' + str(lista_titulo_mestrado[mest]) + '</p>')

orientacoes_mestrado.write("</body>\n</html>")
orientacoes_mestrado.close()
###############################################################################

###############################################################################
'''               Iframe - orientacoes_graduacao.html (Aba Orientações)              '''
orientacoes_graduacao = open("orientacoes_graduacao.html", "w")             # Abrindo/criando o arquivo no modo escrita
criaHTML(orientacoes_graduacao)                                    # Configurações iniciais do HTML

# Inicializando as listas de dados para as orientações de graduação
lista_nome_graduacao = []
lista_ano_graduacao = []
lista_titulo_graduacao = []
contGraduacao = 0                     # Contador do número de orientações de mestrado

flagNatureza = 0                      # 1-IC, 2-TCC

basico_graduacao = xmldoc.getElementsByTagName("DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS")
for gggb in basico_graduacao:

    titulo_graduacao = gggb.attributes["TITULO"].value                 # Título do graduando
    titulo_graduacao = titulo_graduacao.encode('utf-8')
    titulo_graduacao = str(titulo_graduacao)

    naturezaOrientacao = gggb.attributes["NATUREZA"].value
    if naturezaOrientacao == "INICIACAO_CIENTIFICA":
       titulo_graduacao = titulo_graduacao + " - <u>Iniciação Científica</u>"

    elif naturezaOrientacao == "TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO":
       titulo_graduacao = titulo_graduacao + " - <u>Trabalho de Conclusão de Curso</u>"
    lista_titulo_graduacao.append(titulo_graduacao)

    ano_graduacao = gggb.attributes["ANO"].value                       # Ano do graduando
    ano_graduacao = ano_graduacao.encode('utf-8')
    ano_graduacao = str(ano_graduacao)
    lista_ano_graduacao.append(ano_graduacao)

    contGraduacao += 1

detalhamento_graduacao = xmldoc.getElementsByTagName("DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS")
for ggg in detalhamento_graduacao:
    graduando = ggg.attributes["NOME-DO-ORIENTADO"].value              # Nome do graduando
    graduando = graduando.encode('utf-8')
    graduando = str(graduando)
    lista_nome_graduacao.append(graduando)

lista_nome_graduacao.reverse()
lista_ano_graduacao.reverse()
lista_titulo_graduacao.reverse()

for grad in range(contGraduacao):
        orientacoes_graduacao.write('<p>' + str(lista_nome_graduacao[grad]) + ' (' + str(lista_ano_graduacao[grad]) + ') </p>' + '\n')
        orientacoes_graduacao.write('<p class="titulo_orientacoes">' + str(lista_titulo_graduacao[grad]) + '</p>')

orientacoes_graduacao.write("</body>\n</html>")
orientacoes_graduacao.close()
###############################################################################

###############################################################################
'''                      Artigos e trabalhos                                '''
###############################################################################
'''               Iframe - periodicos.html (Aba Publicações)              '''
periodicos = open("periodicos.html", "w")             # Abrindo/criando o arquivo no modo escrita

basico_periodicos = xmldoc.getElementsByTagName("DADOS-BASICOS-DO-ARTIGO")
contadorPeriodico = 1                        # Contador de artigos

lista_titulo_periodico = []
lista_ano_periodico = []
lista_link_periodico = []
lista_local_periodico = []

# Um dicionario para cada lista, assim a relação entre eles é feita pelos indices dos dicicionarios
dicionario_periodicos_titulos = {}
dicionario_periodicos_anos = {}
dicionario_periodicos_links = {}
dicionario_periodicos_locais = {}

periodicos.write("<br/>")

for a in basico_periodicos:
    # Cada nome de artigo tambem ficará na formatação UTF-8
    titulo_do_periodico = (a.attributes["TITULO-DO-ARTIGO"].value).encode('utf-8')
    lista_titulo_periodico.append(titulo_do_periodico)

    ano_do_periodico = a.attributes["ANO-DO-ARTIGO"].value
    lista_ano_periodico.append(ano_do_periodico)

    link_do_periodico = a.attributes["HOME-PAGE-DO-TRABALHO"].value
    link_do_periodico = str(link_do_periodico)
    link_do_periodico =  link_do_periodico.replace("doi:", "http://dx.doi.org/")
    #Removendo '[' e ']'
    link_do_periodico =  link_do_periodico.replace("[", "")
    link_do_periodico =  link_do_periodico.replace("]", "")
    lista_link_periodico.append(link_do_periodico)

    contadorPeriodico += 1

''' Autores dos periódicos '''
autores = xmldoc.getElementsByTagName("AUTORES")
for au in autores:
        autor = au.attributes["NOME-COMPLETO-DO-AUTOR"].value

''' Locais de publicação dos periódicos '''
locais = xmldoc.getElementsByTagName("DETALHAMENTO-DO-ARTIGO")
for loc in locais:
        local = loc.attributes["LOCAL-DE-PUBLICACAO"].value
        lista_local_periodico.append(local)


# Organizando a lista de dados para ficar em ordem decrescente de acordo com os anos de publicação
lista_titulo_periodico.reverse()
lista_ano_periodico.reverse()
lista_link_periodico.reverse()
lista_local_periodico.reverse()

# Montando dicionario com as listas
for dic in range(contadorPeriodico-1):
    dicionario_periodicos_titulos.update( {str(dic):str(lista_titulo_periodico[dic])})
    dicionario_periodicos_anos.update( {str(dic):str(lista_ano_periodico[dic])})
    dicionario_periodicos_links.update( {str(dic):str(lista_link_periodico[dic])})
    dicionario_periodicos_locais.update( {str(dic):str(lista_local_periodico[dic])})

for per in range(contadorPeriodico-1):
    if lista_link_periodico[per] != "":
        periodicos.write('<a target="blank" ')
        periodicos.write("href='" + str(lista_link_periodico[per])  + "'")
        periodicos.write(' > ' + str(lista_titulo_periodico[per].encode('utf-8')) + ' (' + str(lista_ano_periodico[per].encode('utf-8')) + ') ')
        periodicos.write('</a> <br/>'  + str(lista_local_periodico[per].encode('utf-8')) + '\n')
        periodicos.write("\n<br/>\n")            # Quebra de linha
    else:
        periodicos.write(str(lista_titulo_periodico[per].encode('utf-8')) + ' (' + str(lista_ano_periodico[per].encode('utf-8')) + ') ')
        periodicos.write('\n' + '<p class="local_periodico"' + ">" + str(lista_local_periodico[per].encode('utf-8')) + ' </p>' + '\n')
        periodicos.write("\n")            # Quebra de linha

periodicos.write("</body>\n</html>")
periodicos.close()
###############################################################################

###############################################################################
'''               Iframe - trab_anais.html (Aba Publicações)              '''
trab_anais = open("trab_anais.html", "w")    # Abrindo/criando o arquivo no modo escrita

criaHTML(trab_anais)
basico_trabalhos = xmldoc.getElementsByTagName("DADOS-BASICOS-DO-TRABALHO")
contadorTrabalho = 1                        # Contador de artigos = 1                        # Contador de artigos

lista_titulo_trabalho = []
lista_ano_trabalho = []
lista_link_trabalho = []
lista_local_trabalho = []

# Um dicionario para cada lista, assim a relação entre eles é feita pelos indices dos dicicionarios
dicionario_trabalhos_titulos = {}
dicionario_trabalhos_anos = {}
dicionario_trabalhos_links = {}
dicionario_trabalhos_locais = {}

trab_anais.write("<br/>")

for t in basico_trabalhos:
    # Cada nome de artigo tambem ficará na formatação UTF-8
    titulo_trabalho = (t.attributes["TITULO-DO-TRABALHO"].value).encode('utf-8')
    lista_titulo_trabalho.append(titulo_trabalho)

    ano_trabalho = t.attributes["ANO-DO-TRABALHO"].value
    lista_ano_trabalho.append(ano_trabalho)

    link_do_trabalho = t.attributes["HOME-PAGE-DO-TRABALHO"].value
    link_do_trabalho = str(link_do_trabalho)
    link_do_trabalho =  link_do_trabalho.replace("doi:", "http://dx.doi.org/")
    #Removendo '[' e ']'
    link_do_trabalho =  link_do_trabalho.replace("[", "")
    link_do_trabalho =  link_do_trabalho.replace("]", "")
    lista_link_trabalho.append(link_do_trabalho)

    contadorTrabalho += 1


''' Autores dos trabalhos '''
autores_trabalhos = xmldoc.getElementsByTagName("AUTORES")
for tr in autores_trabalhos:
        autor_trabalho = tr.attributes["NOME-COMPLETO-DO-AUTOR"].value

''' Locais de publicação dos trabalhos '''
locais_trabalhos = xmldoc.getElementsByTagName("DETALHAMENTO-DO-TRABALHO")
for loctr in locais_trabalhos:
        local_trabalho = loctr.attributes["NOME-DO-EVENTO"].value
        lista_local_trabalho.append(local_trabalho)

# Organizando a lista de dados para ficar em ordem decrescente de acordo com os anos de publicação
lista_titulo_trabalho.reverse()
lista_ano_trabalho.reverse()
lista_link_trabalho.reverse()
lista_local_trabalho.reverse()

'''
# Montando dicionario com as listas
for dictr in range(contadorTrabalho-1):
    dicionario_trabalhos_titulos.update( {str(dictr):str(lista_titulo_trabalho[dictr])})
    dicionario_trabalhos_anos.update( {str(dictr):str(lista_ano_trabalho[dictr])})
    dicionario_trabalhos_links.update( {str(dictr):str(lista_link_trabalho[dictr])})
    dicionario_trabalhos_locais.update( {str(dictr):str(lista_local_trabalho[dictr])})
'''

for tra in range(contadorTrabalho-1):
    if lista_link_trabalho[tra] != "":
        trab_anais.write('<a target="blank" ')
        trab_anais.write("href='" + str(lista_link_trabalho[tra].encode('utf-8'))  + "'")
        trab_anais.write(str(lista_titulo_trabalho[tra]) + ' (' + str(lista_ano_trabalho[tra].encode('utf-8')) + ') ')
        trab_anais.write("</a>"+ "\n" + "<p class='local_trabalho'" + ">" + str(lista_local_trabalho[tra].encode('utf-8')) + " </p>" + "\n")
        trab_anais.write("\n")            # Quebra de linha
    else:
        trab_anais.write('<p>' + str(lista_titulo_trabalho[tra]) + ' (' + str(lista_ano_trabalho[tra].encode('utf-8')) + ') ' + '</p>')
        trab_anais.write("\n" + "<p class='local_trabalho'" + ">" + str(lista_local_trabalho[tra].encode('utf-8')) + " </p>" + "\n")
        trab_anais.write("\n")            # Quebra de linha


trab_anais.write("</body>\n</html>")
trab_anais.close()
###############################################################################

###############################################################################
'''                              Estilo CSS                               '''
estilo_css = open("estilo.css", "w")             # Abrindo/criando o arquivo no modo escrita
estilo_css.write(
'''
@charset "UTF-8"; /*sempre precisa isso para criar um arquivo css separado*/
/*Fonte importada diretamente do Google Fonts -> Usada no nome do professoor*/
    @import url(http://fonts.googleapis.com/css?family=Bree+Serif);
/*Fonte importada diretamente do Google Fonts -> Usada no nome do professoor*/
    @import url(http://fonts.googleapis.com/css?family=Quicksand);

    body
    {
        /*background-image: url(metal.jpg);*/
        color: rgba(000,000,000,1); /*o a significa transparencia que varia de 0.0 a 1.0*/
        background-color: #dddddd; /*Cinza claro*/
    }

    a
    {
        text-decoration: none;
        color: black;
    }

    /* Utilizei uma classe no rodapé, para só modificar alí os links */
    a.menu_rodape
    {
        margin-left: 15px;
        text-decoration: none
    }

    a.menu_rodape:hover
    {
        -webkit-transition: width 2s, height 2s, -webkit-transform 2s;
        font-size: 14pt;
        text-decoration: bold;
        color: #314141;     /*Cinza escuro*/

    }

    div#interface /*Div com ID Interface*/
    {
        width: 900px;
        background-color: white;
        margin: -20px auto 0px auto ; /*Cima, direita, baixo, esquerda*/
        box-shadow: 0px 0px 10px rgba(0,0,0,0.5); /*lateral, vertical, espalhamento, cor*/
        padding: 10px 10px 10px 10px ; /*Espaçamento interno*/
    }

    }

    p
    {
        text-align: justify;
        text-indent: 50px;
        /*text-decoration: underline;*/
    }

    p#descricao_user
    {
        text-align: justify;
        text-indent: 50px;
        /*text-decoration: underline;*/
    }

    p.nome_projeto
    {
		color: #6e4545;
        font-size: 14pt;
        text-decoration: underline;
    }

    p.desc_projeto
    {
        font-size: 11pt;
        text-align: justify;
        color: #353030;
    }

    section#endereco_p
    {
        font-size: 8pt;
    }

    section#email_contato
    {
        font-size: 30pt;
    }


    img#icone /*Ícone do cabeçalho que eu dei id la onde está o endereço da imagem*/
    {
        position: absolute; /*Para não ficar entre os textos e sim ao lado dos mesmos*/
        margin-left: 745px;
        margin-top: -80px;
    }
    /*Header Menu -> Configuração de margem */
    header#menu_cabecalho
    {
        margin-top: -50px;
        margin-bottom: -27px;
    }

    h1
    {
        font-size: 15pt;
    }

    /*Nome do professor*/
    header#cabecalho h1 /*Header com id cabeçalho*/
    {
    font-size: 1pt;
        font-family: 'Bree Serif', serif;
        font-weight: bold;
        color: #3d3a2c;
        margin-top: 0px;
        margin-bottom: -15px;
    }

    /*Descrição rápida, ex: Professor adjunto no Instituto de Informatática da UFRGS*/
    header#cabecalho h2
    {
        font-family: 'Quicksand', sans-serif;
        color: rgba(0,0,0,0.6);
    }

    header#cabecalho /*Borda do cabeçalho*/
    {
        border-bottom: 1px rgba(0,0,0,0.6) solid;
        height: 150px;
        margin-top: 0px;
    }


    nav#menu
    {
        display: block; /*Um bloco pode flutuar na tela*/
        position: relative; /*O menu pode passar por cima dos documentos*/
        top: -115px;
        right: -236.5px;
    }
    nav#menu ul /*Usa-se '#' para chamar um id no munu de navegação*/
    {
        list-style: none; /*Para sumir com os marcadores*/
        text-transform: uppercase;

    }

    nav#menu li
    {
        display: inline-block; /*Para colocar o menu na horizontal*/
        background-color: #c0c0c0;
        padding: 10px;
        margin: 2px;
        transition: background-color 1s;
    }

    nav#menu li:hover
    {
        background-color: #dc7d7d; /*Vermelho salmão */
        color: black;
    }

    nav#menu h1
    {
        display: none; /*Para esconder o que está em h1*/
    }

    nav#menu a:link /*Todo menu que tiver um link(a-ancora)*/
    {
        color: black;

    }

    nav#menu a:hover
    {
        color: white;
    }

    section#corpo
    {
        display: block;
        width: 555px;
        float: left;
        padding: 15px;
       /* border-right: 1px rgba(0,0,0,0.6) solid;    */
    }

    /*  Endereço e contato*/
    section#rodape_esq
    {
        clear: both; /*Para limpar as configurações e separar o rodapé das outras partes*/
        width: 400px;
        float: left;
        display: block;
    }

    /* Logos */
    section#rodape_dir
    {
        clear: both; /*Para limpar as configurações e separar o rodapé das outras partes*/
        width: 300px;
        float: right;
        display: block;
        margin-top: -103px;   /* Para deixar as fotos sem prejudicar o tamanho do rodapé*/
        margin-bottom: 0px;
    }

    aside#lateral
    {
        display: block;
        width: 300px;
        float: right; /*Para fazer o conteudo da lateral flutuar do lado direito, é necessário "display: block"*/
    }

    footer#rodape_infos
    {
        clear: both; /*Para limpar as configurações e separar o rodapé das outras partes*/
        width: 900px;
        float: left;
        display: block;
        border-top: 1px rgba(0,0,0,0.6) solid;     /*Linha preta*/
        padding: 5px 0px 10px 0px ;
        background-color: #e3e3e3; /*Cinza bem claro*/
    }

    footer#rodape
    {
        clear: both; /*Para limpar as configurações e separar o rodapé das outras partes*/
        border-top: 1px rgba(0,0,0,0.6) solid;
        padding: 10px 0px 30px 0px ;
        background-color: #e3e3e3; /*Cinza bem claro*/
    }

    footer#rodape p /*Footer de id rodape, tudo que for parágrafo*/
    {
        text-align: center;
    }

    table#tabelaspec td.coldir
    {
        color: black;
        background-color: #c9c9c9;
        text-align: left;
    }

    table#tabelaspec caption
    {
        color: #3a3a3a;
        font-weight: bold;
        font-size: 13pt;
    }

    table#tabelaspec span
    {
        display: block; /*Para fazer o trecho se desconectar do resto da frase*/
        float: right;
        font-size: 7pt; /*Tamanho da fonte é dado em "pt" e não em "px"*/
        color: #272727;
        margin-top: 10px; /*Por essa parte estar com um espaço embaixo até a tabela*/
    }

    article#noticia-principal h1
    {
        font-size: 12pt;
        color: #241f1b; /*Quase preto*/
        background-color: #bfb9b4; /*Cinza claro*/
    }

    /* Configuração de Iframes */

    iframe
    {
        background: white;
        border: none;
        overflow: hidden;
    }

    iframe#nome
    {
        margin-top: 50px;
        margin-left: 15px;
        width: 390px;
        height: 60px;
        margin-top: -15px;
        margin-bottom: -90px;
    }

    iframe#nome::-webkit-scrollbar
    {
        display: none;
    }

    iframe#descricao
    {
        width: 566px;
        height: 310px;
    }

    iframe#publicacoes
    {
        width: 870px;
        margin-bottom: 20px;
    }

    iframe#relevantes
    {
        width: 870px;
    }

    iframe#foto
    {
        margin-top: 11px;
        margin-left: 70px;
        width: 170px;
        height: 175px;
    }

    /* Para não poder usar o scroll na parte da foto*/
    iframe#foto::-webkit-scrollbar
    {
        display: none;
    }

    img#foto_index
    {
    border: 1px solid;
    border-radius: 15px;
    }

    img#logo_01
    {
        display: block;
        margin-left: 0px;
        margin-top: -8px;
        /*margin-bottom: -20px;   */
    }

    img#logo_02
    {
        display: block;
        margin-left: 140px;
        margin-top: -105px;
    }

    /* A classe clique é utilizada nas publicações normais e com mais destaque */
    img.clique
    {
        display: block;
        margin-top: -18px;
        margin-left: 820px;
    }

    /* Rodapé */
    iframe#endereco
    {
        margin-left: 15px;
        margin-top: 15px;
        width: 566px;
        height: 120px;

    }

    iframe#logos
    {
        height: 120px;
        margin-top: -18px;
        margin-left: -5px;
        margin-bottom: -10px;
    }

    iframe#endereco::-webkit-scrollbar
    {
        display: none;
    }

    iframe#logos::-webkit-scrollbar
    {
        display: none;
    }

    /* Projetos de pesquisa - Aba Pesquisa */
    iframe#p_pesq
    {
        height: 536px;
        width: 901px;
    }

    /* Orientações */
    iframe#orient_m
    {
        height: 179px;
        width: 901px;
    }
    iframe#orient_d
    {
        height: 178px;
        width: 901px;
    }
    iframe#orient_ic
    {
        height: 179px;
        width: 901px;
    }

    iframe#publicacoes_frame
    {
        height: 705px;
        width: 901px;
    }

    /* Publicações */
    iframe#periodicos
    {
        height: 265px;
        width: 880px;
    }
    iframe#anais
    {
        height: 265px;
        width: 880px;
    }

    p.local_trabalho
    {
		margin-top: -15px;
        font-size: 11pt;
		color: #956d6d;
	}

    p.local_periodico
    {
		margin-top: -15px;
        font-size: 11pt;
		color: #956d6d;
	}

	p.titulo_orientacoes
    {
		margin-top: -15px;
        font-size: 11pt;
		color: #956d6d;
	}

'''
)
estilo_css.close()
