import os
import logging

# Configuração de logs para produção
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Hierarquia de Exceções Customizadas ---
class BaseLaboratorioError(Exception):
    """Classe base para todas as exceções do nosso sistema."""
    pass

class ArquivoInacessivelError(BaseLaboratorioError):
    """Lançada para falhas críticas de IO, existência ou permissão."""
    pass

class DadoCorrompidoError(BaseLaboratorioError):
    """Lançada quando a validação ou conversão de tipos internos falha."""
    pass


# --- Mecanismo de Processamento usando Built-ins ---
def processar_metricas_arquivo(nome_arquivo, callback_sucesso=None):
    """
    Abre um arquivo, converte linhas de dados para inteiros e executa um callback.
    Demonstra o uso prático de open(), isinstance(), int() e callable().
    """
    # Garantindo integridade de tipos com isinstance (Estilo defensivo)
    if not isinstance(nome_arquivo, str):
        raise TypeError("O parâmetro nome_arquivo precisa ser uma string estrita.")

    try:
        # open() gerenciando contexto com 'with' para garantir cleanup automático
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
        resultados = []
        for i, linha in enumerate(linhas, start=1):
            texto = linha.strip()
            if not texto:  # Ignora linhas em branco vazias
                continue
                
            try:
                # int() agindo como validador estrito de dados
                numero = int(texto)
                resultados.append(numero)
            except ValueError as erro_original:
                # RE-RAISE ENRIQUECIDO: Relançamos com contexto sem perder a causa raiz
                raise DadoCorrompidoError(
                    f"Falha na linha {i}: O valor '{texto}' não pôde ser convertido."
                ) from erro_original
                
        # Execução dinâmica segura usando a built-in callable()
        if callback_sucesso and callable(callback_sucesso):
            callback_sucesso(resultados)
            
        return resultados

    except (FileNotFoundError, PermissionError) as erro_sistema:
        # Encapsula exceções nativas do sistema operacional na nossa exceção customizada
        raise ArquivoInacessivelError(f"Erro ao acessar o arquivo '{nome_arquivo}': {erro_sistema}") from erro_sistema


# --- Fluxo de Execução e Diagnóstico ---
def executar_laboratorio():
    arquivo_teste = "dados_experimento.txt"
    
    # Criando arquivo de simulação contendo um erro proposital na linha 3
    with open(arquivo_teste, "w", encoding="utf-8") as f:
        f.write("142\n583\nTextoInvalido\n921")

    print(f"🔹 [Início] Analisando o arquivo gerado: {arquivo_teste}")
    
    try:
        # Passando uma função lambda (que é um callable válido) para processar o sucesso
        processar_metricas_arquivo(arquivo_teste, callback_sucesso=lambda dados: print(f"Soma total: {sum(dados)}"))
        
    except BaseLaboratorioError as erro_sistema:
        print(f"\n❌ [EXCEPT] Capturado erro mapeado do laboratório: {erro_sistema}")
        
        # Validando o tipo específico de erro via polimorfismo com isinstance()
        if isinstance(erro_sistema, DadoCorrompidoError):
            print(f"🔬 [Diagnóstico] Causa original identificada: {erro_sistema.__cause__}")
            
            # 💡 EXPERIMENTO DE DEPURAÇÃO: Descomente a linha abaixo para pausar o script 
            # no terminal e usar a built-in `locals()` para inspecionar as variáveis vivas!
            # breakpoint() 
            
    except Exception as erro_inesperado:
        print("⚠️ [CRÍTICO] Uma falha não mapeada ocorreu.")
        logging.exception(erro_inesperado)
        
    else:
        print("✅ [ELSE] Leitura e processamento concluídos sem nenhuma exceção.")
        
    finally:
        # Garantindo a limpeza do ambiente local
        if os.path.exists(arquivo_teste):
            os.remove(arquivo_teste)
            print("🧹 [FINALLY] Arquivo de teste temporário removido com sucesso do diretório.")

if __name__ == "__main__":
    executar_laboratorio()
