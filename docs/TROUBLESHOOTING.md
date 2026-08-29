# Architecture troubleshooting handbook

## Incident — healthy infrastructure, failed customer journey

**Symptoms:** Instance and load-balancer metrics look healthy, but checkout fails.

**Investigation:** Trace the business transaction across edge, application, identity, data, messaging and third-party dependencies. Use synthetic transaction, distributed traces, dependency latency/errors and change events.

**Root cause pattern:** Component-health dashboards do not represent the end-to-end SLI.

**Permanent fix:** Define customer-journey SLIs and correlate component evidence to them.

## Incident — multi-AZ design still fails during one AZ impairment

**Investigation:** Check actual replica placement, zonal dependencies, cross-AZ routing, NAT, database mode, capacity headroom, storage topology and autoscaling delay.

**Root cause pattern:** Resources span AZs but a dependency or capacity assumption remains zonal.

**Prevention:** AZ-aware diagrams, quota/capacity review and regular evacuation exercises.

## Incident — backup exists but restore misses RTO

**Investigation:** Measure discovery, approval, data retrieval, restore, infrastructure creation, secret/key access, application reconciliation, validation and traffic cutover separately.

**Permanent fix:** Automate the slowest steps and test the complete recovery path, including data correctness and failback.

## Incident — retry storm increases both cost and errors

Inspect retry count, amplification, timeout hierarchy, jitter, queues, concurrency, downstream throttling and circuit-breaker state. Contain load without discarding durable work.

Prevent through retry budgets, idempotency, backpressure and failure-load testing.

## Incident — security findings are generated but not handled

Check finding ownership, severity mapping, routing, notification health, evidence access, response authority and closure verification. Detection without response is an incomplete control.

## Incident — cost optimization breaks reliability

If a change removed failover headroom, rollback to the last tested reliability floor. Recalculate unit cost and capacity from agreed SLOs rather than minimizing the bill in isolation.

## Incident — architecture review produces hundreds of findings

Group findings by customer/business impact and systemic root cause. Prioritize high-risk, low-detection and untested-recovery gaps. Assign owners and evidence-based completion criteria.
