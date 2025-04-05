"""Exemplo de implementação de um Trie em Python (autocomplete)"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False # Verifica se o nó é o final de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode() # Primeiro nó

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode() # Cria um novo nó se o caractere não existir. O caractere é a chave e o novo nó, o valor
            current_node = current_node.children[char] # Atualiza o nó atual para o próximo caractere
        current_node.is_end_of_word = True
    
    def search(self, word):
        current_node = self.root
        for char in word: # Para cada letra da palavra, verifica se existe correspondênca nos nós filhos. Se não houver correspondência em qualquer momento, retorna False
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word # O último nó com correspondência precisa, necessariamente, ser o final da palavra

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in prefix:
                return False
            current_node = current_node.children[char]
        return True

"""Implementação do Trie"""
if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("banana")
    trie.insert("app")
    trie.insert("orange")

    print(trie.starts_with("ap")) # True