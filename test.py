import os
import openai
import constants
openai.api_key = "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"
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)