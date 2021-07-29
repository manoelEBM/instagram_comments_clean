import sys
import pandas as  pd

from functions.export import export

"""Script para coleta e limpeza de comentários do instagram
Passos:
    1. copiar os dados do post selecionando toda a seção de comentários, desde a foto 
    de perfil do primeiro usuário a comentar, até o último comentário.
    
    2. colar no arquivo comments.txt.
    
    3. chamar o script no terminal:
         python comments_clean.py comments.txt data_name """

# arquivo comments.txt        
comments_path = sys.argv[1]

# nome do arquivo que vai receber os dados limpos, ex: post3
data_name = sys.argv[2]

df = pd.DataFrame(columns=['comentários'])

with open(comments_path) as f:
    lines = f.readlines()
    f.close()

count = 2
comments = []

while(count < len(lines)):

    comments.append(lines[count]) 

    count += 4

df['comentários'] = comments

export(df, data_name)

