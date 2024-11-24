<h1>🛠️ Hello, peoples!</h1>
<p>
Este projeto eu fiz pela graduação, no qual eu deveria criar um jogo (qualquer linguagem) da maneira que preferir. Decidi concluir o projeto em python pela facilidade de leitura, aprendizado e praticidade.<br>
Pela diversidade eu resolvi fazer o jogo da forca, pois na minha opnião é um bom jogo para testar os seus conhecimentos. Bom, não tem muito oque explicar sobre o jogo, mas basicamente: O usuário tera de escolher um tema e à partir disso será gerado aleatóriamente uma das palavras descrito na função do tema.
</p>

<h1>📌 Explicando o código</h1>
<p>
  Inicialmente começamos com a função do jogo: "forca()". Em seguida temos a definição dos temas e suas palavras, ao usuário digitar o número correspondente o código irá pegar aleatoriamente uma das palavras contidas no  tema e irá colocar para usuário descobrir a palavra corretamente, por letras. Após isso, exibimos ao usuário os temas disponíveis, através da função "temas.items()" que serve para retornar cada número e tema, o nome do tema é exibido em "f".<br>A seguir temos a escolha do tema, se o usuário digitar o número corretamente, o "try" converte a entrada em um número inteiro, o "while" verifica se a escolha está coerente as opções e "except ValueError" é caso usuário digite algo além de números. À partir disso, temos a configuração inicial do código, utilizando "tema_nome" para recuperar o nome do tema e utilizamos "palavras_tema" com base na escolha do usuário. Para fazer com que o código gere as palavras aleatoriamente, utilizamos "random.choice" e convertemos para letras minusculas com ".lower()". Com "letras_descobertas" criamos uma lista com "_" para letras que ainda não foram descobertas e " " para palavras que contenham espaço. Inicializamos com que o usuário tenha 6 tentativas de acerto, cada erro diminui  a quantidade de tentativa, ao zerar você perde o jogo. O " while tentativas_restantes" faz com que o jogo não pare enquanto não tiver completado a palavra. Quando usuário digitar a letra, utilizamos "tentativa = input ( ~~~ ).strip().lower()" removendo alguns espaços extras com .strip() e convertendo para letras minúsculas com .lower(). O "isalpha()" verifica se a letra e verdadeira.<br>A seguir o código verifica se o usuário não digitou nenhuma letra repetida. Após isso, em casos de acerto é atualizado a posição correspondente na "lista_descoberta", em caso de erro é adicionado a lista de letras erradas e diminui as tentativas. Concluindo, verificamos se o jogador tenha completado toda a palavra corretamente sem conter nenhum "_" exibindo uma mensagem de vitória ou derrota. Por fim, inicializamos o jogo através da função.
</p>


<h2>📂 Questions</h2>
<p>1º Porque eu escolhi a linguagem Python?<br>R: Praticidade e aprendizado.
</p>
