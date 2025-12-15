# Árvore Rubro-Negra

Implementação de uma árvore rubro-negra (red-black tree) em Python, desenvolvida do zero com as operações de inserção, remoção e busca.

## O que é uma Árvore Rubro-Negra

Uma árvore rubro-negra é uma árvore binária de busca autobalanceada onde cada nó possui uma cor (vermelho ou preto). O balanceamento é mantido através de cinco propriedades que garantem que a altura da árvore permaneça logarítmica em relação ao número de elementos.

### Propriedades fundamentais

1. Todo nó é vermelho ou preto
2. A raiz é sempre preta
3. Todas as folhas (NIL) são pretas
4. Nós vermelhos não podem ter filhos vermelhos (não há dois nós vermelhos consecutivos)
5. Todos os caminhos de um nó até suas folhas descendentes contêm o mesmo número de nós pretos

## Funcionalidades implementadas

- **Inserção** com rebalanceamento automático (rotações e recoloração)
- **Remoção** com rebalanceamento automático
- **Busca** por valor (retorna o nó ou None)
- **Rotações**: simples à esquerda e à direita
- **Correções**: algoritmos de recoloração após inserção e remoção
- **Visualização**: impressão da árvore com indicação de cores

## Complexidade das operações

| Operação | Complexidade | Observação |
|----------|-------------|------------|
| Busca | O(log n) | Busca binária padrão |
| Inserção | O(log n) | Inclui tempo de rebalanceamento |
| Remoção | O(log n) | Inclui tempo de rebalanceamento |
| Espaço | O(n) | Armazenamento de n nós |

A altura máxima garantida é **2·log(n+1)**, o que assegura eficiência nas operações.

## Casos de balanceamento

### Inserção

Após inserir um nó vermelho, se o pai também é vermelho, ocorre violação da propriedade 4:

| Caso | Tio | Ação |
|------|-----|------|
| 1 | Vermelho | Recoloração do pai, tio e avô |
| 2 | Preto (linha) | Rotação simples + recoloração |
| 3 | Preto (triângulo) | Rotação dupla + recoloração |

### Remoção

Quando um nó preto é removido, pode violar a propriedade 5. Os casos dependem da cor do irmão e dos sobrinhos:

| Caso | Irmão | Sobrinhos | Ação |
|------|-------|-----------|------|
| 1 | Vermelho | - | Rotação + recoloração |
| 2 | Preto | Ambos pretos | Recoloração do irmão |
| 3 | Preto | Distante preto | Rotação no irmão + ajuste |
| 4 | Preto | Distante vermelho | Rotação + recoloração |

## Como executar

Requisitos: Python 3.8+

```bash
python index.py
```

O script demonstra:
- Sequência de inserções com visualização após cada operação
- Operações de busca (valores existentes e inexistentes)
- Remoções com rebalanceamento automático

Na visualização, `(P)` indica nó preto e `(V)` indica nó vermelho.

## Estrutura do código

```python
from index import RBArvore

# Criar árvore
arv = RBArvore()

# Inserir valores
arv.inserir(10)
arv.inserir(20)
arv.inserir(5)

# Buscar
resultado = arv.buscar(10)
if resultado:
    print(f"Encontrado: {resultado.valor}")

# Remover
arv.remover(20)

# Visualizar
arv.print_tree()
```

## Observações técnicas

- Implementação do zero, sem bibliotecas externas
- Utiliza nó sentinela (NIL) para simplificar casos de borda
- Todos os casos de correção estão implementados
- A remoção é mais complexa que a inserção devido ao maior número de casos

## Arquivos

- `index.py` - implementação das classes `RBNo` e `RBArvore`
- `README.md` - este arquivo
