# Script para coleta e limpeza de comentários do instagram

## 1. Coleta manual (todos os comentários)
### Passos:
    1. copiar os dados do post selecionando toda a seção de comentários, desde a foto 
    de perfil do primeiro usuário a comentar, até o último comentário.
    
    2. colar no arquivo comments.txt.
    
    3. chamar o script no terminal:
         python comments_clean.py comments.txt data_name 

 
## 2. Coleta automática (amostra até 80% dos comentários)
### Passos:
    1. chamar o script no terminal:
         python getComments.py post_code name_data num_comments
    
    argumentos:
    post_code -> código do post, ex: CSFmIk1hP0h

    name_data -> nome do arquivo que armazena os  comentários.

    num_comments -> número de comentaŕios do post.