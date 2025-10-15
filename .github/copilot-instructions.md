# Copilot Instructions

## Env Management
- Always use uv to manage the python environment.
- Only install the packages that are necessary for the project, remove the ones that are no longer needed.

## Python Code Guidelines
- Always use type hints for function parameters and return types.
- Use f-strings for string formatting.

## FastAPI Guidelines
- Use Pydantic models for data validation and serialization and for the FastAPI response models.
- Only use the type hints, do not use the `response_model` parameter in the FastAPI route decorators.

## Testing
- Use `pytest` for writing tests.
- Include only one assertion per test function.
