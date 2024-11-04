from confluent_kafka.admin import AdminClient

class KafkaAdminClient:
    def __init__(self, brokers: str, username: str, password: str ):
        self.brokers = brokers
        self.username = username
        self.password = password
    
    def __call__(self):
        try:
            client = AdminClient({
                "bootstrap.servers": self.brokers,
                "security.protocol": "SASL_SSL",
                "sasl.mechanisms": "PLAIN",
                "sasl.username": self.username,
                "sasl.password": self.password,
            })
            
            # Test the connection by listing topics
            client.list_topics(timeout=10)
            
            return client
        except Exception as e:
            raise RuntimeError(f"Failed to create AdminClient: {e}")   
