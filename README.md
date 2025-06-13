# 21Hash

**21Hash** is an open-source AI assistant designed to support and strengthen the global Bitcoin mining community—from industrial-scale farms to solo pleb miners.

It learns from manuals, logs, config files, and community input to help:
- Troubleshoot mining hardware and firmware
- Optimize energy use and configurations
- Share heat reuse strategies
- Answer technical questions on immersion, undervolting, and tuning
- Foster an open, collaborative mining intelligence layer

---

## 🚀 Mission
**Empower every miner—large or small—to operate smarter, more efficient, and more resilient Bitcoin mining setups through open-source AI and community intelligence.** 

**21Hash exists not only to solve today's challenges, but to help evolve Bitcoin mining hardware, software, and infrastructure—openly, globally, and sustainably—for the next 100 years.**

**It aims to catalyze a collaborative industry effort—uniting manufacturers, operators, hobbyists, and innovators—to share knowledge, co-develop tools, and improve accessibility. By reducing reliance on closed systems and monopoly-like control, 21Hash makes mining more transparent, equitable, and aligned with the values of Bitcoin itself.**

**By encouraging open development of mining hardware and software, 21Hash opens the playing field to new, innovative products and approaches—distributing hashrate, diversifying infrastructure, and helping make the Bitcoin network more decentralized, antifragile, and globally inclusive.**

---

## 💡 Why 21Hash?
- **Bitcoin-Native**: Named after Bitcoin’s 21 million hard cap
- **AI-First**: Uses GPT models and RAG pipelines to learn and improve
- **Open-Source**: Transparent, auditable, and extensible
- **Community-Driven**: Learns from real-world miner data and contributions
- **Future-Focused**: Built to inspire the long-term evolution of mining systems across the industry
- **Accessibility-Oriented**: Designed to help more people participate in mining, regardless of scale or location

---

## 🔧 Who It's For
| Group | How 21Hash Helps |
|-------|------------------|
| Large-scale miners | Optimize performance, identify issues fast, reduce costs |
| Solo/home miners | Get firmware help, setup guidance, undervolting support |
| Heat reuse miners | Improve heat capture design with shared patterns and data |
| Bitaxe/DIY devs | Share and learn from open hardware/firmware logs |
| Open-source devs | Contribute to tools, agents, and hardware/software evolution |

---

## 🧠 How It Learns

21Hash is designed to continuously evolve through a layered learning approach:

### Phase 1 – Static Prompting (Now)
- Uses a pre-engineered system prompt and GPT-4
- Answers drawn from curated mining manuals, firmware docs, and optimization guides

### Phase 2 – Community-Driven Learning (Next)
- Logs unanswered or low-confidence questions
- Contributors submit improved responses and new data
- Expands knowledge base with real miner questions and feedback

### Phase 3 – Operational Intelligence (Future)
- Accepts JSON logs, configuration files, and performance data
- Analyzes miner behavior, temperature, efficiency, uptime
- Adds validated insights into a searchable knowledge graph or vector database

This progressive learning loop allows 21Hash to grow smarter over time, while staying grounded in open contributions and real-world mining practices. By opening up the development of Bitcoin mining hardware and software, 21Hash helps distribute intelligence and hashrate across the global network.

---

## ⚡ Model Use in Phase 1

21Hash defaults to **gpt-3.5-turbo** in Phase 1. This ensures cost efficiency while providing strong answers for most Bitcoin mining questions.

- **gpt-3.5-turbo**: Fast, affordable, suitable for typical hardware, firmware, and setup Q&A.
- **gpt-4**: Higher cost, deeper reasoning, better for complex or edge-case queries (optional for those running their own version).

We have chosen to use OpenAI models initially to focus on rapid deployment, reliability, and proven performance. Our intention is to transition toward **open-source models** (e.g., LLaMA, Mistral, Mixtral) in future phases to further decentralize and democratize mining intelligence. The timeframe for this transition is dependent on community support and technical milestones but is a core long-term goal.

### Using Other Models
Those deploying 21Hash from this repo are free to adjust the model configuration. In `app.py`, simply change the `model=` parameter in the OpenAI API call to your desired model (e.g., `gpt-4`, `gpt-3.5-turbo`, or an OSS-compatible endpoint).

---

## 📦 Phase 1 – MVP Features
- Public chatbot UI (Streamlit)
- Answers common questions about:
  - Antminer S19/S21
  - WhatsMiner M30/M50
  - Firmware: BraiinsOS, LuxOS
  - Power configuration
  - Immersion setups
- Feedback logging for learning
- Open-source prompt and training data

---

## 🗺 Roadmap
| Phase | Goal |
|-------|------|
| 1 | Q&A chatbot with prompt-tuned GPT-4 + Streamlit UI |
| 2 | Logging + feedback + user-submitted config/log parsing |
| 3 | Smart miner analysis tool: config → recommendation engine |
| 4 | Integration with real dashboards (BraiinsOS, WhatsMiner Tool) |
| 5 | Community dataset and leaderboard for heat reuse & efficiency |

---

## 🤝 Contributing
We're looking for help with:
- Adding manuals and firmware docs to `/docs`
- Creating example miner configurations
- Building a RAG pipeline from markdown + PDFs
- Improving prompt logic for better results
- Translating to other languages

### Contribute your logs, configs, questions, or ideas → Help 21Hash learn.

MIT licensed, Bitcoin-native, AI-powered. 
Let’s build this together.

---

## 🔗 Resources
- [BraiinsOS Docs](https://docs.braiins.com/)
- [LuxOS Firmware](https://luxor.tech/firmware)
- [Antminer Manuals (PDFs)](https://shop.bitmain.com/support)
- [WhatsMiner Documentation](https://whatsminer.info/)

---

**Made by Bitcoiners. For Bitcoiners. Built for now—and the next 100 years.**
