# Assignment Review

Review this persona/model orchestration allocation before execution.

## Allocation

```json
{
  "schema": "team_model_orchestrator.allocation.v3",
  "created_at": "2026-05-22T13:21:38+0900",
  "updated_at": "2026-05-22T13:21:39+0900",
  "repo": "/Users/zenkim_office/Project/wavvy",
  "play_run": "/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132138_wavvy-write-command-shim",
  "request": "연결해줘 -director",
  "plan_file": null,
  "plan_fingerprint": null,
  "allocation_basis": "request_only",
  "requested_tier": "auto",
  "resolved_tier": "tier3",
  "risk": "standard",
  "persona_policy": "auto",
  "routing_policy": "difficulty_risk",
  "primary_persona": "ai-ops-expert",
  "cds_figma_component_gate": {
    "enabled": false,
    "source_contract": {
      "cds_repo": "/Users/zenkim_office/Project/CDS",
      "component_contract": {
        "path": "/Users/zenkim_office/Project/CDS/.claude/rules/component-contract.md",
        "version": "1.1",
        "sha256": "16dd19da7c3b67b6afedbaed1290d54ef257309bd558099f46cf504a94d07e6c"
      },
      "review_skill": {
        "path": "/Users/zenkim_office/Project/CDS/.claude/skills/cds-review/SKILL.md",
        "sha256": "51e1db028b5d853e55b9af6e2582d22999fe2917fed53e913cd438c07915ae03"
      },
      "make_component_skill": {
        "path": "/Users/zenkim_office/Project/CDS/.claude/skills/cds-make-component/SKILL.md",
        "sha256": "5e24ca79202aca90fc0ba7e83aa87653e944d305da7c55046f59445a4ce13e2d"
      },
      "naming_policy": {
        "path": "/Users/zenkim_office/Project/CDS/.claude/rules/naming-policy.md",
        "sha256": "537206e545fb707e15ef84497598914cef280e645906545a6ab9d1a1c7fabc33"
      }
    },
    "rules": [
      "ContractException documents quarantine/remediation only and cannot convert structure to PASS",
      "always load CDS/.claude/rules/component-contract.md and record its version/hash",
      "before final handoff/record for component work, submit CompletionEvidence.namingGate evidence",
      "before mutation for public component work, submit CreationDecision evidence",
      "before public createNew, existingCandidates must record CDS component/variant/property/slot search",
      "completion requires structuralFidelity.status=pass",
      "for CDS component creation/extension/custom requests, load CDS/.claude/skills/cds-make-component/SKILL.md",
      "for Figma/CDS review requests, load CDS/.claude/skills/cds-review/SKILL.md",
      "image-backed or screenshot-backed CDS components are not publishable completion",
      "productLocalAllowed routes low-reuse screen-local nodes away from public CDS and does not approve public creation",
      "public createNew requires CreationDecision reuseRejectionEvidence, createNewJustification, and expectedReuseCount >= 3",
      "reuseExisting exact fits and extendExisting variant/property/slot fits must block createNew"
    ]
  },
  "figma_live_mutation": {
    "enabled": false,
    "rules": [
      "baseline evidence must complete before live Figma mutation",
      "live Figma mutation workers must use senior-or-stronger execution profiles when risk is high",
      "Figma layout verification uses design judgment, not generic AI Ops verification",
      "downstream verification workers must not receive the same default mutation write scope"
    ]
  },
  "image_generation_routing": {
    "enabled": false,
    "route": "none",
    "default_route": "builtin_image_gen",
    "api_required": false,
    "api_model": "gpt-image-2",
    "api_helper": "project-local OpenAI Images API helper, e.g. scripts/openai-gpt-image2.py when present",
    "transparent_png_gate": false,
    "rules": [
      "Use the built-in Codex image_gen path for ordinary design sketches, one-off visual drafts, and fast Figma exploration.",
      "Use OpenAI Images API with model gpt-image-2 when the request explicitly requires GPT Image 2/gen2, model evidence, auditability, repeatability, batch generation, manifest/hash/request-id records, delivery, or client review.",
      "Do not persist API keys in repo files; use OPENAI_API_KEY or an ephemeral clipboard/env handoff and record only a non-secret fingerprint when needed.",
      "When transparent PNG/alpha output is required, add a post-processing gate because gpt-image-2 must not be assumed to provide transparent background output directly.",
      "For Figma badge/icon work, keep the frame/reference system as SSOT and generate or composite only the requested interior subject unless the request explicitly asks to redesign the frame."
    ]
  },
  "protected_write_scope": [],
  "forbid_write_scope": [],
  "scope_gate": null,
  "requires_explicit_grant_paths": [],
  "discovery_gate_required": false,
  "discovery_gate_scope": ".ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/orchestrator/discovery-gate.json",
  "discovery_gate_contract": null,
  "release_readiness_required": false,
  "release_readiness_scope": ".ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/orchestrator/release-readiness.md",
  "review_target": "claude",
  "timeout_seconds": 2700,
  "tier_profile": {
    "label": "Decomposition + Lead Integration",
    "description": "Cross-project policy, architecture, risky automation, or broad orchestration work.",
    "worker_shape": "senior evidence, senior maker, lead integration, and lead release judgment",
    "review_shape": "assignment review, per-stage peer gates, and integration review",
    "workers": [
      {
        "id": "worker-01",
        "persona_strategy": "evidence",
        "execution_profile": "senior",
        "difficulty": "low",
        "risk": "medium",
        "responsibility": "Gather bounded evidence and list affected files without editing."
      },
      {
        "id": "worker-02",
        "persona_strategy": "primary",
        "execution_profile": "senior",
        "difficulty": "medium",
        "risk": "high",
        "responsibility": "Implement the assigned slice inside a disjoint write scope."
      },
      {
        "id": "worker-03",
        "persona_strategy": "integration",
        "execution_profile": "lead",
        "difficulty": "high",
        "risk": "high",
        "responsibility": "Integrate worker output, repair defects, and verify behavior."
      },
      {
        "id": "worker-04",
        "persona_strategy": "release",
        "execution_profile": "lead",
        "difficulty": "high",
        "risk": "high",
        "responsibility": "Check architecture, process fit, and release readiness."
      }
    ]
  },
  "risk_policy": {
    "description": "Use deterministic scope heuristics without bias.",
    "auto_tier_bias": 0,
    "allow_default_decisions": true
  },
  "routing_policy_profile": {
    "basis": "difficulty+risk",
    "description": "Assign functional persona for judgment first, then assign execution_profile/model/effort by task difficulty, blast radius, integration risk, and review need.",
    "token_optimization": "Prefer the lowest execution profile that can safely satisfy the task; reserve senior/lead profiles for integration, repair, architecture, policy, and release judgment.",
    "request_interpretation_guard": {
      "description": "Ask the user before converting ambiguous intent into durable allocation or policy behavior.",
      "ask_user_when": [
        "The request could mean one-off/current-project handling or a global/permanent policy change.",
        "The request could apply only to research, analysis, and planning, or to implementation, verification, and allocation as well.",
        "Performance wording could mean highest-quality planning output or a blanket worker/profile restriction.",
        "Cleanup wording could remove incorrect implementation/policy traces or also delete planning/research artifacts the user may want preserved."
      ],
      "default_action": "pause_and_ask_before_editing_policy_or_allocator",
      "junior_intern_policy": "Simple repetitive work that does not require difficult reasoning or analysis remains eligible for intern/junior execution profiles unless explicitly excluded."
    }
  },
  "workers": [
    {
      "id": "worker-01",
      "execution_profile": "senior",
      "difficulty": "low",
      "risk": "medium",
      "responsibility": "Gather bounded evidence and list affected files without editing.",
      "persona": "researcher",
      "role": "senior",
      "model": "gpt-5.5",
      "effort": "high",
      "scope_mode": "evidence",
      "repair_only": false,
      "repair_source_worker": null,
      "repair_contract": null,
      "write_scope": [],
      "external_candidates": [
        {
          "id": "hesreallyhim-awesome-claude-code",
          "status": "candidate",
          "repo": "https://github.com/hesreallyhim/awesome-claude-code",
          "stars_checked": "42900+",
          "checked_at": "2026-05-08",
          "license": "see-repo",
          "fit": "high-signal discovery index for Claude Code resources",
          "risk": "README organization is in flux; use as map, not operational source"
        },
        {
          "id": "rohitg00-skillkit",
          "status": "candidate",
          "repo": "https://github.com/rohitg00/skillkit",
          "stars_checked": "not-checked",
          "checked_at": "2026-05-08",
          "license": "unknown",
          "fit": "portable skill source map across Claude Code, Codex, Cursor, and others",
          "risk": "translation layer must preserve original licenses and creator attribution"
        }
      ],
      "open_skill_playbook": {
        "status": "local_fallback",
        "checked_at": "2026-05-10",
        "source_ids": [],
        "reference_source_ids": [
          "agent-skills-open-standard"
        ],
        "activation": "Use when the worker owns bounded evidence gathering, source quality, prior-art scanning, or uncertainty reporting.",
        "rules": [
          "Prefer primary sources and local repo evidence.",
          "Separate verified fact, inference, and unresolved uncertainty.",
          "Keep discovery bounded to the assigned question and output reusable citations."
        ],
        "do_not": [
          "Do not turn discovery into implementation unless explicitly assigned.",
          "Do not cite a collection index as proof for the underlying tool without checking the source."
        ]
      },
      "open_skill_sources": [
        {
          "url": "https://agentskills.io/what-are-skills",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "website",
          "license_policy": "website",
          "use_policy": "metadata_only",
          "fit": "Agent Skill structure and progressive-disclosure source format.",
          "id": "agent-skills-open-standard",
          "active": false
        }
      ],
      "open_skill_source_ids": [
        "agent-skills-open-standard"
      ],
      "seniority": "senior",
      "functional_role": "Researcher Worker",
      "runtime": "codex",
      "execution_group": "parallel-1",
      "depends_on": []
    },
    {
      "id": "worker-02",
      "execution_profile": "senior",
      "difficulty": "medium",
      "risk": "high",
      "responsibility": "Implement the assigned slice inside a disjoint write scope.",
      "persona": "ai-ops-expert",
      "role": "senior",
      "model": "gpt-5.5",
      "effort": "high",
      "scope_mode": "implementation",
      "repair_only": false,
      "repair_source_worker": null,
      "repair_contract": null,
      "write_scope": [],
      "external_candidates": [
        {
          "id": "wshobson-agents-orchestration",
          "status": "candidate",
          "repo": "https://github.com/wshobson/agents",
          "stars_checked": "34250+",
          "checked_at": "2026-05-08",
          "license": "MIT",
          "fit": "orchestration, agent workflow, plugin architecture, progressive-disclosure skills",
          "risk": "large plugin surface; adapt selectively, do not install wholesale"
        }
      ],
      "open_skill_playbook": {
        "status": "adapted",
        "checked_at": "2026-05-10",
        "source_ids": [
          "wshobson-agents-orchestration"
        ],
        "reference_source_ids": [
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ],
        "activation": "Use when the worker owns agent workflows, commands, context, handoff, memory, or orchestration artifacts.",
        "rules": [
          "Design the durable artifact contract before changing runtime behavior.",
          "Separate public triggers from internal routing metadata.",
          "Preserve resume, handoff, and audit trails when adding automation.",
          "Define observability events for handoffs, tool calls, costs, retries, and multi-agent coordination before adding hidden automation.",
          "For design-system automation, represent recovery, quarantine, remediationRequired, and PASS as separate states; exceptions must not silently promote blocked work to completion.",
          "For CDS/Figma automation, require existing component, variant, property, and slot candidate evidence before allowing public createNew."
        ],
        "do_not": [
          "Do not add public role/model triggers for internal routing metadata.",
          "Do not rely on hidden session state when a file artifact can preserve the decision.",
          "Do not let an exception schema or reviewer note override a hard completion gate without explicit audited evidence.",
          "Do not let productLocalAllowed approve public CDS creation when expected reuse is below the threshold."
        ]
      },
      "open_skill_sources": [
        {
          "url": "https://github.com/wshobson/agents",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "adapted_principles",
          "fit": "Agent workflow, orchestration, command, and skill architecture patterns.",
          "id": "wshobson-agents-orchestration",
          "active": true
        },
        {
          "url": "https://agentskills.io/what-are-skills",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "website",
          "license_policy": "website",
          "use_policy": "metadata_only",
          "fit": "Agent Skill structure and progressive-disclosure source format.",
          "id": "agent-skills-open-standard",
          "active": false
        },
        {
          "url": "https://github.com/nexus-labs-automation/agent-observability",
          "status": "candidate",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "metadata_only",
          "fit": "Agent observability source for tracing, tool-call tracking, token/cost tracking, multi-agent coordination, guardrails, and production evals; kept inactive until public maintenance/activity improves.",
          "id": "nexus-agent-observability",
          "active": false
        }
      ],
      "open_skill_source_ids": [
        "wshobson-agents-orchestration",
        "agent-skills-open-standard",
        "nexus-agent-observability"
      ],
      "seniority": "senior",
      "functional_role": "AI Ops Expert Worker",
      "runtime": "codex",
      "execution_group": "parallel-1",
      "depends_on": []
    },
    {
      "id": "worker-03",
      "execution_profile": "lead",
      "difficulty": "high",
      "risk": "high",
      "responsibility": "Integrate worker output, repair defects, and verify behavior.",
      "persona": "ai-ops-expert",
      "role": "lead",
      "model": "gpt-5.5",
      "effort": "xhigh",
      "scope_mode": "repair_only",
      "repair_only": true,
      "repair_source_worker": "worker-02",
      "repair_contract": {
        "base_worker": "worker-02",
        "allowed_changes": "repair defects, integrate worker output, and verify behavior without wholesale reimplementation",
        "redesign_behavior": "stop with NEEDS_USER_DECISION if the base design must be replaced"
      },
      "write_scope": [],
      "external_candidates": [
        {
          "id": "wshobson-agents-orchestration",
          "status": "candidate",
          "repo": "https://github.com/wshobson/agents",
          "stars_checked": "34250+",
          "checked_at": "2026-05-08",
          "license": "MIT",
          "fit": "orchestration, agent workflow, plugin architecture, progressive-disclosure skills",
          "risk": "large plugin surface; adapt selectively, do not install wholesale"
        }
      ],
      "open_skill_playbook": {
        "status": "adapted",
        "checked_at": "2026-05-10",
        "source_ids": [
          "wshobson-agents-orchestration"
        ],
        "reference_source_ids": [
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ],
        "activation": "Use when the worker owns agent workflows, commands, context, handoff, memory, or orchestration artifacts.",
        "rules": [
          "Design the durable artifact contract before changing runtime behavior.",
          "Separate public triggers from internal routing metadata.",
          "Preserve resume, handoff, and audit trails when adding automation.",
          "Define observability events for handoffs, tool calls, costs, retries, and multi-agent coordination before adding hidden automation.",
          "For design-system automation, represent recovery, quarantine, remediationRequired, and PASS as separate states; exceptions must not silently promote blocked work to completion.",
          "For CDS/Figma automation, require existing component, variant, property, and slot candidate evidence before allowing public createNew."
        ],
        "do_not": [
          "Do not add public role/model triggers for internal routing metadata.",
          "Do not rely on hidden session state when a file artifact can preserve the decision.",
          "Do not let an exception schema or reviewer note override a hard completion gate without explicit audited evidence.",
          "Do not let productLocalAllowed approve public CDS creation when expected reuse is below the threshold."
        ]
      },
      "open_skill_sources": [
        {
          "url": "https://github.com/wshobson/agents",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "adapted_principles",
          "fit": "Agent workflow, orchestration, command, and skill architecture patterns.",
          "id": "wshobson-agents-orchestration",
          "active": true
        },
        {
          "url": "https://agentskills.io/what-are-skills",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "website",
          "license_policy": "website",
          "use_policy": "metadata_only",
          "fit": "Agent Skill structure and progressive-disclosure source format.",
          "id": "agent-skills-open-standard",
          "active": false
        },
        {
          "url": "https://github.com/nexus-labs-automation/agent-observability",
          "status": "candidate",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "metadata_only",
          "fit": "Agent observability source for tracing, tool-call tracking, token/cost tracking, multi-agent coordination, guardrails, and production evals; kept inactive until public maintenance/activity improves.",
          "id": "nexus-agent-observability",
          "active": false
        }
      ],
      "open_skill_source_ids": [
        "wshobson-agents-orchestration",
        "agent-skills-open-standard",
        "nexus-agent-observability"
      ],
      "seniority": "lead",
      "functional_role": "AI Ops Expert Worker",
      "runtime": "codex",
      "execution_group": "serial-integration",
      "depends_on": [
        "worker-01",
        "worker-02"
      ]
    },
    {
      "id": "worker-04",
      "execution_profile": "lead",
      "difficulty": "high",
      "risk": "high",
      "responsibility": "Check architecture, process fit, and release readiness.",
      "persona": "ai-ops-expert",
      "role": "lead",
      "model": "gpt-5.5",
      "effort": "xhigh",
      "scope_mode": "implementation",
      "repair_only": false,
      "repair_source_worker": null,
      "repair_contract": null,
      "write_scope": [],
      "external_candidates": [
        {
          "id": "wshobson-agents-orchestration",
          "status": "candidate",
          "repo": "https://github.com/wshobson/agents",
          "stars_checked": "34250+",
          "checked_at": "2026-05-08",
          "license": "MIT",
          "fit": "orchestration, agent workflow, plugin architecture, progressive-disclosure skills",
          "risk": "large plugin surface; adapt selectively, do not install wholesale"
        }
      ],
      "open_skill_playbook": {
        "status": "adapted",
        "checked_at": "2026-05-10",
        "source_ids": [
          "wshobson-agents-orchestration"
        ],
        "reference_source_ids": [
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ],
        "activation": "Use when the worker owns agent workflows, commands, context, handoff, memory, or orchestration artifacts.",
        "rules": [
          "Design the durable artifact contract before changing runtime behavior.",
          "Separate public triggers from internal routing metadata.",
          "Preserve resume, handoff, and audit trails when adding automation.",
          "Define observability events for handoffs, tool calls, costs, retries, and multi-agent coordination before adding hidden automation.",
          "For design-system automation, represent recovery, quarantine, remediationRequired, and PASS as separate states; exceptions must not silently promote blocked work to completion.",
          "For CDS/Figma automation, require existing component, variant, property, and slot candidate evidence before allowing public createNew."
        ],
        "do_not": [
          "Do not add public role/model triggers for internal routing metadata.",
          "Do not rely on hidden session state when a file artifact can preserve the decision.",
          "Do not let an exception schema or reviewer note override a hard completion gate without explicit audited evidence.",
          "Do not let productLocalAllowed approve public CDS creation when expected reuse is below the threshold."
        ]
      },
      "open_skill_sources": [
        {
          "url": "https://github.com/wshobson/agents",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "adapted_principles",
          "fit": "Agent workflow, orchestration, command, and skill architecture patterns.",
          "id": "wshobson-agents-orchestration",
          "active": true
        },
        {
          "url": "https://agentskills.io/what-are-skills",
          "status": "verified",
          "checked_at": "2026-05-10",
          "license": "website",
          "license_policy": "website",
          "use_policy": "metadata_only",
          "fit": "Agent Skill structure and progressive-disclosure source format.",
          "id": "agent-skills-open-standard",
          "active": false
        },
        {
          "url": "https://github.com/nexus-labs-automation/agent-observability",
          "status": "candidate",
          "checked_at": "2026-05-10",
          "license": "MIT",
          "license_policy": "permissive",
          "use_policy": "metadata_only",
          "fit": "Agent observability source for tracing, tool-call tracking, token/cost tracking, multi-agent coordination, guardrails, and production evals; kept inactive until public maintenance/activity improves.",
          "id": "nexus-agent-observability",
          "active": false
        }
      ],
      "open_skill_source_ids": [
        "wshobson-agents-orchestration",
        "agent-skills-open-standard",
        "nexus-agent-observability"
      ],
      "seniority": "lead",
      "functional_role": "AI Ops Expert Worker",
      "runtime": "codex",
      "execution_group": "serial-release",
      "depends_on": [
        "worker-03"
      ]
    }
  ],
  "review": {
    "verdict": null,
    "result_file": null,
    "exit_code": null,
    "updated_at": null
  },
  "execution": {
    "status": "pending",
    "requested_runtime": null,
    "exit_code": null,
    "updated_at": null
  },
  "integration": {
    "status": "pending",
    "worker_id": null,
    "exit_code": null,
    "updated_at": null
  },
  "implementation_review": {
    "verdict": null,
    "result_file": null,
    "exit_code": null,
    "updated_at": null
  },
  "primary_owner": "ai-ops-expert",
  "routing_decision": {
    "mode": "team_dispatch",
    "tier": "tier3",
    "resolved_tier": "tier3",
    "primary_owner": "ai-ops-expert",
    "needs_assignment_review": true,
    "reason": "오케스트레이터가 Lenny Team owner를 세우고, 동시에 할 수 있는 실무는 병렬로 시작하되 통합/최종 판단은 순서대로 진행하도록 판단했습니다.",
    "decision_reason": "오케스트레이터가 Lenny Team owner를 세우고, 동시에 할 수 있는 실무는 병렬로 시작하되 통합/최종 판단은 순서대로 진행하도록 판단했습니다.",
    "execution_mode": "mixed",
    "solo_reason": null,
    "serial_reason": null,
    "parallel_reason": "서로 기다리지 않아도 되는 실무 worker는 같은 실행 그룹에서 동시에 시작합니다.",
    "parallelization": {
      "considered": true,
      "decision": "mixed",
      "reason": "오케스트레이터가 Lenny Team owner를 세우고, 동시에 할 수 있는 실무는 병렬로 시작하되 통합/최종 판단은 순서대로 진행하도록 판단했습니다.",
      "worker_count": 4,
      "execution_groups": [
        {
          "id": "parallel-1",
          "mode": "parallel",
          "reason": "증거 수집과 주 구현은 서로 기다리지 않아도 되므로 동시에 시작합니다."
        },
        {
          "id": "serial-integration",
          "mode": "serial",
          "reason": "통합과 수정은 선행 worker 결과가 필요합니다.",
          "depends_on": [
            "parallel-1"
          ]
        },
        {
          "id": "serial-release",
          "mode": "serial",
          "reason": "최종 판단은 통합 결과 뒤에 진행합니다.",
          "depends_on": [
            "serial-integration"
          ]
        }
      ]
    }
  },
  "owner_allocation": {
    "chain": [
      "orchestrator",
      "lenny-team-owner",
      "practical-workers"
    ],
    "owner": {
      "persona": "ai-ops-expert",
      "label": "AI Ops Expert",
      "level": "director",
      "runtime": "codex",
      "model": "gpt-5.5",
      "effort": "xhigh",
      "reason": "업무 방향, 분배, 통합 판단을 맡습니다."
    },
    "co_owners": [
      {
        "persona": "ai-ops-expert",
        "label": "AI Ops Expert",
        "level": "director",
        "runtime": "codex",
        "model": "gpt-5.5",
        "effort": "xhigh"
      }
    ]
  },
  "work_breakdown": {
    "workers": [
      {
        "id": "worker-01",
        "role": "senior",
        "persona": "researcher",
        "execution_profile": "senior",
        "functional_role": "Researcher Worker",
        "seniority": "senior",
        "runtime": "codex",
        "model": "gpt-5.5",
        "effort": "high",
        "responsibility": "Gather bounded evidence and list affected files without editing.",
        "scope_mode": "evidence",
        "repair_only": false,
        "repair_source_worker": null,
        "repair_contract": null,
        "write_scope": [],
        "execution_group": "parallel-1",
        "depends_on": [],
        "open_skill_source_ids": [
          "agent-skills-open-standard"
        ]
      },
      {
        "id": "worker-02",
        "role": "senior",
        "persona": "ai-ops-expert",
        "execution_profile": "senior",
        "functional_role": "AI Ops Expert Worker",
        "seniority": "senior",
        "runtime": "codex",
        "model": "gpt-5.5",
        "effort": "high",
        "responsibility": "Implement the assigned slice inside a disjoint write scope.",
        "scope_mode": "implementation",
        "repair_only": false,
        "repair_source_worker": null,
        "repair_contract": null,
        "write_scope": [],
        "execution_group": "parallel-1",
        "depends_on": [],
        "open_skill_source_ids": [
          "wshobson-agents-orchestration",
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ]
      },
      {
        "id": "worker-03",
        "role": "lead",
        "persona": "ai-ops-expert",
        "execution_profile": "lead",
        "functional_role": "AI Ops Expert Worker",
        "seniority": "lead",
        "runtime": "codex",
        "model": "gpt-5.5",
        "effort": "xhigh",
        "responsibility": "Integrate worker output, repair defects, and verify behavior.",
        "scope_mode": "repair_only",
        "repair_only": true,
        "repair_source_worker": "worker-02",
        "repair_contract": {
          "base_worker": "worker-02",
          "allowed_changes": "repair defects, integrate worker output, and verify behavior without wholesale reimplementation",
          "redesign_behavior": "stop with NEEDS_USER_DECISION if the base design must be replaced"
        },
        "write_scope": [],
        "execution_group": "serial-integration",
        "depends_on": [
          "worker-01",
          "worker-02"
        ],
        "open_skill_source_ids": [
          "wshobson-agents-orchestration",
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ]
      },
      {
        "id": "worker-04",
        "role": "lead",
        "persona": "ai-ops-expert",
        "execution_profile": "lead",
        "functional_role": "AI Ops Expert Worker",
        "seniority": "lead",
        "runtime": "codex",
        "model": "gpt-5.5",
        "effort": "xhigh",
        "responsibility": "Check architecture, process fit, and release readiness.",
        "scope_mode": "implementation",
        "repair_only": false,
        "repair_source_worker": null,
        "repair_contract": null,
        "write_scope": [],
        "execution_group": "serial-release",
        "depends_on": [
          "worker-03"
        ],
        "open_skill_source_ids": [
          "wshobson-agents-orchestration",
          "agent-skills-open-standard",
          "nexus-agent-observability"
        ]
      }
    ],
    "execution_groups": [
      {
        "id": "parallel-1",
        "mode": "parallel",
        "reason": "증거 수집과 주 구현은 서로 기다리지 않아도 되므로 동시에 시작합니다."
      },
      {
        "id": "serial-integration",
        "mode": "serial",
        "reason": "통합과 수정은 선행 worker 결과가 필요합니다.",
        "depends_on": [
          "parallel-1"
        ]
      },
      {
        "id": "serial-release",
        "mode": "serial",
        "reason": "최종 판단은 통합 결과 뒤에 진행합니다.",
        "depends_on": [
          "serial-integration"
        ]
      }
    ]
  },
  "fingerprints": {
    "allocation": {
      "sha256": "c351d521c26a40f251061ac7726ca3d547b837cffe3c8c0470799347979330d9"
    }
  },
  "projection_files": {
    "routing_decision": "/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/orchestrator/routing-decision.json",
    "owner_allocation": "/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/orchestrator/owner-allocation.json",
    "work_breakdown": "/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/orchestrator/work-breakdown.json"
  }
}

```

