from confluent_kafka.admin import AdminClient, KafkaException
from confluent_kafka import TopicCollection
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def describe_topics(a: AdminClient, args: list[str]) -> None:
    """
    Describe topics in the Kafka cluster.

    Args:
        a (AdminClient): The Kafka AdminClient instance.
        args (list[str]): List of arguments where the first element is a flag for including authorized operations and the rest are topic names.
    """
    logging.info(f"Describing topics with args: {args}")
    include_auth_ops = bool(int(args[0]))
    args = args[1:]
    topics = TopicCollection(topic_names=args)
    results = {topic: {'partitions': []} for topic in args}
    try:
        futureMap = a.describe_topics(topics, request_timeout=10, include_authorized_operations=include_auth_ops)
    except Exception as e:
        logging.error(f"Failed to describe topics: {e}")
        raise RuntimeError(f"Failed to describe topics: {e}")
    
    for topic_name, future in futureMap.items():
        try:
            t = future.result()
            logging.info(f"Topic name: {t.name}")
            logging.info(f"Topic id: {t.topic_id}")
            if t.is_internal:
                logging.info("Topic is Internal")

            if include_auth_ops:
                logging.info("Authorized operations:")
                op_string = "  ".join(acl_op.name for acl_op in t.authorized_operations)
                logging.info(f"    {op_string}")

            logging.info("Partition Information")
            for partition in t.partitions:
                partition_info = {
                    'id': partition.id,
                    'leader': partition.leader,
                    'replicas': [replica for replica in partition.replicas],
                    'in_sync_replicas': [isr for isr in partition.isr]
                }
                results[topic_name]['partitions'].append(partition_info)

        except KafkaException as e:
            logging.error(f"Error while describing topic '{topic_name}': {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise RuntimeError(f"Unexpected error: {e}")

    return {'status': 'success', 'message': results}
