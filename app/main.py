import Model.databaseModel as db

def run_tests():
    print("🔧 Iniciando testes do Banco de Dados...\n")
    
    # 1. Configura o banco zerado
    print("-> Configurando o banco de dados (search_history.db)...")
    db.setup_db()
    
    # 2. Inserindo dados com os 4 pontos (TL e BR)
    print("-> Salvando pesquisas de teste com quinas TL e BR...")
    db.save_search(
        slug="08/11/2002 12h 00m 00s", 
        lat_tl=-28.9333, lon_tl=-49.4833, 
        lat_br=-28.9400, lon_br=-49.4700
    )
    db.save_search(
        slug="08/11/2002 23h 59m 59s", 
        lat_tl=-28.9500, lon_tl=-49.5000, 
        lat_br=-28.9600, lon_br=-49.4900
    )
    db.save_search(
        slug="23/10/1953 23h 59m 59s", 
        lat_tl=-23.5505, lon_tl=-46.6333, 
        lat_br=-23.5600, lon_br=-46.6200
    )
    
    # 3. Testando a busca por termo (Data)
    termo_pesquisa = "08/11/2002"
    print(f"\n-> Buscando no histórico pelo termo: '{termo_pesquisa}'...")
    resultados_termo = db.find_search_by_term(termo_pesquisa)
    if resultados_termo:
        for res in resultados_termo:
            print(f"  - {res}")
            
    # 4. Testando a busca de TODO o histórico (Missão 2)
    print("\n-> Buscando TODO o histórico do banco...")
    todo_historico = db.get_all_history()
    
    print("✅ Histórico Completo:")
    if todo_historico:
        for linha in todo_historico:
            print(f"  - {linha}")
    else:
        print("  O banco está vazio.")
        
    print("\n🚀 Testes finalizados com sucesso!")

if __name__ == "__main__":
    run_tests()