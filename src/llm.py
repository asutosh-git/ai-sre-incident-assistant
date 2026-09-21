import os
def enrich(incident, deterministic, model="gpt-5"):
    """Optional text enrichment. Fail closed to deterministic analysis, never execute suggestions."""
    if not os.getenv("OPENAI_API_KEY"):
        return deterministic, "local-fallback:no-api-key"
    try:
        from openai import OpenAI
        prompt = "Summarize this simulated incident for an SRE. Give advisory-only observations and verification steps. Do not invent evidence.\\n" + str(incident)
        response=OpenAI().responses.create(model=model,input=prompt)
        result=dict(deterministic); result["llm_enrichment"]=response.output_text
        return result, "openai"
    except Exception as exc:
        return deterministic, f"local-fallback:{type(exc).__name__}"
