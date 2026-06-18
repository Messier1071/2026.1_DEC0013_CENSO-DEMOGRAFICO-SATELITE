import os
import Model.databaseModel as db

def run_full_tests():
    print("🚀 INICIANDO BATERIA DE TESTES COMPLETOS (CRUD + RELACIONAMENTOS)...\n")

    # 0. Limpeza do ambiente (Garante que o teste comece do zero)
    if os.path.exists(db.DB_NAME):
        os.remove(db.DB_NAME)
        print("🗑️  Banco de dados anterior removido para um teste limpo.")

    # 1. SETUP
    print("\n-> 1. Configurando o banco de dados...")
    db.setup_db()
    print("✅ Tabelas criadas com sucesso!")

    # 2. CREATE
    print("\n-> 2. Inserindo dados (CREATE)...")
    id_1 = db.save_search("10/01/2026 - Centro", -28.1, -49.1, -28.2, -49.2)
    db.save_result(id_1, 10500, 150.2)
    
    id_2 = db.save_search("15/01/2026 - Bairro", -28.3, -49.3, -28.4, -49.4)
    db.save_result(id_2, 3200, 50.5)
    
    id_cobaia = db.save_search("Teste para Deletar", -28.5, -49.5, -28.6, -49.6)
    db.save_result(id_cobaia, 999, 9.9)
    print("✅ 3 pesquisas e 3 resultados inseridos perfeitamente!")

    # 3. READ (Get All)
    print("\n-> 3. Testando Busca Geral (get_all_history)...")
    historico = db.get_all_history()
    if len(historico) == 3:
        print(f"✅ Histórico completo carregado! ({len(historico)} itens encontrados)")
    else:
        print("❌ FALHA: Número incorreto de itens no histórico.")

    # 4. READ (Search by Term)
    print("\n-> 4. Testando Busca por Termo (get_search_by_term)...")
    busca_centro = db.get_search_by_term("Centro")
    if len(busca_centro) == 1 and busca_centro[0] == "10/01/2026 - Centro":
        print("✅ Busca por termo 'Centro' funcionou perfeitamente!")
    else:
        print("❌ FALHA: A busca por termo não retornou o resultado esperado.")

    # 5. READ (Result by ID)
    print("\n-> 5. Testando Busca de Resultado (get_result_by_id)...")
    resultado_2 = db.get_result_by_id(id_2)
    resultado_fantasma = db.get_result_by_id(9999)
    
    if resultado_2 == (3200, 50.5) and resultado_fantasma is None:
        print("✅ Busca de população e densidade por ID (Caminho Feliz e Triste) passou!")
    else:
        print("❌ FALHA: O retorno da busca unitária está incorreto.")

    # 6. DELETE (Cascade)
    print("\n-> 6. Testando Delete em Cascata (delete_search)...")
    db.delete_search(id_cobaia)
    
    # Prova real do delete
    historico_pos_delete = db.get_all_history()
    resultado_apagado = db.get_result_by_id(id_cobaia)
    
    if len(historico_pos_delete) == 2 and resultado_apagado is None:
        print("✅ Deleção e Cascade funcionaram! A cobaia foi erradicada de ambas as tabelas.")
    else:
        print("❌ FALHA: O Cascade falhou. Dados da cobaia ainda existem no banco.")

    print("\n🎉🏆 TODOS OS TESTES PASSARAM COM LOUVOR! O SEU MODEL ESTÁ BLINDADO! 🏆🎉\n")

if __name__ == "__main__":
    run_full_tests()