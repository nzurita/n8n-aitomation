# n8n sample workflow with local agents

This is a sample n8n workflow with nodes linked to local AI models served through Ollama.

![Schema](n8n-graph-nodes.png)

## Start local n8n instance

Notes: in order to make it possible to execute local models you must enable execute commands permissions. As for a test project it's enough to set environment variable `export NODES_EXCLUDE='[]'` in `~/.bashrc`

    n8n start

## Local Ollama service and AI models

To install local instance of Ollama and models of your choice run these commands:

    curl -fsSL https://ollama.com/install.sh | sh
    # check installation with ollama -v

    # These models are good for required tasks in this workflow
    ollama pull qwen2.5:14b    # For text analisys and information gathering
    ollama pull mistral:7b     # For translation

## Credentials for local LLM service

- Create new credential
- Choose 'Ollama' service
- Set local URL for service, probably `http://localhost:11434`
- No API key required
- After that, you can create nodes with the different "Ollama" options and set any of the local models you have installed for it. This allow to set different models in different models sharing same credentials.

## Get Telegram stickers

Script `dump-telegram-stickers.py` returns a list of stickers IDs from Telegram collections so you can customize n8n node `Pick random sticker` with your own collections. To execute script and get IDs list run next command with any number of collections. Short name of collection is expected:

    python3 dump-telegram-stickers.py <<YOUR TOKEN>> Frankestein HarryGorilla

To get short name of collection and other info there are different options, run:

    curl -s "https://api.telegram.org/bot<<YOUR TOKEN>>/getStickerSet?name=Frankestein" | python3 -m json.tool

Or run next command just after sending a sticket to bot:

    curl -s "https://api.telegram.org/bot<<YOUR TOKEN>>/getUpdates" | python3 -m json.tool

