import os
import streamlit as st

# Clases y funciones del trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_end_of_word = True

    def _search_anagrams(self, node, available_letters, prefix, anagrams):
        if node.is_end_of_word:
            anagrams.add(prefix)
        
        for letter, count in available_letters.items():
            if count > 0 and letter in node.children:
                available_letters[letter] -= 1
                self._search_anagrams(node.children[letter], available_letters, prefix + letter, anagrams)
                available_letters[letter] += 1

    def search_anagrams(self, input_word):
        available_letters = {}
        for letter in input_word:
            if letter in available_letters:
                available_letters[letter] += 1
            else:
                available_letters[letter] = 1

        anagrams = set()
        self._search_anagrams(self.root, available_letters, "", anagrams)
        return anagrams

def cargar_diccionario(path, trie):
    for letra in "abcdefghijklmnñopqrstuvwxyz":
        with open(os.path.join(path, f"{letra}.txt"), encoding="utf-8") as archivo:
            palabras = archivo.read().splitlines()
            for palabra in palabras:
                trie.insert(palabra.lower())

# Configuración de la aplicación Streamlit
st.set_page_config(
    page_title="Generador de Anagramas",
    page_icon=":book:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Cargar el diccionario
# Reemplaza esto con la ruta a tu carpeta de archivos del diccionario
path = dict_rae_txt/dics 
trie = Trie()
cargar_diccionario(path, trie)

# Interfaz de usuario
st.title("Generador de Anagramas")
palabras = st.text_input("Introduce una o varias palabras:")

if palabras:
    anagramas = trie.search_anagrams(palabras)
    st.subheader(f"Se han encontrado {len(anagramas)} anagramas:")
    st.write(", ".join(sorted(anagramas)))
else:
    st.write("Por favor, ingrese una o varias palabras para generar anagramas.")
