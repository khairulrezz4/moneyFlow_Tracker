# General Chat Skills – Token-Optimized for Claude Haiku 4.5

## Skill: Request Structure
**Purpose**: Get accurate answers with minimal token waste.  
**Token Cost**: Saved tokens (shorter conversations).

### Best Practices
- **Be specific**: State the exact problem, not vague goals
- **Provide context upfront**: File paths, error messages, code snippets
- **Ask for one thing**: Multiple asks = multiple response cycles
- **Use structured output**: Request JSON, lists, or tables instead of prose

### Anti-Patterns
- ❌ "How do I debug this?" (too vague)
- ✓ "The error is `TypeError: 'NoneType' object is not subscriptable` at line 42 in `handler.py`. How do I fix it?"

---

## Skill: Code Review & Debugging
**Purpose**: Fix bugs efficiently without wasting tokens on hypotheticals.  
**Token Cost**: 200-400 tokens per bug fix.

### Required Information
- Exact error message + line number
- Relevant code snippet (10-15 lines context)
- Expected vs actual behavior
- Reproducible steps (if applicable)

### Output Format
```
Issue: [exact problem]
Root Cause: [why it happens]
Fix: [code change]
Test: [how to verify]
```

---

## Skill: File Operations & Navigation
**Purpose**: Work efficiently with workspace files.  
**Token Cost**: Minimal (let Haiku use tools).

### Efficient Patterns
- **Read large ranges**: 50-100 lines at once, not line-by-line
- **Use grep for overviews**: Find patterns across files
- **Parallel operations**: Ask for multiple file reads in one message
- **Absolute paths**: Always use full paths to avoid ambiguity

### Example Request
"Read lines 1-50 of `src/api.ts` and lines 100-120 of `src/utils.ts`, then show me where `getUserData` is called."

---

## Skill: Documentation & Comments
**Purpose**: Write minimal but complete code docs.  
**Token Cost**: Saves future clarification questions.

### Quick Patterns
- Function: `# Returns: Type | Raises: Exception`
- Class: `# Manages X; Key methods: method1, method2`
- Complex logic: 1-line summary + 1-line per branch
- No verbose docstrings—Haiku understands concise code

### Example
```python
def parse_expense(text: str) -> dict:
    # Extracts category, amount, date from natural language
    # Returns: {"category": str, "amount": float, "date": str}
    ...
```

---

## Skill: Testing & Validation
**Purpose**: Verify code works before deploying.  
**Token Cost**: One-time investment saves debugging cycles.

### Minimal Test Setup
```python
# tests.py
def test_case(input_val, expected):
    result = function(input_val)
    assert result == expected, f"Expected {expected}, got {result}"
```

### When to Ask for Tests
- Edge cases (empty input, None, negative)
- Boundary conditions
- Error handling
- Integration points

---

## Skill: Prompt Optimization (Self-Help)
**Purpose**: Refine prompts using feedback loops.  
**Token Cost**: 300-400 tokens per cycle (GEPA-style).

### 3-Step Process
1. **Initial prompt** → Get response
2. **Feedback** → "Expected X but got Y"
3. **Refined prompt** → Load improved version

### Template (for custom tools/scripts)
```
Initial: "Parse expense messages"
Feedback: "Failed on: 'spent 50 on gas' → got Transport, expected Fuel"
Refined: "...Extract category from standard list: Food, Transport, Fuel, Healthcare..."
```

---

## Skill: File Creation & Scaffolding
**Purpose**: Set up projects without repetitive questions.  
**Token Cost**: One-time (200-300 tokens).

### Efficient Approach
- **Provide structure upfront**: "Create project layout: src/, tests/, config/"
- **Use templates**: Reference existing patterns, ask Haiku to adapt
- **Batch creates**: "Create files A, B, C with these contents" (not one at a time)

---

## Skill: Error Message Interpretation
**Purpose**: Convert cryptic errors into actionable fixes.  
**Token Cost**: 150-300 tokens per error.

### Format Error Messages for Haiku
```
Error Type: [TypeError, AttributeError, etc.]
Message: [exact message]
Location: [file.py:line_num]
Context: [3-5 lines of code around error]
```

### Example
```
Error Type: ImportError
Message: "No module named 'gepa'"
Location: optimize_parser.py:5
Context: `from gepa import optimize`
```

---

## Skill: Performance & Token Budgeting
**Purpose**: Keep chats focused and on-budget.  
**Token Cost**: Awareness (no direct cost).

### Token Budget Breakdown
- **Context gathering**: 500-1000 tokens (read files, search code)
- **Analysis**: 200-500 tokens (identify issues)
- **Solution**: 500-1000 tokens (code + explanation)
- **Verification**: 200-300 tokens (testing/validation)

**Total per task**: ~1500-3000 tokens (Haiku is efficient)

### Budget Tips
- Avoid: "Explain the entire codebase" (unbounded)
- Prefer: "Show me how X interacts with Y"
- Reuse: Store common patterns in memory/docs

---

## Skill: Context Window Management
**Purpose**: Use Haiku's 200K context efficiently.  
**Token Cost**: Zero (reference only).

### Best Practices
- **Discard old context**: Summarize progress before starting new tasks
- **Link files**: Use relative paths, let Haiku load what it needs
- **Batch related questions**: Ask 2-3 related things in one message
- **Avoid redundancy**: Don't repeat error messages or code in multiple messages

### When to Archive
- Task completed
- Context window >100K used
- Switching to unrelated project

---

## Skill: Getting Help from Haiku
**Purpose**: Ask for the right thing, get the right answer.  
**Token Cost**: Depends on clarity (vague = more tokens).

### Request Types & Optimal Phrasing

| Need | Phrase | Est. Tokens |
|------|--------|-------------|
| Bug fix | "Error: [msg], code: [snippet], fix:" | 300-500 |
| Code review | "Review [file] for [concern] only" | 400-600 |
| Refactor | "Refactor [function] to [goal]" | 500-800 |
| Explain | "What does [code] do?" | 200-400 |
| Generate | "Create [thing] with these constraints" | 600-1000 |
| Debug | "Why does [code] produce [wrong output]?" | 400-700 |

---

## Quick Checklist: Before Asking
✓ Specific problem (not "help me fix this")  
✓ Relevant code/error (full context)  
✓ Expected vs actual behavior  
✓ Reproducible steps (if applicable)  
✓ No vague requests ("optimize my code")  
✓ Single focus (one task per message)  
✓ File paths are absolute & clear

