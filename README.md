# Pyntent 🚀

Pyntent is a lightweight, easy-to-use Python library for intent recognition using plain text files.  
You define possible user phrases for each intent in separate files, and an index file maps intent codes to these files.  
The library matches a given phrase to the best intent based on keyword overlap.

---

## ✨ Features

- **No dependencies**: Pure Python, no external libraries required.
- **Simple setup**: Just text files for your intents.
- **Fast matching**: Finds the best intent using keyword overlap.
- **Easy to extend**: Add new intents by creating new files.

---

## ⚙️ How It Works

1. **Define intents**: Each intent is described by a text file containing example phrases.
2. **Index mapping**: The `intent/INDEX.txt` file maps intent codes to their corresponding files.
3. **Matching**: When you call `get_intent(phrase)`, the library compares the input phrase to all example phrases and returns the intent code with the highest match percentage.

---

## 📁 File Structure Example

```
pyntent.py
intent/
├── INDEX.txt
├── weather.txt
└── greetings.txt
```

### Example: `intent/INDEX.txt`

```
0|greetings
1|weather
```
- `0` is the code for greetings, using `greetings.txt`
- `1` is the code for weather, using `weather.txt`

### Example: `intent/greetings.txt`

```
Hello
Good morning
Hello, how are you?
Hi
```

### Example: `intent/weather.txt`

```
What's the weather like today?
How many degrees is it?
What's the weather?
```

---

## 🚦 How to Use

1. Place `pyntent.py` and the `intent/` folder (with your `.txt` files) in the same directory.
2. Edit `intent/INDEX.txt` to map intent codes to file names (without `.txt`).
3. Add example phrases (one per line) in each intent file.

### Example Usage

```python
from pyntent import get_intent

intent_id, confidence = get_intent("What's the weather like today?")
print(f"Intent ID: {intent_id}, Confidence: {confidence:.2f}")
```

This will return the intent code (e.g., `1` for weather) and a confidence score.

---

## 💡 Tips for Improving Accuracy

- **Use clear, representative phrases** for each intent.
- **Avoid overlapping phrases** between different intents.
- **Normalize your phrases**: keep them lowercase and remove punctuation.
- **Add more examples**: The more varied your example phrases, the better the recognition.
- **Group synonyms**: Include common variations and synonyms for user queries.
- **Regularly review**: Update your intent files as you discover new user inputs.

---

## 🛠️ Application Scenarios

- **Chatbots**: Quickly map user messages to intents for conversational AI.
- **Voice assistants**: Recognize spoken commands and map them to actions.
- **FAQ bots**: Route user questions to the correct answers.
- **Simple command interpreters**: Build CLI tools that understand natural language commands.
- **Prototyping**: Rapidly test intent recognition logic without complex ML models.

---

