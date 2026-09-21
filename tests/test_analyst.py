import unittest
from src.analyst import analyse
class AnalystTests(unittest.TestCase):
    def test_pool_saturation_reasoning(self):
        incident={"incident_id":"x","service":"api","alerts":[{"name":"HighP95Latency","value_ms":1000,"threshold_ms":500}],"metrics":{"db_connection_utilization_percent":98},"logs":["pool exhausted"]}
        result=analyse(incident);self.assertEqual(result["severity"],"SEV-2");self.assertIn("connection-pool",result["probable_cause"]);self.assertEqual(result["confidence"],"high")
if __name__=="__main__":unittest.main()
