from models import DescribeTopicsRequest
from routers import topic
from services import KafkaAdminClient, describe_topics
from typing import Annotated
from fastapi import Depends, HTTPException


@topic.post("/describe", description="Get topics details.")
async def describe(request: DescribeTopicsRequest, kafka_admin_client: KafkaAdminClient = Depends(KafkaAdminClient)):
    try:
        result = await describe_topics(kafka_admin_client, [str(int(request.include_auth_ops))] + request.topics)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

