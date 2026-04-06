import os
import time
import json
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()
CLIENT_ID = os.getenv("MAL_CLIENT_ID")

BASE_URL = "https://api.myanimelist.net/v2"


def fetch_top_animes(total_target=15000, limit_per_request=500, starting_offset=0):
    """Busca animes do ranking geral e retorna uma lista formatada"""

    if not CLIENT_ID or CLIENT_ID == "cole_aqui_seu_client_id_gerado":
        raise ValueError("MAL_CLIENT_ID não configurado no .env")

    headers = {"X-MAL-CLIENT-ID": CLIENT_ID}

    extracted_data = []
    limit_per_request = min(
        total_target,
        limit_per_request,
        500,
    )

    # Salvar cada request como arquivo separado
    os.makedirs("data/raw", exist_ok=True)

    start_time = time.time()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[*] Inicio em {current_time}.")
    print(f"[*] Iniciando extração de {total_target} animes do MyAnimeList...")

    for offset in range(starting_offset, total_target, limit_per_request):
        batch_start = time.time()
        fields = "id,title,synopsis,start_season,mean,genres"
        url = (
            f"{BASE_URL}/anime/ranking?"
            f"ranking_type=all&"
            f"limit={limit_per_request}&"
            f"offset={offset}&"
            f"fields={fields}&"
            f"nsfw=false"
        )
        response = None

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            batch_data = []
            has_score = True
            for item in data.get("data", []):
                node = item["node"]
                anime_id = node.get("id")
                title = node.get("title")
                synopsis = node.get("synopsis", "")
                genres = node.get("genres") or []
                genre_names = [g.get("name") for g in genres if g.get("name")]
                year = node.get("start_season", {}).get("year")
                mean = node.get("mean", {})
                # Desprezamos animes sem sinopse
                if mean is None:
                    has_score = False
                    break
                if synopsis:
                    item_data = {
                        "id": anime_id,
                        "title": title,
                        "synopsis": synopsis,
                        "year": year,
                        "genres": genre_names,
                    }
                    extracted_data.append(item_data)
                    batch_data.append(item_data)

            batch_index = (offset // limit_per_request) + 1
            out_path = f"data/raw/animes-{batch_index:04d}.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(batch_data, f, ensure_ascii=False, indent=2)
            print(
                f" -> Lote {offset} a {offset+limit_per_request} concluído. Total até agora: {len(extracted_data)}"
            )
            paging = data.get("paging")
            next = paging["next"]
            next_page = (data.get("paging") or {}).get("next")

            if not next_page or not has_score or len(extracted_data) >= total_target:
                print("[INFO] Fim dos requests...")
                break
            batch_elapsed = time.time() - batch_start
            total_elapsed = time.time() - start_time
            print(
                f"[*] Tempo decorrido: {batch_elapsed:.2f}s (total: {total_elapsed:.2f}s). Aguardando 15s..."
                # Pausa educada para não tomar Block (Rate limit)
            )
            time.sleep(15)

        except requests.exceptions.RequestException as e:
            print(f"[!] Erro ao acessar a API: {e}")
            if response is not None:
                for k, v in response.headers.items():
                    print(f"{k}: {v}")
            break

    total_elapsed = time.time() - start_time
    print(
        f"[*] Fim da Extração! {len(extracted_data)} animes salvos em data/raw/animes-XXX.json."
    )
    print(f"[*] Tempo total: {total_elapsed:.2f}s.")


if __name__ == "__main__":
    # Teste rápido de 100 itens para verificar
    fetch_top_animes()
