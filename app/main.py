from typing import Annotated
from fastapi import Depends, FastAPI
# from controller.v1.routers import topic
from v1.topic import topic

app = FastAPI()

app.include_router(topic)   
# app.include_router(topic, dependencies=[Depends(KafkaAdminClient)])  # works too