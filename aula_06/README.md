# Aula 06 - Revisão.


```python
!python --version
```

    Python 3.10.13



```python
from site import getsitepackages
```


```python
print(getsitepackages())
```

    ['/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.10/site-packages']



```python
import os
```


```python
os.getcwd()
```




    '/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_06/notebook'




```python
os.chdir('/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_06')
os.getcwd()
```




    '/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_06'



 ## Guia de boas práticas:

A [PEP 8](https://peps.python.org/pep-0008/) é uma das PEPs (Python Enhancement Proposals) mais importantes da comunidade Python. Ela estabelece diretrizes para a formatação do código Python, incluindo convenções de estilo, espaçamento, nomes de variáveis e outros aspectos importantes da escrita de código Python legível e consistente.

A PEP 8 foi criada para promover uma base de código Python que seja fácil de ler e entender para os desenvolvedores, independentemente de quem tenha escrito o código originalmente. Isso é crucial para facilitar a manutenção do código, colaboração entre equipes de desenvolvimento e garantir a qualidade do código em projetos Python de todos os tamanhos.

Ao seguir as diretrizes da PEP 8, os desenvolvedores podem garantir que seu código Python seja coeso, consistente e legível, o que contribui para a sua usabilidade, manutenção e escalabilidade ao longo do tempo.

Em resumo, a [PEP 8](https://peps.python.org/pep-0008/) é uma referência essencial para qualquer desenvolvedor Python que queira escrever código claro, organizado e de fácil manutenção, promovendo as melhores práticas de desenvolvimento na comunidade Python.

### A seguir algumas bibliotecas que nos ajudam a automatizar essas boas práticas de maneira a manter nosso código coeso, consitente e legível:

[**Black:**](https://pypi.org/project/black/)

* O Black é uma ferramenta de formatação de código Python. Ele foi projetado para automatizar a formatação do código Python de acordo com as diretrizes da PEP 8, garantindo assim que o código seja formatado de maneira consistente e legível. Black é conhecido por ser muito rígido em sua formatação e, portanto, é considerado como uma "opinião" sobre como o código Python deve ser formatado.
Além de seguir as diretrizes da PEP 8, o Black também se esforça para produzir um código Python mais conciso e legível, removendo a necessidade de discussões sobre estilos de codificação em equipes de desenvolvimento.

[**isort:**](https://pypi.org/project/isort/)

* O isort é uma ferramenta para ordenar os imports de módulos em arquivos Python. Ele reorganiza automaticamente as declarações de importação em ordem alfabética e agrupa-as de acordo com as convenções de importação específicas. Isso ajuda a manter a organização e a legibilidade dos imports em arquivos Python.
Além de ordenar os imports, o isort também pode corrigir importações erradas e remover imports não utilizados, ajudando a manter o código Python limpo e livre de importações desnecessárias.

[**flake8:**](https://pypi.org/project/flake8/)

* O flake8 é uma ferramenta de verificação de código Python que ajuda a garantir a conformidade com as diretrizes de estilo do PEP 8 e identifica possíveis problemas no código-fonte. Ele verifica o código em busca de erros de sintaxe, problemas de estilo, variáveis não utilizadas e outros problemas potenciais.
O flake8 é altamente configurável e pode ser estendido com plugins para fornecer verificações adicionais específicas ao projeto. É frequentemente usado como parte de pipelines de integração contínua (CI) para garantir a qualidade do código Python em projetos de software.

Em resumo, "black" é uma ferramenta de formatação de código Python, "isort" é uma ferramenta para organizar e ordenar imports, e "flake8" é uma ferramenta de verificação de código que ajuda a manter o código Python consistente, limpo e livre de problemas. Juntas, essas ferramentas são amplamente utilizadas na comunidade Python para promover boas práticas de desenvolvimento e garantir a qualidade do código.

**Conforme a aula vamos executar alguns exemplos para entender o funcionamento de cada lib.**

#### Primeiro vamos instalar o flake8:


```python
#instala a lib flake8 em modo silencioso no ambiente .venv.
!poetry add flake8 -q
```

* Criando uma função simples e salvar o código em src/exemplo1.py:


```python
%%writefile src/exemplo01.py
def minha_funcao ():
    resultado = 2 + 2
    print("O resultado é:", resultado)
if __name__ == "__main__":
    minha_funcao()

```

    Overwriting src/exemplo01.py


* Agora vamos executar o código para garantir que o mesmo esteja funcionando:


```python
!python src/exemplo01.py
```

    O resultado é: 4


* Veja que a função funcionou perfeitamente, porém será que o código está de acordo com a PEP8?
* Podemos usar o flake8 para identificar possíveis erros de padronização conforme abaixo: 


```python
!flake8 src/exemplo01.py
```

    [1msrc/exemplo01.py[m[36m:[m1[36m:[m17[36m:[m [1m[31mE211[m whitespace before '('
    [1msrc/exemplo01.py[m[36m:[m4[36m:[m1[36m:[m [1m[31mE305[m expected 2 blank lines after class or function definition, found 0


* Veja que interessante o flake8 já notificou 2 erros, vamos corrigir:
    * Ele informa que na linha 1  e caracter 17 existe um espaço antes do '(' -> será corrigido
    * Informa que na linha 4 logo no primeiro caracter já solicita que precisa de 2 espaços depois de uma classe ou função. -> corrigido abaixo.
    * Importante notar que informa até mesmo o código "E211 e E305" do erro se precisar podem pesquisar o erro [aqui.](https://www.flake8rules.com/)


```python
%%writefile src/exemplo01.py
def minha_funcao():
    resultado = 2 + 2
    print("O resultado é:", resultado)


if __name__ == "__main__":
    minha_funcao()
```

    Overwriting src/exemplo01.py


* O código foi corrigido agora vamos executar o flake8 novamente:


```python
!flake8 src/exemplo01.py
```

* Veja que ele não trouxe nenhum erro agora, ou seja, dentro dos padrões pré-estabelecidos pelo flake8, o código está legivel.
* O flake8 é muito bom para corrigirmos esses problemas de espaçamentos, excesso de caracteres em uma linha, linhas em branco etc...
* Ele não faz nada no código, apenas informa onde corrigir.

#### Agora vamos instalar o Black:


```python
# instalando a lib black no ambiente virtual.
!poetry add black -q
```

* Agora vamos criar a mesma função porém vamos salvar como src/exemplo02.py


```python
%%writefile src/exemplo02.py
def minha_funcao ():
    resultado = 2 + 2
    print("O resultado é:", resultado)
if __name__ == "__main__":
    minha_funcao()

```

    Writing src/exemplo02.py


* Vamos rodar o black agora:


```python
!black src/exemplo02.py
```

    [1mreformatted src/exemplo02.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m1 file [0m[1mreformatted[0m.


* Vamos abrir o arquivo e verificar o que ele formatou: 


```python
# %load src/exemplo02.py
def minha_funcao():
    resultado = 2 + 2
    print("O resultado é:", resultado)


if __name__ == "__main__":
    minha_funcao()

```

* Veja que o black corrigiu automáticamente os erros de código: "E211 e E305" que o flake8 havia identificado.
* Vamos rodar o flake8 no exemplo02.py para conferir.


```python
!flake8 src/exemplo02.py
```

* O Flake8 executou a verificação sem erros, pois o black já havia realizado as devidas correções.
* Essa é a vantagem com black, pois ele identifica e já corrige o erro de forma autônoma.

* Então quer dizer que podemos unir o melhor dos dois mundos e usar ambas libs para sempre mantermos um código dentro dos padrões?
  * Nem tudo é perfeito, existe um pequeno conflito entre ambas e vou demonstrar aqui para uma melhor compreensão.
  * O Flake8 utiliza por adoção 79 caracteres máximo por linha e o black 88, isso pode gerar um problema.
  * Veja o exemplo abaixo: irei salvar o arquivo em src/conflito_entre_black_e_flake8.py


```python
%%writefile src/conflito_entre_black_e_flake8.py
def exemplo_de_conflito_entre_black_e_flake8():
    variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8 = "conflito"

    if variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8 == "confito":
        print("Conflito entre o Black e o Flake8!")
    else:
        print("Sem conflito entre o Black e o Flake8!")

    return variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8

if __name__=="__main__":
    exemplo_de_conflito_entre_black_e_flake8()

```

    Overwriting src/conflito_entre_black_e_flake8.py


* Vou executar o black para corrigir possíveis erros de formatação automaticamente:


```python
!black src/conflito_entre_black_e_flake8.py
```

    [1mreformatted src/conflito_entre_black_e_flake8.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m1 file [0m[1mreformatted[0m.



```python
# %load src/conflito_entre_black_e_flake8.py
def exemplo_de_conflito_entre_black_e_flake8():
    variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8 = (
        "conflito"
    )

    if (
        variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8
        == "confito"
    ):
        print("Conflito entre o Black e o Flake8!")
    else:
        print("Sem conflito entre o Black e o Flake8!")

    return variavel_com_nome_muito_longo_para_testar_um_conflito_entre_black_e_flake8


if __name__ == "__main__":
    exemplo_de_conflito_entre_black_e_flake8()

```

* Agora irei executar o flake8 para confirmação:


```python
!flake8 src/conflito_entre_black_e_flake8.py
```

    [1msrc/conflito_entre_black_e_flake8.py[m[36m:[m2[36m:[m80[36m:[m [1m[31mE501[m line too long (82 > 79 characters)
    [1msrc/conflito_entre_black_e_flake8.py[m[36m:[m7[36m:[m80[36m:[m [1m[31mE501[m line too long (82 > 79 characters)
    [1msrc/conflito_entre_black_e_flake8.py[m[36m:[m14[36m:[m80[36m:[m [1m[31mE501[m line too long (85 > 79 characters)


* Ué mas o black não realizou as correções e nos informou que já estava tudo certo?
    * Como o black aceita até 88 caracteres ele entendeu que estava tudo certo, veja uma breve explicação e como corrigir isso.



O Black, por padrão, formata o código Python utilizando linhas com até 88 caracteres de comprimento. Ele adota esse limite para facilitar a leitura do código em telas de tamanho padrão e para permitir que as linhas sejam divididas com um nível adequado de aninhamento sem prejudicar a legibilidade.

Por outro lado, o Flake8, por padrão, verifica se as linhas de código Python têm até 79 caracteres de comprimento. Esse limite é baseado nas diretrizes da PEP 8, que recomenda linhas de até 79 caracteres para facilitar a leitura em ambientes com terminais de 80 colunas.

Esses valores padrão diferentes podem causar conflitos entre o Black e o Flake8, já que um pode formatar o código além do limite recomendado pelo outro.

Para resolver esse conflito e usar o Black e o Flake8 juntos, existem algumas abordagens:

Ajustar as Configurações Padrão: Você pode ajustar as configurações padrão do Black e do Flake8 para usar o mesmo limite de comprimento de linha. Isso pode ser feito configurando explicitamente os parâmetros --line-length para o Black e max-line-length para o Flake8 com o mesmo valor (por exemplo, 79 caracteres).

Ignorar Verificações de Comprimento de Linha do Flake8: Você pode configurar o Flake8 para ignorar verificações de comprimento de linha, permitindo que o Black formate o código como desejar. Isso pode ser feito configurando max-line-length para um valor alto ou desativando a verificação de comprimento de linha completamente no arquivo de configuração do Flake8 (setup.cfg ou .flake8).

Ignorar Formatação de Código do Black: Você também pode configurar o Black para ignorar a formatação do código e focar apenas na verificação de erros de estilo usando o Flake8. Isso pode ser feito desativando a formatação automática do Black ou configurando-o para não modificar o comprimento das linhas.

##### Neste exemplo irei configurar o flake8 para aceitar o maximo de 88 caracteres em cada linha e ignorar alguns erros para evitar futuros conflitos, atribuindo a configuração em um arquivo .flake8 conforme abaixo:


```python
%%writefile .flake8
[flake8]
max-line-length = 88
extend-ignore = E203,E701
```

    Overwriting .flake8


* Agora vamos executar o flake8 novamente no nosso arquivo de exemplo:


```python
!flake8 src/conflito_entre_black_e_flake8.py
```

* Agora sim o conflito foi corrigido pois o flake8 agora aceita com maximo 88 caracteres em cada linha.

#### Agora vamos instalar o isort para cuidar da ordem dos imports:


```python
# instala a lib isort no ambiente virtual.
!poetry add isort -q
```

* Agora vou criar uma função de exemplo e salvar como src/exemplo_isort.py


```python
%%writefile src/exemplo_isort.py
# Exemplo de arquivo desorganizado com imports
import os
import math
import site

def calcular_area_circulo(raio):
    """
    Função para calcular a área de um círculo.
    """
    return math.pi * raio ** 2

def diretorio_atual():
    """
    Função para informar o diretório atual.
    """
    return os.getcwd()

def ambiente_atual():
    """
    Informa o ambiente de desenvolvimento atual.
    """
    return site.getsitepackages()
if __name__ == "__main__":
    diretorio_atual()

```

    Overwriting src/exemplo_isort.py


* Executando o isort para organizar a ordem das importações:


```python
!isort src/exemplo_isort.py
```

    Fixing /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_06/src/exemplo_isort.py


* Verificando as alterações:


```python
# %load src/exemplo_isort.py
# Exemplo de arquivo desorganizado com imports
import math
import os
import site


def calcular_area_circulo(raio):
    """
    Função para calcular a área de um círculo.
    """
    return math.pi * raio ** 2

def diretorio_atual():
    """
    Função para informar o diretório atual.
    """
    return os.getcwd()

def ambiente_atual():
    """
    Informa o ambiente de desenvolvimento atual.
    """
    return site.getsitepackages()
if __name__ == "__main__":
    diretorio_atual()

```

* Veja que o isort, segue as diretrizes da PEP 8 e organiza os imports em ordem alfabética.

* Agora vamos garantir um código legível com as 3 libs:


```python
!isort src/exemplo_isort.py
```


```python
!black src/exemplo_isort.py
```

    [1mreformatted src/exemplo_isort.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m1 file [0m[1mreformatted[0m.



```python
!flake8 src/exemplo_isort.py
```

* Analisando o código já com as 3 verificações:


```python
# %load src/exemplo_isort.py
# Exemplo de arquivo desorganizado com imports
import math
import os
import site


def calcular_area_circulo(raio):
    """
    Função para calcular a área de um círculo.
    """
    return math.pi * raio**2


def diretorio_atual():
    """
    Função para informar o diretório atual.
    """
    return os.getcwd()


def ambiente_atual():
    """
    Informa o ambiente de desenvolvimento atual.
    """
    return site.getsitepackages()


if __name__ == "__main__":
    diretorio_atual()

```

* Hoje, aprendemos como usar essas bibliotecas para melhorar nossos processos de desenvolvimento de software. Aprendemos como formatar o código automaticamente com o Black, organizar os imports com o isort e verificar a qualidade do código com o Flake8. Ao dominar essas ferramentas, podemos nos tornar desenvolvedores mais eficientes e produzir código Python de alta qualidade.


```python
# 03/04 02:40
```


```python

```
