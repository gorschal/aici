#!/usr/bin/env python3
"""
GitHub Action runner for AIQACI.
"""

import os
import sys
import openai

# ------------------------------------------------------------------
# 1. PROMPT (exmple)
# ------------------------------------------------------------------
PROMPT = (
    "You are a helpful coding assistant. "
    "Generate clean, idiomatic code according to the user request."
)

# ------------------------------------------------------------------
# 2. Reading environment variables
# ------------------------------------------------------------------
MODEL = os.getenv("MODEL") or "gpt-3.5-turbo"
TEMPERATURE = float(os.getenv("TEMPERATURE") or "0.3")
LANGUAGE = os.getenv("LANGUAGE")
FRAMEWORK = os.getenv("FRAMEWORK") or ""
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not LANGUAGE:
    sys.exit("LANGUAGE env variable is required")
if not OPENAI_KEY:
    sys.exit("OPENAI_API_KEY env variable is required")

openai.api_key = OPENAI_KEY

# ------------------------------------------------------------------
# 3. Forming the user's message
# ------------------------------------------------------------------
user_msg_parts = [f"Language: {LANGUAGE}"]
if FRAMEWORK:
    user_msg_parts.append(f"Framework: {FRAMEWORK}")
user_msg_parts.append(f"\nTask: {PROMPT}")
user_message = "\n".join(user_msg_parts)

# ------------------------------------------------------------------
# 4. Request to OpenAI
# ------------------------------------------------------------------
try:
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": user_message}],
        temperature=TEMPERATURE,
    )
    print(response.choices[0].message.content.strip())
except openai.error.OpenAIError as e:
    sys.exit(f"OpenAI API error: {e}")
