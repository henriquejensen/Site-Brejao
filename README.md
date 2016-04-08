Brejao
===========

Projeto com o intuito de desenvolver um site para o alojamento estudantil da Universidade federal de Lavras (vulgo Brejao)

Ferramentas a serem utilizadas no desenvolvimento:
--------------------------------------------------

Back-end:
    - Python
    - Flask (micro-framework web python)
    - MySQL

Front-end:
    - HTML5
    - CSS3 (utilizando o SASS)
    - JavaScript (utilizando JQuery)

Esqueleto do site:
------------------

- Home
    + Slide
    + Noticias
- Como morar
    + Descricao dos requisitos para morar
    + Links dos requisitos
- Historia
    + Descricao
    + Fotos
- Estrutura
    + Imagens do alojamento
    + Descricao
- Galeria
    + Imagens de festas ou eventos
    + Descricao
- Moradores
    + Apartamentos e seus antigos e atuais moradores
- Contato
    + Formulario de contato com os prefeitos do alojamento

Como contribuir
---------------

- Faça um fork do projeto(somente caso vá contribuir com código) 
- Clone o seu fork em sua máquina
- Crie uma issue ou proponha um PR propondo alguma funcionalidade ou corrigindo algum erro:
- Antes de realizar qualquer modificação:
    + sincronize seu fork com o projeto original
      * como configurar um remoto para um fork
        -`git remote add upstream https://github.com/henriquejensen/brejao.git`
      * sincronizando um fork
        - `git fetch upstream`
        - `git rebase upstream/master`        
    + crie um branch (localmente) para a issue que você deseja resolver com:
        - ` git checkout -b "fix_issue_X" ` 
- Trabalhe localmente, faça suas modificações e commits no seu branch "fix_issue_X" e suba suas alterações para o seu fork remoto com:
    - ` git push -u origin "fix_issue_X" `
- Proponha um PR tomando o seu branch "fix_issue_X" como base no branch "master" do grupython 
- Aguarde aprovação de um dos membros responsáveis pelo projeto.
Caso seja membro do grupython da equipe do Marolo, aguarde aprovação de outro membro que não você próprio.
