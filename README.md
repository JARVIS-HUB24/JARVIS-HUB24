# JARVIS-HUB24

**Jarvis Agent Toolkit** - open-source utilities for AI agent systems.

Production-tested scripts from the Jarvis autonomous AI agent infrastructure.

## Utilities

### web_search.py - DuckDuckGo Web Search CLI

A lightweight, zero-API-key web search tool via DuckDuckGo.

**Features:**
- No API key required
- Domain filtering (--domain github.com)
- Time period filtering (--period w/m/y)
- JSON output mode
- Clean CLI interface

**Install:** pip install ddgs

**Usage:**

    python3 web_search.py query
    python3 web_search.py query --max 20
    python3 web_search.py query --domain github.com
    python3 web_search.py query --period w
    python3 web_search.py query --json

## License

MIT

---
Built by Jarvis - an autonomous AI agent system.