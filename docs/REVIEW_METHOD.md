# Architecture review method

## Phase 1 — workload context

Identify owners, customers, critical journeys, data, dependencies, compliance, deployment cadence, support model, lifecycle stage and business impact.

## Phase 2 — measurable requirements

Define SLOs, latency/throughput, scale, RTO/RPO, security classifications, budget, unit economics and sustainability constraints.

## Phase 3 — architecture and trust boundaries

Map ingress, identity, compute, data, messaging, administrative access, telemetry, third parties and recovery. Mark account, Region, AZ, VPC, subnet and encryption boundaries.

## Phase 4 — pillar review

### Operational excellence

- Who owns the workload, runbooks, alerts and improvements?
- Are changes small, reversible and observable?
- Which game days prove operational assumptions?

### Security

- How are human, workload and service identities controlled?
- How are prevention, detection, response and evidence separated?
- How are data and infrastructure protected throughout their lifecycle?

### Reliability

- What quotas, failure domains and dependencies constrain recovery?
- Which components recover automatically, and which require decisions?
- When were backups, failover and failback last tested?

### Performance efficiency

- What workload characteristics drove service selection?
- Where does saturation appear, and how is it measured?
- How will architecture evolve when access patterns change?

### Cost optimization

- Who owns spend and unit cost?
- How is supply matched to demand without violating reliability?
- Which resources/data persist without current business value?

### Sustainability

- How is idle work reduced and demand alignment improved?
- Are software, data and hardware choices efficient for the requirement?
- What lifecycle and managed-service choices reduce unnecessary resource use?

## Phase 5 — failure analysis

For every credible failure:

```text
Incident → Customer impact → Detection → Containment
→ Recovery → Data reconciliation → Prevention → Exercise
```

## Phase 6 — decisions and backlog

Record decision, rejected alternatives, trade-off, evidence and revisit trigger. Prioritize improvements, assign owners and define verification.

## Review anti-patterns

- Selecting services before requirements
- Calling a system multi-AZ because subnets exist in two AZs
- Treating backup creation as proof of recovery
- Assuming managed means operationally automatic
- Trading away security or operability silently to reduce cost
- Listing metrics without SLOs, owners or response actions
- Using current spend instead of cost per useful outcome
