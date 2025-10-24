import logging
import boto3
import os
import json
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

endpoint_url = os.environ.get('AWS_ENDPOINT_URL')

dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
s3 = boto3.client('s3', endpoint_url=endpoint_url)

TABLE_NAME = os.environ.get('TABLE_NAME')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    logger.info(f"Evento recebido: {json.dumps(event)}")
    try:
        # ROTA 1: Evento vindo do S3
        if 'Records' in event and 's3' in event['Records'][0]:
            logger.info("Processando evento do S3...")
            s3_event = event['Records'][0]['s3']
            bucket_name = s3_event['bucket']['name']
            object_key = s3_event['object']['key']
            
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            content = response['Body'].read().decode('utf-8')
            records = json.loads(content, parse_float=Decimal)

            with table.batch_writer() as batch:
                for record in records:
                    batch.put_item(Item=record)
            
            logger.info(f"Sucesso! {len(records)} registros inseridos via S3.")
            return {
                "statusCode": 200, 
                "body": json.dumps(f"{len(records)} registros inseridos com sucesso via S3.")
            }
        
        # ROTA 2: Evento vindo do API Gateway
        elif 'body' in event and event['body']:
            logger.info("Processando evento do API Gateway...")
            # O 'body' do API Gateway é uma string, então precisa ser convertido para JSON
            record = json.loads(event['body'], parse_float=Decimal)
            
            table.put_item(Item=record)
            
            logger.info("Sucesso! 1 registro inserido via API Gateway.")
            return {
                "statusCode": 201, # 201 Created é mais apropriado para POST
                "body": json.dumps("Registro criado com sucesso via API!")
            }

        # Se não for nenhum dos dois
        else:
            logger.warning("Tipo de evento não reconhecido.")
            return {"statusCode": 400, "body": json.dumps("Tipo de evento não suportado.")}

    except Exception as e:
        logger.error(f"Erro ao processar o evento: {str(e)}")
        return {"statusCode": 500, "body": json.dumps(f"Erro interno no servidor: {str(e)}")}