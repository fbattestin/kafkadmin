from pydantic import BaseModel
from typing import List

class TopicRequest(BaseModel):
    topics: List[str]

class DescribeTopicsRequest(BaseModel):
    include_auth_ops: bool = False
    topics: List[str]

class ListOffsetsRequest(BaseModel):
    isolation_level: str
    topic_partition_offsets: List[str]

class DeleteRecordsRequest(BaseModel):
    topic_partition_offsets: List[str]
