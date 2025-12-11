from guardrails import Guard

rules_yaml = """
input_schema: {}
output_schema:
  - name: answer
    type: string
    constraints:
      - not_empty: {}
"""

guard = Guard.from_yaml(rules_yaml)

def validate_output(text: str) -> str:
    result = guard.run(text)
    return result["answer"]
