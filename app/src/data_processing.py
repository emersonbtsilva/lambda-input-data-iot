import time
import random
import json

def generate_mock_payload(machine_id="maquina_001", sensor_id="sensor_pressao_01"):
    """
    Gera um payload mockado simulando leituras de sensores.
    """
    payload = {
        "machine_id": machine_id,
        "sensor_id": sensor_id,
        "timestamp": int(time.time()),
        "pressao_bar": round(random.uniform(5, 9), 2),
        "temperatura_c": round(random.uniform(20, 30), 2),
        "consumo_w": round(random.uniform(2.5, 5.0), 2),
        "status_valvula": random.choice(["aberta", "fechada"]),
        "alerta": False
    }

    # Regras de alerta simples
    if payload["pressao_bar"] > 8.5 or payload["temperatura_c"] > 28:
        payload["alerta"] = True

    return payload

def serialize_payload(payload: dict) -> str:
    """
    Converte payload em JSON string.
    """
    return json.dumps(payload, ensure_ascii=False)
