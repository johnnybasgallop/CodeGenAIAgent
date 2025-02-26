# Quantum Doc - AI-Powered DocString Generator

Quantum Doc is a powerful Visual Studio Code extension that leverages AI to generate production-quality docstrings in the Google style directly within your Python files. Say goodbye to manually writing docstrings and let Quantum Doc handle the documentation for you!

## 🚀 Features
- **AI-Powered DocStrings**: Generates high-quality Google-style docstrings for your Python functions, classes, and modules.
- **Seamless Integration**: Works directly within VS Code without disrupting your workflow.
- **Easy to Use**: Just press `Cmd + Shift + P`, type `Generate Docstrings`, and let Quantum Doc do the rest!
- **Powered by Gemini 1.5 Flash**: Utilizes the latest AI model for accurate and efficient documentation.

## 🛠 Installation
1. Open Visual Studio Code.
2. Go to the Extensions Marketplace (`Cmd + Shift + X` on Mac or `Ctrl + Shift + X` on Windows/Linux).
3. Search for `Quantum Doc` and click **Install**.

## 🎯 Usage
1. Open a Python file in VS Code.
2. Press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux).
3. Type `Generate Docstrings` and select the option.
4. Watch as Quantum Doc intelligently adds well-structured docstrings to your functions and classes!

## 🌟 Example
### Before:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)
items = []

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201
```

### After:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)
items = []

@app.route("/items", methods=["POST"])
def create_item():
    """Creates a new item.

    Returns:
        tuple: JSON representation of the created item and HTTP status 201.
    """
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201
```


## 🎥 Example Video
![any alternative text you want ](/QuantumDoc.gif)

[Placeholder for .mov video file]

## 🔑 Setting Up Your Gemini API Key
Since Quantum Doc relies on the **Gemini 1.5 Flash** model, users need to provide their own API key to enable AI-powered docstring generation.

### Steps to Get Your Gemini API Key:
1. Go to the [Google AI Developer Console](https://ai.google.com/) and sign in.
2. Navigate to the **API Keys** section.
3. Generate a new API key.
4. Copy the API key and add it to the extension settings in VS Code:
   - Open VS Code settings (`Cmd + Shift + P` and type `Open User Settings`).
   - Search for `Quantum Doc API Key`.
   - Paste your API key in the field.

## 📌 Notes
- Ensure that your API key has sufficient quota for AI requests.
- The extension only supports Python at the moment.
- Your API key is stored locally and never shared.

## 🤝 Contributing
We welcome contributions! If you find a bug or want to improve the extension, feel free to submit a pull request or open an issue on GitHub.

## 📜 License
Quantum Doc is proprietary software. The license restricts copying, sharing, and unauthorized use outside of the extension.

## 📩 Support
For support or feedback, reach out via [GitHub Issues](https://github.com/your-repo/quantum-doc/issues).

Happy Coding! 🚀
