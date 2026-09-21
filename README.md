# AI SRE Incident Assistant

A safe incident-analysis assistant that correlates simulated alerts, metrics, and logs into an actionable incident brief. It defaults to deterministic local reasoning so the complete demo works without network access, credentials, or an LLM.

## Demo

```bash
python -m src.cli --incident data/checkout_latency.json
python -m unittest discover -s tests -v
```

The fixture simulates a checkout API latency incident associated with database connection saturation. The assistant produces severity, confidence, observations, probable cause, immediate mitigations, verification steps, and an incident summary.

## Optional OpenAI enrichment

Set `OPENAI_API_KEY` and install `openai`, then pass `--mode openai`. The program sends only the provided incident payload to the configured Responses API client. The deterministic reasoning result remains the safe fallback if the key, package, or API call is unavailable.

```bash
pip install -r requirements.txt
OPENAI_API_KEY=... python -m src.cli --incident data/checkout_latency.json --mode openai
```

The optional adapter follows the [official OpenAI Responses API quickstart](https://developers.openai.com/api/docs/quickstart?site_locale=en). Do not send customer data, secrets, access tokens, or unredacted production logs to an external model without approved controls.

## Design principles

- advisory only: never changes infrastructure or executes remediation
- deterministic mode for repeatable demos and tests
- evidence-first output; recommendations distinguish mitigation from verification
- provider abstraction so model choice is an implementation detail
- public-safe sample data only

## Structure

`src/` CLI, analyst, and LLM adapter · `data/` fictional incident fixtures · `docs/` architecture/runbook guidance · `tests/` regression tests.

## License

MIT
