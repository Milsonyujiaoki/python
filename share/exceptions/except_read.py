import os

# --- 1. Criação das Suas Próprias Exceptions Customizadas ---
class ArquivoNaoEncontradoError(Exception):
    """Lançada quando o arquivo não existe no diretório atual."""
    pass

class ConteudoInvalidoError(Exception):
    """Lançada quando o conteúdo do arquivo não atende aos critérios exigidos."""
    pass


# --- 2. Função Principal com o Fluxo de Tratamento ---
def laboratorio_excecoes():
    nome_arquivo = input("Digite o nome do arquivo que deseja procurar (ex: dados.txt): ").strip()
    
    try:
        print(f"\n🔹 [TRY] Iniciando a busca pelo arquivo: '{nome_arquivo}'")
        
        # Cenário de Erro 1: O arquivo não existe no diretório local
        if not os.path.exists(nome_arquivo):
            raise ArquivoNaoEncontradoError(f"O arquivo '{nome_arquivo}' não foi localizado na pasta atual.")
            
        # Tentativa de leitura segura do arquivo
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
        # Cenário de Erro 2: Conteúdo completamente vazio
        if not conteudo.strip():
            raise ConteudoInvalidoError("O arquivo existe, mas está totalmente vazio.")
            
        # Cenário de Erro 3: Critério arbitrário de validação de conteúdo
        # Vamos exigir que o arquivo contenha a palavra "Python"
        if "Python" not in conteudo:
            raise ConteudoInvalidoError("Conteúdo inválido: A palavra obrigatória 'Python' não foi encontrada.")
            
    # Capturando especificamente cada exceção criada
    except ArquivoNaoEncontradoError as erro:
        print(f"❌ [EXCEPT Customizado] Capturado: {erro}")
        
    except ConteudoInvalidoError as erro:
        print(f"❌ [EXCEPT Customizado] Capturado: {erro}")
        
    except Exception as erro_inesperado:
        print(f"⚠️ [EXCEPT Genérico] Um erro imprevisto aconteceu: {erro_inesperado}")
        
    # Executa se tudo deu certo no bloco 'try'
    else:
        print("✅ [ELSE] Sucesso total! Nenhuma exceção foi disparada.")
        print(f"📖 Conteúdo Lido com Sucesso:\n---\n{conteudo}\n---")
        
    # Executa sempre, sem exceção, servindo para limpeza de recursos
    finally:
        print("🧹 [FINALLY] O bloco finally foi executado. O ciclo de verificação foi encerrado com segurança.")

# Execução do laboratório
if __name__ == "__main__":
    laboratorio_excecoes()
