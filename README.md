# n8n sample workflow with local agents

This is a sample n8n workflow with nodes linked to local AI models served through Ollama.

## Start local n8n instance

Notes: in order to make it possible to execute local models you must enable execute commands permissions. As for a test project it's enough to set environment variable `export NODES_EXCLUDE='[]'` in `~/.bashrc`

    n8n start

## Credentials for local LLM service

- Create new credential
- Choose 'Ollama' service
- Set local URL for service, probably `http://localhost:11434`
- No API key required
- After that, you can create nodes with "Ollama Chat Model" and set any of the local models you have installed for it. This allow to set different models in different models sharing same credentials.
