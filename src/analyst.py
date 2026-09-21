"""Deterministic, evidence-based incident reasoning for safe demonstrations."""
def analyse(incident):
    metrics, logs = incident.get("metrics",{}), " ".join(incident.get("logs",[])).lower()
    evidence=[]; recommendations=[]; cause="Insufficient evidence for a specific cause."
    severity="SEV-3" if incident.get("alerts") else "SEV-4"
    latency=next((a for a in incident.get("alerts",[]) if a["name"]=="HighP95Latency"),None)
    if latency:
        evidence.append(f"p95 latency is {latency['value_ms']}ms against {latency['threshold_ms']}ms threshold")
        severity="SEV-2"
    if metrics.get("db_connection_utilization_percent",0) >= 90 and ("pool exhausted" in logs or "connection" in logs):
        cause="Database connection-pool saturation is the most probable contributor to checkout timeouts."
        evidence.append(f"database connection utilisation is {metrics['db_connection_utilization_percent']}%")
        evidence.append("application logs report database pool exhaustion")
        recommendations=[
            {"action":"Mitigate","text":"Use the approved runbook to reduce connection pressure or temporarily increase pool capacity within tested limits."},
            {"action":"Verify","text":"Confirm p95 latency, error rate, and database connection utilisation return below alert thresholds."},
            {"action":"Follow-up","text":"Review pool sizing, slow queries, and downstream connection lifecycle after stabilisation."}]
    return {"incident_id":incident.get("incident_id","unknown"),"service":incident.get("service","unknown"),"severity":severity,"confidence":"high" if len(evidence)>=2 else "low","observations":evidence,"probable_cause":cause,"recommendations":recommendations,"summary":f"{severity}: {incident.get('service','service')} is experiencing degraded behaviour. {cause}"}
