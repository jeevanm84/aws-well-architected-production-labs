# End-to-end architecture review guide

This path requires no AWS account. It teaches the review method first, then applies it to five production scenarios.

## 1. Validate the evidence system

```bash
git clone https://github.com/jeevanm84/aws-well-architected-production-labs.git
cd aws-well-architected-production-labs
./scripts/check.sh
```

Expected result: five structured assessments and the queue reliability simulator pass without credentials or network access.

## 2. Start from requirements

Choose a lab and write measurable requirements before selecting AWS services:

- Business outcome and critical user journey
- Availability/SLO target
- RTO and RPO
- Data classification and compliance constraints
- Traffic shape and growth assumption
- Operational ownership and support hours
- Budget and unit-cost goal

Avoid claims such as “highly available” or “secure” without measurable acceptance criteria.

## 3. Draw boundaries and flows

Document actors, trust boundaries, data stores, synchronous and asynchronous dependencies, failure domains, administrative paths, telemetry, and recovery paths.

Checkpoint: every arrow has a protocol/identity expectation, and every stateful component has ownership and recovery requirements.

## 4. Record decisions and trade-offs

Use:

```text
Requirement → Options → Decision → Trade-off
→ Failure mode → Evidence → Revisit trigger
```

Run a scenario assessment:

```bash
python3 scripts/assess.py scenarios/01-ha-web.json
```

The validator rejects missing pillars, failure response, evidence, cost controls, or decision revisit conditions.

## 5. Review all six pillars

For each pillar, require both decisions and evidence. A design statement without a verification method is an assumption.

Use [Review Method](REVIEW_METHOD.md) for the complete question sequence.

## 6. Exercise failure behavior

For the event-driven lab:

```bash
python3 simulators/queue_delivery.py
python3 tests/test_queue_delivery.py
```

Observe successful processing, transient retry recovery, duplicate suppression, and poison-message dead-letter handling. Then explain the limitations of this deterministic simulation compared with real SQS/Lambda behavior.

For other labs, conduct tabletop or sandbox game days using the listed failure modes. Do not test against an unauthorized or production account.

## 7. Build an improvement backlog

Prioritize findings using business impact, likelihood, detection gap, recovery gap, effort and dependency. Assign an owner and verification condition. Avoid a flat list of best practices with no workload context.

## 8. Connect design to implementation

Use the architecture outcomes to drive:

- [Terraform AWS HA Web Platform](https://github.com/jeevanm84/terraform-aws-ha-web-platform)
- [Packer AWS Golden Image Pipeline](https://github.com/jeevanm84/packer-aws-golden-image-pipeline)
- [Kubernetes Zero to Production](https://github.com/jeevanm84/kubernetes-zero-to-production)

Implementation must preserve decision IDs and verification expectations where practical.

## Completion checklist

- [ ] Requirements are measurable and business-owned.
- [ ] Trust, network, data and failure boundaries are visible.
- [ ] All six pillars contain workload-specific decisions and evidence.
- [ ] RTO/RPO are tested objectives, not labels.
- [ ] Failure detection, mitigation and prevention are documented.
- [ ] Cost is measured per useful business outcome.
- [ ] Decisions include trade-offs and revisit triggers.
- [ ] Improvements have owners and acceptance evidence.
