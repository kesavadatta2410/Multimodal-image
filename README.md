# Multimodal Agent

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Streamlit](https://img.shields.io/badge/streamlit-%E2%9C%93-success)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Overview
A multimodal AI agent that accepts images and natural‑language instructions, processes them with Llama 4 Scout via the Groq API, and returns structured JSON results. The project includes a Streamlit front‑end for easy interaction.

---

## Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/multimodal-agent.git
cd multimodal-agent

# Create a fresh virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file (or copy from the example) with your Groq API key:
```bash
cp .env.example .env
# Edit .env and set GROQ_API_KEY=your_key_here
```

---

## Usage
Run the Streamlit UI:
```bash
streamlit run app.py
```

*Upload an image, enter a question or instruction, optionally add context, and click **Run** in the sidebar.*

You can also call the API directly (e.g., via a serverless function) using the `/api/analyze` endpoint. The endpoint expects a JSON payload:
```json
{
  "image": "<base64‑encoded image>",
  "filename": "optional.jpg",
  "instruction": "Describe the image",
  "context": "additional context"
}
```

---

## Development
### Running tests
```bash
pytest
```

### Adding features
1. Update the prompt in `agent/prompt.py` if you need to change the system instructions.
2. Extend the UI in `app.py` – the layout uses Streamlit best practices.
3. Ensure any new code validates inputs similarly to `api/analyze.py`.

---

## Contributing
Contributions are welcome! Please open an issue or pull request.

1. Fork the repository.
2. Create a feature branch.
3. Ensure all tests pass.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
