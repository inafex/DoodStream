# 🚀 Doodstream API Client

<p align="center">
  <img src="doodstream.svg" alt="Doodstream Logo" width="200"/>
</p>

A comprehensive command-line interface for interacting with the Doodstream API. This tool provides easy access to Doodstream's file hosting and management features directly from your terminal.

## 🌟 Features That'll Make You Go "Wow!"

- **Upload files like a boss** 📤 (local AND remote - we're flexible like that!)
- **Manage files with the grace of a digital ballet dancer** 💃 (list, rename, move, delete)
- **Folder operations smoother than a buttered slide** 📁 (create, rename, list contents)
- **Remote upload management** 🌐 (because who doesn't love a good remote control?)
- **File search so good, it could find Waldo** 🔍
- **Account info at your fingertips** 👆 (impress your friends with your Doodstream stats!)
- **DMCA list retrieval** ⚖️ (keeping it legal, folks!)

## 🛠 Requirements (AKA "The Stuff You Need")

- Python 3.6+ (we're not cavemen, after all)
- `requests` library (for making friends with web servers)
- `requests_toolbelt` library (because sometimes you need extra tools in your belt)
- `Coffee` for sajen

## 🏗 Installation (Don't Worry, It's Easier Than become Vice President of Indonesia)

1. Clone this bad boy:
   ```
   git clone https://github.com/inafex/DoodStream.git
   cd DoodStream
   ```

2. Install the dependencies (they're needy, but we love them):
   ```
   pip install -r requirements.txt
   ```

## 🔧 Configuration (Quick, Like Ripping Off a Band-Aid)

Set your Doodstream API key as an environment variable:

```
export DOODSTREAM_API_KEY="your_super_secret_api_key_here"
```

Or, if you're feeling lazy (pemalas), just use the `--api-key` option when running the script.

## 🚀 Usage (Where the Magic Happens)

General syntax (it's not rocky gerung, but it's close):

```
python doodstream_client.py [--api-key API_KEY] COMMAND [ARGS]
```

Replace `COMMAND` with your desired action, and `[ARGS]` with... well, the arguments. You got this!

### 📜 Available Commands (Your Spellbook of Digital Incantations)

1. **Upload a file** (local edition):
   ```
   python doodstream_client.py upload /home/arsip-bapak/pesawat-jet-adek.mp4
   ```

2. **Clone a file** (because good things deserve copies):
   ```
   python doodstream_client.py clone FILE_CODE
   ```

3. **Remote upload** (for when you're feeling lazy):
   ```
   python doodstream_client.py remote-upload https://x.com/marimas.mp4
   ```

4. **List remote uploads** (check on your pokeb collections):
   ```
   python doodstream_client.py remote-upload-list
   ```

5. **Create a folder** (organization is key, people!):
   ```
   python doodstream_client.py create-folder "Kekejaman KPI dan Soertahono"
   ```

6. **Search for files** (find that needle in the digital haystack):
   ```
   python doodstream_client.py search "bergerak sendiri"
   ```

...

## 🎭 Examples (Because We All Learn from Examples)

1. **Upload a funny video of your friends (mulyono) :**
   ```
   python doodstream_client.py upload /home/fufufafa/mulyono-bicycles.mp4
   ```

2. **Create a folder for your secret meme:**
   ```
   python doodstream_client.py create-folder "ARSIP-1998"
   ```

3. **Search for that embarrassing video you uploaded last night:**
   ```
   python doodstream_client.py search "list koruptor"
   ```

## 🎨 Response Format

Responses come in beautiful, prettified JSON.

## 🚦 Error Handling

If something goes wrong, the script will let you know.

## ⏱ Rate Limiting

Remember, with great power comes great responsibility. Don't abuse the API, or Doodstream might put you in time-out!

## 🤝 Contributing

Found a bug? Want to add a feature? Just fork, code, and send us a pull request.

## 📜 License

This project is licensed under the GNU General Public License v3.0 (GPLv3).

## ⚠️ Disclaimer

This tool isn't officially associated with Doodstream.

## 📮 Contact

Questions? Comments? Love letters? Open an issue on GitHub.
