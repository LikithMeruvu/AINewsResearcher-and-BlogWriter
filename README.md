
---

# AINewsresearcher-and-BlogWriter

AINewsresearcher-and-BlogWriter is an innovative project aimed at automating the process of AI news gathering and blog post writing. With our AI agent at the helm, you can effortlessly collect insights and news about any topic of your interest from the Internet. Leveraging Crew AI frameworks for robust agents, this project streamlines the otherwise time-consuming tasks of information gathering and content creation.

## Installation

To get started with AINewsresearcher-and-BlogWriter, follow these simple steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using pip:
   
   ```
   pip install -r requirements.txt
   ```

## Setup Environment Variables

Before running the project, you need to set up your environment variables. Create a `.env` file in the root directory of the project and add the following variables:

```
GROQ_API_KEY = "XXXXXXXXXXXXXXXXXXXXXX"
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXX"
GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXX"
```

Replace the placeholder values (`XXXXXXXXXXXXXXXXXXXXXX`, `XXXXXXXXXXXXXXXXXXXX`, `XXXXXXXXXXXXXXXXXXX`) with your respective API keys.

You can obtain these API keys from the following sources:

- For GROQ API key, visit: [GROQ Console](https://console.groq.com/keys)
- For Gemini API key, visit: [Google AI Studio](https://aistudio.google.com/app/apikey)
- For OpenAI API key, visit: [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

Once you have set up the environment variables, you can start using the project. There are two main ways to interact with the system:

1. **Using cmd.py:** You can run `cmd.py` directly from the command line and provide your prompt as an argument. Here's how you can do it:

   ```
   python cmd.py <your prompt>
   ```

2. **Using main.py programmatically:** If you prefer programmatic interaction, you can utilize `main.py` to integrate the functionality into your own applications.

## Frameworks and Tools

This repository utilizes the following frameworks and tools:

- CrewAI Framework: A powerful framework for building AI agents and automation systems.
- Language Chain Tools: Tools and libraries for natural language processing and generation.

## Contributing

We welcome contributions from the community! If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Crew AI for their outstanding framework and support.
- Thanks to the developers of Language Chain Tools for providing essential tools for NLP tasks.

---
