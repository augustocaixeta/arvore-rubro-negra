# Árvore Rubro-Negra

Implementação de uma árvore rubro-negra (red-black tree) em Python, com operações de inserção, remoção e busca.

## Sobre

Árvore rubro-negra é uma árvore binária de busca balanceada onde cada nó tem uma cor (vermelho ou preto). Ela mantém o balanceamento através de 5 propriedades básicas que garantem que a altura seja sempre O(log n).

## Propriedades

1. Todo nó é vermelho ou preto
2. A raiz é preta
3. Folhas (NIL) são pretas
4. Nós vermelhos não podem ter filhos vermelhos
5. Todos os caminhos da raiz até as folhas têm o mesmo número de nós pretos

## O que foi implementado

- Inserção com rebalanceamento automático
- Remoção com rebalanceamento automático  
- Busca
- Rotações (esquerda e direita)
- Correção após inserção e remoção (recoloração)
- Função para visualizar a árvore

## Como usar

```bash
python index.py
```

O script mostra exemplos de inserção, busca e remoção com a árvore sendo impressa após cada operação. Na visualização, `(P)` indica nó preto e `(V)` indica nó vermelho.

## Casos principais

**Inserção:** Quando um nó vermelho é inserido e seu pai também é vermelho, é necessário corrigir a violação. Se o tio é vermelho, aplica-se recoloração. Se o tio é preto, aplica-se rotação.

**Remoção:** Quando um nó preto é removido, pode violar as propriedades da árvore. É necessário analisar a cor do irmão e dos sobrinhos para decidir se aplica rotação, recoloração ou ambos.

A remoção é mais complexa que a inserção devido ao maior número de casos a tratar.

## Arquivos

- `index.py` - código principal com as classes RBNo e RBArvore
- `README.md` - este arquivo
