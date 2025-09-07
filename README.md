# AIQACI

<img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white"/>

**AIQACI** (Artificial Intelligence for Quality Assurance in Continuous Integration) is an intelligent agent designed to evaluate the quality of pull requests.

## Inputs

| Name             | Required | Default       | Description                |
| ---------------- | -------- | ------------- | -------------------------- |
| `language`       | true     | —             | Programming language       |
| `framework`      | false    | `""`          | Framework (optional)       |
| `model`          | false    | gpt-3.5-turbo | OpenAI model name          |
| `temperature`    | false    | 0.3           | Sampling temperature (0-2) |
| `openai-api-key` | true     | —             | Your OpenAI API key        |

## Example

```yaml
name: aiqaci

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run GPT-Builder
        uses: ./.github/actions/gpt-builder
        with:
          model: "gpt-4"
          temperature: "0.2"
          language: "python"
          framework: "FastAPI"
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
```
