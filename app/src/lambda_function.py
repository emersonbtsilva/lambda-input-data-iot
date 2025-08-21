import boto3
from app.src import data_processing

# Cliente do IoT Core (data-plane)
client = boto3.client("iot-data", region_name="us-east-1")  # ajuste a região

def lambda_handler(event, context):
    """
    Função Lambda que gera dados mockados e publica no IoT Core.
    
    event esperado (pode ser vazio):
    {
        "machine_id": "maquina_001",
        "sensor_id": "sensor_pressao_01"
    }
    """
    
    machine_id = event.get("machine_id", "maquina_001")
    sensor_id  = event.get("sensor_id", "sensor_pressao_01")
    
    
    payload = data_processing.generate_mock_payload(
        machine_id=machine_id,
        sensor_id=sensor_id
    )
    
    # Publica no IoT Core
    client.publish(
        topic="maquina/sensores",
        qos=1,
        payload=data_processing.serialize_payload(payload)
    )
    
    print("Publicado:", payload)
    
    return {
        "statusCode": 200,
        "body": payload
    }
