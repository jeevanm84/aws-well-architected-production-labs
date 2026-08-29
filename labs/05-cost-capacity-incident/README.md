# Lab 05 — cost and capacity incident

## Incident

Daily cost triples while latency and error rate rise. Leadership asks for immediate cost reduction without a reliability assessment.

```mermaid
flowchart LR
  Cost[Billing + unit cost] --> Correlate[Correlate timeline]
  Telemetry[Latency + errors + saturation] --> Correlate
  Changes[Deployments + configuration] --> Correlate
  Correlate --> Hypothesis[Retry / scaling / traffic hypotheses]
  Hypothesis --> Contain[Contain customer and cost impact]
  Contain --> Prevent[Permanent controls]
```

## Investigation

Run `python3 scripts/assess.py scenarios/05-cost-capacity-incident.json`, then determine:

- What changed at the anomaly start?
- Did traffic, retries, payload, log volume, data transfer or capacity change?
- What is cost per successful transaction?
- Which capacity is required for normal and failure conditions?
- Which mitigation is reversible and SLO-safe?

## Prevention

Implement accountable allocation, anomaly routing, retry budgets, measured scaling, lifecycle policies, unit-cost dashboards and periodic failover-capacity tests.
