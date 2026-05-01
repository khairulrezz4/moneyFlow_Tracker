# Chat Workflow Protocol
## Always Reference System Skills

### Directive
In every interaction in this chat:
1. **Identify the task category** from user request
2. **Load relevant skill(s)** from `system_skills.yaml`
3. **Apply skill template** (request format, input/output format)
4. **Communicate the skill ID** to user
5. **Follow skill guidelines** (prerequisites, best practices, anti-patterns)
6. **Report token cost** estimate

---

## Interaction Protocol

### Step 1: User Request
```
User: "I need to fix an ImportError in bot.py"
```

### Step 2: Match to Skill
```
Task type: Debugging
Matching skill(s): debug_error, error_interpretation
Primary skill: debug_error (id: debug_error)
```

### Step 3: Load Skill Metadata
```yaml
id: debug_error
token_cost: 150-300
prerequisites:
  - error_message: true
  - line_number: true
  - code_context: true
input_format:
  error_type: string
  message: string
  location: "file.py:line_num"
  context: "code snippet"
```

### Step 4: Apply Template
```
Me: "I'll use the 'debug_error' skill (est. 150-300 tokens).

To proceed, I need:
  ✓ Error type: ImportError
  ✓ Exact message: [you provide]
  ✓ Location: bot.py:5
  ✓ Context: 3-5 lines around the error

Please provide the complete error message and context."
```

### Step 5: Execute & Report
```
[After you provide details]

Root Cause: [diagnosis]
Fix: [code block]
Verification: [test steps]

Skill Used: debug_error
Tokens Used: ~250
Status: ✓ Complete
```

---

## Skill Routing Rules

| Request Type | Primary Skill | Secondary Skills |
|---|---|---|
| "How do I fix this error?" | debug_error | error_interpretation |
| "Review my code" | code_review | refactor |
| "I need to read X file" | file_read | file_search |
| "Create a new file" | file_create | file_read (for reference) |
| "Write tests for X" | testing | validation |
| "Help me set up" | environment_setup | dependency_management |
| "Deploy this" | deployment | build_task |
| "How many tokens?" | token_budgeting | context_management |

---

## Communication Format

### Every Response Should Include:

```
**Skill Used**: [skill_name] (id: [skill_id])
**Token Cost**: [estimated tokens]
**Status**: [In-progress / Complete / Needs more info]

[Main content following skill template]

---
**Next Step**: [What happens next or what you need to provide]
```

### Example Response:

```
**Skill Used**: code_review (id: code_review)
**Token Cost**: 400-600 tokens
**Status**: Ready to proceed

Reviewing: bot.py::handle_expense for performance

To proceed, please confirm:
- Are you concerned about execution speed, memory usage, or both?
- Expected performance target? (e.g., <100ms per request)

---
**Next Step**: Provide concerns and constraints, then I'll analyze
```

---

## When Multiple Skills Apply

**Scenario**: User says "My code doesn't work"

1. **Primary skill**: debug_error (most likely)
2. **Secondary skills**: error_interpretation, validation, testing
3. **Action**: Ask for clarification
   - "Do you have an error message? → use debug_error"
   - "No error but wrong output? → use validation"
   - "Need to add tests? → use testing"

---

## Special Cases

### Case 1: Skill Prerequisites Not Met
```
Skill: debug_error
Prerequisites missing: error_message, line_number

Me: "I need the error message and line number to use the debug_error skill.
What is the complete error output?"
```

### Case 2: Wrong Skill Selected
```
User: "Optimize my code"
Initial skill: refactor
Problem: "Optimize" is ambiguous

Me: "To help you optimize, I need to know:
- Performance optimization? → code_review (performance concern)
- Token optimization? → token_budgeting
- Readability optimization? → refactor (readability goal)

Which concern applies?"
```

### Case 3: Cross-Skill Task
```
User: "Set up a new project with tests"
Skills: environment_setup (primary) + testing (secondary)

Me: "This requires two skills:
1. environment_setup: Install dependencies, configure env
2. testing: Write test suite

Should I proceed with both, or focus on setup first?"
```

---

## Anti-Patterns to Avoid

❌ **Don't**: Ignore the skill system and just answer
✓ **Do**: Reference skill, apply template

❌ **Don't**: Use skills inconsistently (sometimes yes, sometimes no)
✓ **Do**: Always reference skills, even for quick answers

❌ **Don't**: Make up custom workflows
✓ **Do**: Use system_skills.yaml as single source of truth

❌ **Don't**: Forget to report token cost and skill ID
✓ **Do**: Include both in every response

---

## Token Tracking (Optional)

If tracking tokens per chat session:
```
Session Start: [timestamp]

| Skill | Request | Tokens Used | Status |
|-------|---------|-------------|--------|
| debug_error | Fix ImportError | 250 | ✓ |
| code_review | Review performance | 500 | ✓ |
| file_read | Read bot.py:1-50 | 300 | ✓ |
| testing | Write expense tests | 400 | ✓ |
|-------|---------|-------------|--------|
| **Total** | | **1450** | |

Budget Remaining: 1550 / 3000 tokens
```

---

## Summary

**The Golden Rule**: 
> Every interaction references system_skills.yaml, applies the skill template, reports the skill ID and token cost, and follows the skill's guidelines.

This ensures:
- ✓ Consistency
- ✓ Efficiency (no wasted tokens on unclear requests)
- ✓ Traceability (you know which skill was used)
- ✓ Predictability (you know what to expect)
