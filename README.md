# news-crawler

# Installation
### Linux dependencies
`sudo apt install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`

### Create the environment
- `conda create -n da-vinci python=3.9`
- `conda activate da-vinci`
- `sudo apt install git`
- `git clone git@github.com:icapetti/da-vinci.git`
- `pip install -r requirements.txt`

### Important
This project currently uses:
- [Python 3.9.7](https://www.python.org/downloads/release/python-397/)
- [Scrapy 2.5.1](https://docs.scrapy.org/en/latest/news.html#scrapy-2-5-1-2021-10-05)

Requirements generation:
- `pip install pipreqs`
- `pipreqs /home/icapetti/git/tarcisio/da-vinci --force`
<br>
I don't use `pip freeze` because this saves all packages in the environment including those that you don't use in your current project. `pipreqs` generate requirements.txt file for any project based on imports.
### Projects
- News: extract textual data relating to news.
- This crawler is particularly useful for researches with NLP and Computational Linguistics.
- The items crawled from the website are saved as jsonlines, compressed with gzip and send to a bucket on AWS.
- Example of output jsonline file:
``` python
{
   "date":"12/09/2019 18:23",
   "content":"Um dos indicadores que mais demora a se recuperar após o início da crise econômica no Brasil, em 2014, a taxa de investimentos segue nos menores patamares da história. Depois de chegar a representar 21% do PIB Brasileiro em 2013, a Formação Bruta de Capital Fixo (FBCF), medida pelo IBGE desde 1996, atingiu seu menor patamar em 2017 (14,98%) e pouco evoluiu desde então (15,83% em 2018 e 15,69% no primeiro semestre deste ano).Os números da economia do segundo trimestre do ano, divulgados na última quinta-feira (5), trouxeram algum alento: revelaram que o avanço no investimento produtivo – principalmente na construção civil, com alta de 3,2% – foi o principal fator para o crescimento de 0,4% no PIB no período. Mas logo no dia seguinte veio o balde de água fria: o anúncio do orçamento da União de 2020, com a previsão do menor investimento da história do governo federal.A debandada da União faz com que a responsabilidade pelo investimento produtivo – isto é, o gasto em obras, máquinas e equipamentos que permitam mais produção no futuro – fique ainda mais sobre as costas do setor privado. Que, por vários motivos, anda pensando várias vezes antes de aplicar seu dinheiro. A reforma tributária tem impacto positivo de alavancar a competitividade da produção nacional”, diz.O economista cita, no entanto, que conferir às reformas a responsabilidade pela recuperação do investimento é exagero. Ele comenta que a decisão de investir é mais complexa que apenas reduzir incertezas.“Além da confiança, há elementos importantes como a estrutura de financiamento. Com o encolhimento do BNDES, nosso mercado de capital não desenvolveu musculatura suficiente para compensar. Numa retomada de investimento é importante ter canais de financiamento compatíveis com a rentabilidade dos projetos. E não sabemos se nossa atual estrutura de financiamento vai funcionar num momento de expansão”, diz.",
   "author":"Roger Pereira, especial para a Gazeta do Povo",
   "title":"Queda no investimento e cautela do empresário retardam recuperação",
   "source":"Gazeta do Povo",
   "url":"https://www.gazetadopovo.com.br/republica/queda-investimento-cautela-empresario-retardam-recuperacao/",
   "created_at":"2021-11-02 15:52:51"
}
```