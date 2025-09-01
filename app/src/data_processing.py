import time
import random
import json
from datetime import datetime, timezone

def generate_mock_payload(machine_id="maquina_001", sensor_id="sensor_pressao_01"):
    """
    Gera um payload mockado simulando leituras de sensores.
    """
    sensor_data = {
        "pressao_bar": round(random.uniform(5, 9), 2),
        "temperatura_c": round(random.uniform(20, 30), 2),
        "consumo_w": round(random.uniform(2.5, 5.0), 2),
        "status_valvula": random.choice(["aberta", "fechada"]),
        "alerta": False
    }

    if sensor_data["pressao_bar"] > 8.5 or sensor_data["temperatura_c"] > 28:
        sensor_data["alerta"] = True

    payload = {
        "machine_id": machine_id,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        "properties": sensor_data
    }
    return payload

def serialize_payload(payload: dict) -> str:
    """
    Converte payload em JSON string.
    """
    return json.dumps(payload, ensure_ascii=False)
