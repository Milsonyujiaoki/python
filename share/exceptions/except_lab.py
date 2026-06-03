import os
import logging

# Configuração básica do sistema de Logs profissionais do Python
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Seus Exceptions Customizados ---
class ArquivoNaoEncontradoError(Exception):
    pass

class ConteudoInvalidoError(Exception):
    pass


# --- Função Auxiliar Avançada ---
def ler_e_validar_arquivo(nome_arquivo):
    """Função focada apenas em ler o arquivo e validar a regra de negócio."""
    try:
        if not os.path.exists(nome_arquivo):
            raise ArquivoNaoEncontradoError(f"Arquivo '{nome_arquivo}' sumiu ou não existe.")
            
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
        if "Python" not in conteudo:
            raise ConteudoInvalidoError("A palavra obrigatória 'Python' não foi encontrada.")
            
        return conteudo

    except ConteudoInvalidoError as erro_conteudo:
        # Prática do RE-RAISE: Interceptamos o erro para colocar um aviso decorativo, 
        # mas usamos o 'raise' puro para repassar a falha adiante para a função principal.
        print("⚠️ [INTERCEPTADO] Um erro de validação aconteceu! Preparando para relançar...")
        raise  # <--- Isso joga o exato mesmo erro para fora da função


# --- Função Principal (Laboratório Avançado) ---
def laboratorio_avancado():
    nome_arquivo = input("Digite o nome do arquivo para o teste avançado: ").strip()
    
    try:
        print(f"\n🔹 [TRY] Tentando processar: '{nome_arquivo}'")
        conteudo_valido = ler_e_validar_arquivo(nome_arquivo)
        
    # Exemplo 1: Capturando nossa exceção customizada que foi relançada
    except ConteudoInvalidoError as erro:
        print(f"❌ [EXCEPT] Capturado na camada principal: {erro}")

    # Exemplo 2: Agrupando erros comuns em uma tupla para o mesmo tratamento
    # Se o usuário passar um número em vez de texto ou houver problemas de permissão (PermissionError)
    except (TypeError, PermissionError, ArquivoNaoEncontradoError) as erro_sistema:
        print(f"❌ [EXCEPT AGRUPADO] Tratando falha crítica de sistema/tipo: {erro_sistema}")
        
    # Exemplo 3: O bloco genérico 'Fallback' usando LOGGING em vez de print
    except Exception as erro_inesperado:
        # Se acontecer qualquer bizarro (ex: falta de memória), guardamos o log profissional com o Traceback
        print("⚠️ [EXCEPT GENÉRICO] Algo totalmente imprevisto ocorreu. Verifique a linha de Log abaixo:")
        logging.exception(erro_inesperado) # <--- Prática recomendada em ambiente de produção
        
    else:
        print("✅ [ELSE] Nenhuma exceção ocorreu! Arquivo processado com absoluto sucesso.")
        print(f"📖 Conteúdo:\n{conteudo_valido}")
        
    finally:
        # O oposto do else, executa não importa o que aconteça
        print("🧹 [FINALLY] Recursos finalizados com sucesso e laboratório encerrado.")

if __name__ == "__main__":
    laboratorio_avancado()
