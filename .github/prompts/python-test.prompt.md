---
mode: agent
---

Create an E2E test for the highlighted code.

- use pytest
- test both the green path and possible errors
- use fixture to set up and tear down resources before and after the test
- for fastapi testing, use the built-in client
- only include one assert per each test function