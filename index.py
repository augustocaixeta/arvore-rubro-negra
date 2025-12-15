# ---------------------------------------------
# ÁRVORE RUBRO-NEGRA (IMPLEMENTAÇÃO COMPLETA)
# ---------------------------------------------

VERMELHO = 0
PRETO = 1

class RBNo:
    def __init__(self, valor):
        self.valor = valor
        self.cor = VERMELHO
        self.esq = None
        self.dir = None
        self.pai = None

class RBArvore:
    def __init__(self):
        self.nil = RBNo(None)
        self.nil.cor = PRETO
        self.nil.esq = self.nil.dir = self.nil.pai = self.nil
        self.raiz = self.nil

    def rot_esq(self, no):
        filho = no.dir
        no.dir = filho.esq

        if filho.esq != self.nil:
            filho.esq.pai = no

        filho.pai = no.pai

        if no.pai == self.nil:
            self.raiz = filho
        elif no == no.pai.esq:
            no.pai.esq = filho
        else:
            no.pai.dir = filho

        filho.esq = no
        no.pai = filho

    def rot_dir(self, no):
        filho = no.esq
        no.esq = filho.dir

        if filho.dir != self.nil:
            filho.dir.pai = no

        filho.pai = no.pai

        if no.pai == self.nil:
            self.raiz = filho
        elif no == no.pai.dir:
            no.pai.dir = filho
        else:
            no.pai.esq = filho

        filho.dir = no
        no.pai = filho

    def inserir(self, valor):
        novo = RBNo(valor)
        novo.esq = novo.dir = self.nil

        p = self.nil
        no = self.raiz

        while no != self.nil:
            p = no
            if novo.valor < no.valor:
                no = no.esq
            else:
                no = no.dir

        novo.pai = p

        if p == self.nil:
            self.raiz = novo
        elif novo.valor < p.valor:
            p.esq = novo
        else:
            p.dir = novo

        self.corrigir_insercao(novo)

    def corrigir_insercao(self, no):
        while no.pai.cor == VERMELHO:
            avo = no.pai.pai

            # Caso: pai é filho esquerdo do avô
            if no.pai == avo.esq:
                t = avo.dir  # tio

                # Caso 1 – Tio vermelho (recoloração)
                if t.cor == VERMELHO:
                    no.pai.cor = PRETO
                    t.cor = PRETO
                    avo.cor = VERMELHO
                    no = avo  # Subir para o avô

                else:
                    # Caso 2 – Filho direito
                    if no == no.pai.dir:
                        no = no.pai
                        self.rot_esq(no)

                    # Caso 3 – Rotação simples direita
                    no.pai.cor = PRETO
                    avo.cor = VERMELHO
                    self.rot_dir(avo)

            # Caso simétrico: pai é filho direito do avô
            else:
                t = avo.esq  # tio

                if t.cor == VERMELHO:
                    no.pai.cor = PRETO
                    t.cor = PRETO
                    avo.cor = VERMELHO
                    no = avo  # Subir para o avô
                else:
                    if no == no.pai.esq:
                        no = no.pai
                        self.rot_dir(no)

                    no.pai.cor = PRETO
                    avo.cor = VERMELHO
                    self.rot_esq(avo)

        self.raiz.cor = PRETO
    
    def transplant(self, antigo, novo):
        if antigo.pai == self.nil:
            self.raiz = novo
        elif antigo == antigo.pai.esq:
            antigo.pai.esq = novo
        else:
            antigo.pai.dir = novo
        novo.pai = antigo.pai
    
    def minimo(self, no):
        while no.esq != self.nil:
            no = no.esq
        return no
    
    def buscar(self, valor, no=None):
        if no is None:
            no = self.raiz
        
        while no != self.nil:
            if valor == no.valor:
                return no
            elif valor < no.valor:
                no = no.esq
            else:
                no = no.dir
        
        return None
    
    def remover(self, valor):
        alvo = self.raiz

        # Procurar o nó
        while alvo != self.nil and alvo.valor != valor:
            alvo = alvo.esq if valor < alvo.valor else alvo.dir

        if alvo == self.nil:
            return # Nó não encontrado

        substituto = alvo
        cor_original = substituto.cor

        # Caso 1: Apenas filho à direita
        if alvo.esq == self.nil:
            filho = alvo.dir
            self.transplant(alvo, alvo.dir)

        # Caso 2: Apenas filho à esquerda
        elif alvo.dir == self.nil:
            filho = alvo.esq
            self.transplant(alvo, alvo.esq)

        # Caso 3: Dois filhos
        else:
            sucessor = self.minimo(alvo.dir)
            cor_original = sucessor.cor
            filho = sucessor.dir

            if sucessor.pai == alvo:
                filho.pai = sucessor
            else:
                self.transplant(sucessor, sucessor.dir)
                sucessor.dir = alvo.dir
                sucessor.dir.pai = sucessor

            self.transplant(alvo, sucessor)
            sucessor.esq = alvo.esq
            sucessor.esq.pai = sucessor
            sucessor.cor = alvo.cor

        if cor_original == PRETO:
            self.corrigir_remocao(filho)

    def corrigir_remocao(self, no):
        iterador = no

        while iterador != self.raiz and iterador.cor == PRETO:
            pai = iterador.pai

            # Iterador é filho da esquerda
            if iterador == pai.esq:
                irmao = pai.dir  

                # Caso 1: Irmão vermelho
                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    pai.cor = VERMELHO
                    self.rot_esq(pai)
                    irmao = pai.dir

                sobrinho_esq = irmao.esq
                sobrinho_dir = irmao.dir

                # Caso 2: Irmão e sobrinhos pretos
                if sobrinho_esq.cor == PRETO and sobrinho_dir.cor == PRETO:
                    irmao.cor = VERMELHO
                    iterador = pai

                else:
                    # Caso 3: Irmão preto, sobrinho esquerdo vermelho e direito preto
                    if sobrinho_dir.cor == PRETO:
                        sobrinho_esq.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rot_dir(irmao)
                        irmao = pai.dir

                    # Caso 4 — irmão preto e sobrinho direito vermelho
                    irmao.cor = pai.cor
                    pai.cor = PRETO
                    irmao.dir.cor = PRETO
                    self.rot_esq(pai)
                    iterador = self.raiz

            else:
                # Espelho (iterador é filho da direita)
                irmao = pai.esq

                if irmao.cor == VERMELHO:
                    irmao.cor = PRETO
                    pai.cor = VERMELHO
                    self.rot_dir(pai)
                    irmao = pai.esq

                sobrinho_esq = irmao.esq
                sobrinho_dir = irmao.dir

                if sobrinho_esq.cor == PRETO and sobrinho_dir.cor == PRETO:
                    irmao.cor = VERMELHO
                    iterador = pai

                else:
                    if sobrinho_esq.cor == PRETO:
                        sobrinho_dir.cor = PRETO
                        irmao.cor = VERMELHO
                        self.rot_esq(irmao)
                        irmao = pai.esq

                    irmao.cor = pai.cor
                    pai.cor = PRETO
                    irmao.esq.cor = PRETO
                    self.rot_dir(pai)
                    iterador = self.raiz

        iterador.cor = PRETO


    def print_tree(self, no=None, indent="", last=True):
        if no is None:
            no = self.raiz

        if no == self.nil:
            return

        print(indent, "`- " if last else "|- ",
              f"{no.valor} ({'P' if no.cor == PRETO else 'V'})", sep="")

        indent += "   " if last else "|  "

        self.print_tree(no.esq, indent, False)
        self.print_tree(no.dir, indent, True)


if __name__ == "__main__":
    arv = RBArvore()
    inserir_valores = [4, 11, 2, 1, 7, 5, 8, 14, 15]

    print("-> INSERÇÕES...")
    for v in inserir_valores:
        print(f"\nInserindo {v}:")
        arv.inserir(v)
        arv.print_tree()

    print("\n\n-> BUSCAS...")
    buscar_valores = [7, 15, 100, 1, 50]
    
    for b in buscar_valores:
        resultado = arv.buscar(b)
        if resultado:
            print(f"Busca {b}: Encontrado (cor: {'PRETO' if resultado.cor == PRETO else 'VERMELHO'})")
        else:
            print(f"Busca {b}: Não encontrado")

    print("\n\n-> REMOÇÕES...")

    remover_valores = [7, 4, 11, 14]

    for r in remover_valores:
        print(f"\nRemovendo {r}:")
        arv.remover(r)
        arv.print_tree()