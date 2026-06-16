import Model.databaseModel as db

def run_tests():
    print("🔧 Iniciando testes do Banco de Dados...\n")
    
    # 1. Cria o banco de dados e a tabela (se não existirem)
    print("-> Configurando o banco de dados (search_history.db)...")
    db.setup_db()
    
    # 2. Inserindo dados falsos (Simulando o Controller após processar as imagens)
    print("-> Salvando 3 pesquisas de teste...")
    db.save_search("08/11/2002 12h 00m 00s", -28.9333, -49.4833) 
    db.save_search("08/11/2002 23h 59m 59s", -28.9500, -49.5000)
    db.save_search("23/10/1953 23h 59m 59s", -23.5505, -46.6333) 
    
    # 3. Testando a busca (Simulando o usuário digitando uma data e clicando em pesquisar)
    termo_pesquisa = "08/11/2002"
    print(f"-> Buscando no histórico pelo termo: '{termo_pesquisa}'...\n")
    
    resultados = db.find_search_by_term(termo_pesquisa)
    
    # 4. Exibindo os resultados na tela
    print("✅ Resultados encontrados no banco:")
    if resultados:
        for res in resultados:
            print(f"  - {res}")
    else:
        print("  Nenhum resultado encontrado.")
        
    print("\n🚀 Teste finalizado com sucesso!")

if __name__ == "__main__":
    run_tests()