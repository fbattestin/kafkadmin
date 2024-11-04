from fastapi import APIRouter, Depends
from services import KafkaAdminClient

topic = APIRouter(
        prefix="/v1/topic",
        tags=["topic"],
        responses={404: {"description": "Not found"}},
        # dependencies=[Depends(KafkaAdminClient)],
)

