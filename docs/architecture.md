# Architecture

`simulated alert/metric/log payload → deterministic evidence rules → incident brief → optional LLM enrichment → terminal or JSON output`.

The deterministic engine owns severity, evidence, cause hypothesis, and recommended verification. The LLM adapter may add a text enrichment only; it is optional, fault-tolerant, and cannot perform actions.
