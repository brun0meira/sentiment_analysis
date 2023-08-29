# Biblioteca para representação em ASCII
from unidecode import unidecode

# Biblioteca para formatação de Regex
import re

# Biblioteca para computação científica
import numpy as np

# Biblioteca para funções matemáticas
import math

# Biblioteca para funções de PLN
import spacy
nlp = spacy.load('pt_core_news_sm')

# Biblioteca para carregar as variaveis de ambiente
import os
from dotenv import load_dotenv
load_dotenv()

# Biblioteca para envio do SMS
from twilio.rest import Client

def remove_accents(text: str) -> str:
    '''
    Função para remover acentos

    Parâmetros:
    -----------
      text: str
        Texto a ser tratado

    Retorno:
    --------
        text: str
          Texto tratado
    '''
    return unidecode(text)


def lowercase_text(text: str) -> str:
    '''
    Função para transformar em minúsculo

    Parâmetros:
    -----------
      text: str
        Texto a ser tratado

    Retorno:
    --------
        text: str
          Texto tratado
    '''
    return text.lower()


def remove_marks(text: str) -> str:
    '''
    Função para remover caracteres não alfanumericos

    Parâmetros:
    -----------
      text: str
        Texto a ser tratado

    Retorno:
    --------
        text: str
          Texto tratado
    '''
    return re.sub(r'[^\w\s]|_', '', text)

def stopWords(dados: list) -> list:
    '''
    Função para remover stop words

    Parâmetros:
    -----------
      dados: list
        Array a ser tratado

    Retorno:
    --------
        dados: list
          Array tratado
    '''
    resultado = [' '.join([token.text for token in nlp(texto) if not token.is_stop]) for texto in dados]
    saida = [token for token in resultado if token.strip()]
    return saida

def dictionary(array_st: list, array_nd: list ) -> list:
    '''
    Função para remover criar um dicionario entre dois arrays de palavras

    Parâmetros:
    -----------
      array_st: list
        Primeiro array
      array_nd: list
        Segundo array array 

    Retorno:
    --------
        dictionary: list
          Dicionarios das palavras da soma dos dois arrays 
    '''
    dictionary = set(array_st + array_nd)
    return dictionary

def cosine_similarity_with_negatives(text: list, negative_words:list) -> float:
    '''
    Função para calcular a similaridade do cosseno

    Parâmetros:
    -----------
      text: list
        Array com as palavras da primeiroa frase
      negative_words: list
        Array com as palavras negativas

    Retorno:
    --------
        text_similarity: float
          Similaridade do cosseno com a frase e as palavras negativas
    '''

    # Cria o dicionario das duas frases
    dictionary_frases = dictionary(text, negative_words)

    # Armazenar as ocorrencias das duas frases para cada palavra
    ocorrencia_frase_um = []
    ocorrencia_frase_dois = []

    # Calcula a ocorrencia do dicionario com a frase
    for palavra in dictionary_frases:
      ocorrencias = text.count(palavra)
      ocorrencia_frase_um.append(ocorrencias)

    # Calcula a ocorrencia do dicionario com as palavras negativas
    for palavra in dictionary_frases:
      ocorrencias = negative_words.count(palavra)
      ocorrencia_frase_dois.append(ocorrencias)

    # ocorrencia_frase_um = [1,0,1,1,1]
    # ocorrencia_frase_dois = [1,1,0,0,1]

    # Converta as listas em arrays NumPy
    ocorrencia_frase_um = np.array(ocorrencia_frase_um)
    ocorrencia_frase_dois = np.array(ocorrencia_frase_dois)

    # Realiza a soma dos produtos dos dois arrays de ocorrencias - A.B
    product_sum = np.sum(ocorrencia_frase_um * ocorrencia_frase_dois)


    # Calcula os quadrados de cada valor nos arrays
    squared_frase_um = np.square(ocorrencia_frase_um)
    squared_frase_dois = np.square(ocorrencia_frase_dois)

    # Soma os quadrados dos valores em cada array
    sum_of_squares_array1 = np.sum(squared_frase_um)
    sum_of_squares_array2 = np.sum(squared_frase_dois)

    # Calcula o módulo de A.B - |A|.|B|
    modulo = math.sqrt(sum_of_squares_array1) * math.sqrt(sum_of_squares_array2) 
    
    # Calcula a similaridade do cosseno - Cos(A.B)
    text_similarity = product_sum / modulo

    return text_similarity

def send_sms(text: str) -> str:
    '''
    Envio de email com alerta

    Parâmetros:
    -----------
      text: str
        Texto a ser enviado no sms

    Retorno:
    --------
      text: str
        Confirmação de envio
    '''
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=os.getenv('TWILIO_PHONE_NUMBER'),
                          to=os.getenv('CELL_PHONE_NUMBER'),
                          body=text)

    return 'SMS enviado com sucesso!'

def normalize_text(text: str) -> str:
    '''
    Pipeline de normalização do texto

    Parâmetros:
    -----------
      text: str
        Texto a ser tratado

    Retorno:
    --------
      text: str
        Texto tratado
    '''
    text = lowercase_text(text)
    text = remove_accents(text)
    text = remove_marks(text)
    return text


if __name__ == '__main__':
    # Definição da primeira frase (Negativa)
    frase_negativa = 'A reputação da IBM sofre um golpe à medida que alegações de práticas obscuras de privacidade, coleta não autorizada de dados e falta de transparência vêm à tona, levantando sérias preocupações sobre a ética corporativa e a confiança dos clientes na empresa.'

    # Definição da segunda frase (Positiva)
    frase_positiva = 'Os novos recursos de IA de hoje são mais um exemplo de como os avanços de ponta da IA provenientes de IBM Research nos ajudam a fornecer inovações em linguagem, automação e construção de confiança no IBM Watson que estão fazendo a diferença para empresas de todos os tamanhos e em todos os setores'

    # Definição da palavras negativas
    palavras_negativas = ['reputacao','sofre', 'golpe', 'alegacoes', 'obscuras','privacidade', 'falta','transparencia', 'preocupacoes', 'questionavel', 'nao','autorizada','dados', 'confianca', 'etica', 'clientes']

    # Tratamento das frases
    frase_negativa = normalize_text(frase_negativa)
    frase_positiva = normalize_text(frase_positiva)

    # Separando as palavras das frases
    array_frase_negativa = frase_negativa.split()
    array_frase_positiva = frase_positiva.split()

    # Remoção das stop words
    sw_negativa = stopWords(array_frase_negativa)
    sw_positiva = stopWords(array_frase_positiva)

    # Calcula a similaridade da primeira frase
    similaridade_frase_negativa = cosine_similarity_with_negatives(sw_negativa, palavras_negativas)
    print(f'Similaridade Negativa com a Frase 1: {similaridade_frase_negativa}')

    # Calcula a similaridade da segunda frase
    similaridade_frase_positiva = cosine_similarity_with_negatives(sw_positiva, palavras_negativas)
    print(f'Similaridade Negativa com a Frase 2: {similaridade_frase_positiva}')

    # Condições que verificam a similaridade e emitem um alerta
    if similaridade_frase_negativa >= 0.70 and similaridade_frase_positiva >= 0.70:
        send_sms(f'As duas frases são negativas, elas são - Frase 1: {frase_negativa} e Frase 2: {frase_positiva}')
    elif similaridade_frase_negativa >= 0.70:
        send_sms(f'A primeira frase é negativa, ela é: {frase_negativa}')
    elif similaridade_frase_positiva >= 0.70:
        send_sms(f'A segunda frase é negativa, ela é: {frase_positiva}')
    else:
        print("Nenhuma frase foi identificada como negativa")