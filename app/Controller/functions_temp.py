import C_shared
from Model.databaseModel import save_result
from inference_sdk import InferenceHTTPClient

def get_population_from_image(image_path: str) -> int:
    """Envia a imagem para a IA, conta os telhados, e retorna a estimativa de população."""
    client = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key=C_shared.ROBOFLOW_API_KEY
    )

    result = client.run_workflow(
        workspace_name="ian-martins-mendes",
        workflow_id="general-segmentation-api-6",
        images={
            "image": image_path  # Path recebido como argumento
        },
        parameters={"classes": "roof"},
        use_cache=True,  # cache workflow definition for 15 minutes
    )

    total_houses = len(result[0]["predictions"]["predictions"])
    population = total_houses * 3
    
    if C_shared.DEBUG:
        print(f"[DEBUG] Imagem: {image_path} | Casas: {total_houses} | População: {population}")

    return population

def get_searched_area(width_m: float) -> float:
    """Recebe a largura do mapa em metros e calcula a área total em km²."""
    # converte de metros para km e calcula a area do quadrado
    searched_area = (width_m * 0.001) ** 2
    
    if C_shared.DEBUG:
        print(f"[DEBUG] Largura do mapa: {width_m}m | Área pesquisada: {searched_area:.6f} km²")
        
    return searched_area

def get_population_density(population: int, searched_area: float) -> float:
    """Recebe a população estimada e a área (em km²) e cospe densidade populacional."""
    population_density = population / searched_area
    
    if C_shared.DEBUG:
        print(f"[DEBUG] População: {population} hab | Área: {searched_area:.6f} km² | Densidade: {population_density:.2f} hab/km²")
        
    return population_density

def process_and_save_vision_data(search_id: int, image_path: str, width_m: float) -> tuple:
    """Consulta a IA, calcula tudo que tem que calcular e salva os resultados no banco de dados."""
    if C_shared.DEBUG:
        print(f"\nIniciando processamento para o ID {search_id}...")

    population = get_population_from_image(image_path)
    searched_area = get_searched_area(width_m)
    population_density = get_population_density(population, searched_area)

    save_result(search_id, population, population_density)
    
    if C_shared.DEBUG:
        print("Fluxo de Visão Computacional e Banco de Dados finalizado com sucesso!\n")

    return population, searched_area, population_density