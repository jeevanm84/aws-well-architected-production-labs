# AWS architecture interview questions

## Fundamentals

1. What are the six AWS Well-Architected pillars?
2. Compare Region, Availability Zone, VPC, subnet and account as boundaries.
3. What makes a requirement measurable?
4. Compare RTO, RPO, availability target and durability.
5. Why is an architecture diagram insufficient evidence of reliability?

## Intermediate

1. Design a two-AZ web application and identify every remaining single dependency.
2. Compare SQS retries, DLQ, idempotency and ordering concerns.
3. How do private instances receive administrative and AWS API access?
4. How do you prove backup restoration meets RTO/RPO?
5. Compare cost per hour with cost per successful business transaction.

## Advanced

1. Compare backup/restore, pilot light, warm standby and active/active DR.
2. Design multi-account identity, log archive and security tooling boundaries.
3. How do service quotas affect both normal scaling and disaster recovery?
4. When can multi-AZ architecture increase cross-AZ dependency or transfer cost?
5. How do you choose synchronous versus asynchronous integration?

## Production and senior engineer

1. A managed service fails. Which operational responsibilities remain yours?
2. A design meets availability but exceeds budget. How do you preserve non-negotiable outcomes while evaluating alternatives?
3. How do you design game days that are safe but still invalidate assumptions?
4. How do you move from a one-time Well-Architected review to continuous improvement?
5. How do you communicate architecture risk to business owners without hiding uncertainty?

## Architect and SRE scenarios

### Regional outage

The primary Region is unavailable and replication lag is 22 minutes against a 15-minute RPO. Explain decision authority, data choice, customer communication, recovery validation, reconciliation and follow-up.

### Identity outage

Federated workforce login fails during a production incident. Explain break-glass controls, monitoring, audit evidence, privilege duration and post-incident rotation.

### Cost anomaly

Daily spend triples while latency rises. Explain evidence collection, customer-impact protection, retry/scaling analysis, containment, unit-cost calculation and prevention.

## Answer framework

```text
Business requirement → Architecture options → Decision and trade-off
→ Failure behavior → Evidence → Recovery → Cost → Revisit trigger
```
