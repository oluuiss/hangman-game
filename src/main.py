import random

def forca():
    print("--- Bem-vindo ao Jogo da Forca! ---")
    

    temas = {
        1: ("Filmes & Series", ["titanic", "corra", "you", "breaking bad", "dexter", "lucifer", "la casa de papel", "outher banks", "vis a vis", "stranger things", "gossip girl", "lupin", "alice in borderland", "death note", "jurassic park", "avatar", "clube da luta", "as branquelas", "toy story", "shrek", "meu malvado favorito", "homem aranha", "one piece", "suits", "the walking dead", "rick and morty", "os simpsons", "bojack horseman"]),
        2: ("Jogos", ["minecraft", "fortnite", "valorant", "zelda", "pokemon", "xadrez", "league of legends", "roblox", "brawl stars", "terraria", "fall guys", "the sims", "uncharted", "elden ring", "overwatch", "world of warcraft", "gran turismo", "forza horizon", "the last of us", "street fighter", "mortal kombat", "stardew valley"]),
        3: ("Computação", ["processador", "arquivo", "memoria ram", "codigo", "programacao", "python", "teclado", "mouse", "gabinete", "placa mae", "placa de video", "monitor", "software", "memoria", "disco rigido"]),
        4: ("Marcas de carro", ["bmw", "aston martin", "mercedes benz", "audi", "toyota", "chevrolet", "tesla", "ora", "byd", "porsche", "lamborghini", "pagani", "volkswagen", "honda", "ford", "ram", "dodge", "citroen", "hyundai", "jeep", "ferrari", "cadillac", "gmc", "mazda", "mitsubish", "subaru", "lexus", "suzuki", "alfa romeu", "maserati", "jaguar", "bentley", "rolls royce", "land rover", "mini", "kia", "volvo", "koenigsegg"]),
        5: ("Marcas globais", ["louis vuitton", "mc donalds", "burguer king", "apple", "sansumg", "coca cola", "pepsi", "nestle", "sephora", "kfc", "red bull", "avon", "puma", "new balance", "amazon", "disney", "netflix", "spotify", "kopenhagen", "gucci", "versace", "chanel", "nike", "adidas", "rolex", "prada", "balenciaga"])
    }

    

    print("| Temas disponíveis:")
    for numero, (nome, _) in temas.items():
        print(f"| {numero}. {nome}")

    print("---------------------------")
    

    try:
        escolha = int(input("\n---------------------------\n| Digite o número do tema que deseja jogar: "))
        while escolha not in temas:
            print("| Opção inválida. Tente novamente.")
            escolha = int(input("| Digite o número do tema que deseja jogar: "))
    except ValueError:
        print("| Por favor, digite um número válido. Reinicie o jogo para tentar novamente.")
        return
    
    tema_nome, palavras_tema = temas[escolha]
    palavra_secreta = random.choice(palavras_tema).lower()
    letras_descobertas = ["_" if char != " " else " " for char in palavra_secreta]
    tentativas_restantes = 6
    letras_erradas = []
    

    while tentativas_restantes > 0 and "_" in letras_descobertas:
        print(f"\n---------------------------\n| Tema escolhido: {tema_nome}")
        print("| Palavra:", " ".join(letras_descobertas))
        print(f"| Letras erradas: {', '.join(letras_erradas)}")
        print(f"| Tentativas restantes: {tentativas_restantes}")
        

        tentativa = input("| Digite uma letra: ").strip().lower()
        
       
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("| Por favor, digite apenas uma letra válida.")
            continue
        
    
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("| Você já tentou essa letra. Tente outra!")
            continue
        
       
        if tentativa in palavra_secreta:
            print("| Ótimo! Acertou a palavra corretamente.\n---------------------------")
            for index, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_descobertas[index] = tentativa
        else:
            print("Que pena, tente novamente! A letra não está na palavra.")
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1
    
    # resultado
    if "_" not in letras_descobertas:
        print("\n---------------------------\n| Parabéns! Você acertou, a palavra é:", palavra_secreta)
        print("---------------------------")
    else:
        print("\n---------------------------\n| Você perdeu! A palavra era:", palavra_secreta)
        print("---------------------------")

# inicia o jogo
forca()