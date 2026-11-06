# app.py
def add(a, b):
    return a + b

# test_app.py
from app import add
def test_add():        # NB : 1 seule ligne vide avant -> flake8 va râler !
    assert add(2, 3) == 5

# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4