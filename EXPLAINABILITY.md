# Explainability

## Inputs and Data Sources

The agent accepts caller-provided device inventories, condition notes, quantities, location constraints, recovery options, downstream destination details, and handler information. It does not access live recycler registries or commodity markets.

## Decision and Reasoning

The agent checks inventory completeness, organizes supplied recovery options, and structures handoff tasks. It does not infer device composition, calculate verified recovery yields, or certify a downstream handler.

## Limits and Constraints

The agent does not determine legal waste classification, verify recycler authorization, inspect devices, or validate hazardous-material status. Follow applicable local rules and use qualified handlers for hazardous or regulated materials.

## assess-ewaste-inventory

### Inputs
Device type, quantity, condition, known components, and storage or collection notes.

### Data Sources
Caller-provided inventory only.

### Decision
Checks for missing inventory fields and flags supplied notes indicating damaged devices or batteries for qualified review.

### Outputs
Inventory summary, missing fields, and handling review flags.

### Failure Handling
Unknown composition or condition remains unknown.

### Limits
No physical inspection or hazardous-material diagnosis.

## compare-recovery-options

### Inputs
Available reuse, repair, refurbishment, recycling, and disposal options.

### Data Sources
Caller-provided options only.

### Decision
Organizes options and their supplied benefits, constraints, and evidence without fabricating a ranking metric.

### Outputs
Option comparison and missing decision information.

### Failure Handling
Unspecified costs, yields, or certifications are marked missing.

### Limits
No external verification of downstream facilities.

## plan-responsible-handling

### Inputs
Inventory, collection constraints, destination details, and handoff tasks.

### Data Sources
Caller-provided information only.

### Decision
Creates a checklist for safe collection, data sanitization where relevant, and verified handoff to an appropriate handler.

### Outputs
Handoff checklist and information gaps.

### Failure Handling
Missing handler authorization or local requirements are flagged for confirmation.

### Limits
Not a substitute for local regulatory or hazardous-waste guidance.

## Traceability

Each observation maps to a supplied inventory field or proposed handling task.

## Transparency

Known facts, assumptions, and missing information remain distinct.

## Reproducibility

The core is deterministic for identical inputs.

## Safety

The agent avoids unsafe dismantling instructions and directs hazardous components to qualified handling.