## Review Questions

- Is the tier appropriate for the request and risk policy?
- Are worker personas appropriate for the functional judgment needed?
- Are external skill candidates treated as metadata unless explicitly adapted after review?
- Are Open Skill Playbook sources/license policies valid, and are metadata-only references kept inactive?
- For Figma/CDS component work, is the CDS Figma Component Gate enabled and is image-backed output blocked from completion?
- For Figma/CDS component work, does the plan require existing CDS component/variant/property search before any public `createNew`?
- For Figma/CDS component work, does the plan block `createNew` when `reuseExisting` or `extendExisting` can cover the node?
- For Figma/CDS component work, does the plan require `CreationDecision` reuse evidence, `expectedReuseCount >= 3`, and product-local routing for low-reuse nodes?
- Are execution profiles/model tiers appropriate for each worker difficulty and risk?
- Are worker responsibilities scoped with clear boundaries?
- If a Discovery Gate is required, is the producer/consumer handoff explicit and included in the relevant write scopes?
- If a release readiness artifact is required, does the release worker have a narrow write scope for that artifact?
- Did the orchestrator explicitly decide solo, serial, parallel, or mixed execution instead of silently defaulting?
- If parallel execution is selected, are the parallel groups independent enough and are later integration/release groups ordered correctly?
- Are reviewer/integrator execution profiles strong enough for the risk?
- Are peer gates preserved without silent fallback?
