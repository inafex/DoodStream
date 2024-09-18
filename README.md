# Doodstream API Client

A comprehensive command-line interface for interacting with the Doodstream API. This tool provides easy access to Doodstream's file hosting and management features directly from your terminal.

## Features

- File upload (local and remote)
- File management (list, rename, move, delete)
- Folder operations (create, rename, list contents)
- Remote upload management
- File search
- Account information retrieval
- DMCA list retrieval

## Requirements

- Python 3.6+
- `requests` library
- `requests_toolbelt` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/inafex/doodstream-api-client.git
   cd doodstream-api-client
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Set your Doodstream API key as an environment variable:

```
export DOODSTREAM_API_KEY="your_api_key_here"
```

Alternatively, you can pass the API key using the `--api-key` option when running the script.

## Usage

The general syntax for using the script is:

```
python doodstream_client.py [--api-key API_KEY] COMMAND [ARGS]
```

Replace `COMMAND` with one of the available commands, and `[ARGS]` with the appropriate arguments for that command.

### Available Commands

1. **Upload a local file**
   ```
   python doodstream_client.py upload FILE_PATH [--folder-id FOLDER_ID]
   ```

2. **Clone a file**
   ```
   python doodstream_client.py clone FILE_CODE [--folder-id FOLDER_ID]
   ```

3. **Add a remote upload**
   ```
   python doodstream_client.py remote-upload URL [--folder-id FOLDER_ID] [--title TITLE]
   ```

4. **List remote uploads**
   ```
   python doodstream_client.py remote-upload-list
   ```

5. **Check remote upload status**
   ```
   python doodstream_client.py remote-upload-status FILE_CODE
   ```

6. **Check remote upload slots**
   ```
   python doodstream_client.py remote-upload-slots
   ```

7. **Perform remote upload actions**
   ```
   python doodstream_client.py remote-upload-actions ACTION [--file-code FILE_CODE]
   ```
   Available actions: restart_errors, clear_errors, clear_all, delete_code

8. **Create a new folder**
   ```
   python doodstream_client.py create-folder NAME [--parent-id PARENT_ID]
   ```

9. **Rename a folder**
   ```
   python doodstream_client.py rename-folder FOLDER_ID NEW_NAME
   ```

10. **List folder contents**
    ```
    python doodstream_client.py list-contents [--folder-id FOLDER_ID]
    ```

11. **List files**
    ```
    python doodstream_client.py list-files [--folder-id FOLDER_ID] [--page PAGE] [--per-page PER_PAGE]
    ```

12. **Check file status**
    ```
    python doodstream_client.py file-status FILE_CODE
    ```

13. **Get file information**
    ```
    python doodstream_client.py file-info FILE_CODE
    ```

14. **Get file image information**
    ```
    python doodstream_client.py file-image FILE_CODE
    ```

15. **Rename a file**
    ```
    python doodstream_client.py rename-file FILE_CODE NEW_TITLE
    ```

16. **Move a file**
    ```
    python doodstream_client.py move-file FILE_CODE FOLDER_ID
    ```

17. **Search for files**
    ```
    python doodstream_client.py search SEARCH_TERM
    ```

## Examples

1. Upload a file to the root directory:
   ```
   python doodstream_client.py upload /path/to/your/file.mp4
   ```

2. Create a new folder:
   ```
   python doodstream_client.py create-folder "My New Folder"
   ```

3. Upload a file to a specific folder:
   ```
   python doodstream_client.py upload /path/to/your/file.mp4 --folder-id 12345
   ```

4. List files in a specific folder:
   ```
   python doodstream_client.py list-files --folder-id 12345
   ```

5. Search for files:
   ```
   python doodstream_client.py search "my video"
   ```

## Response Format

The script returns JSON responses from the Doodstream API. The output is prettified for better readability.

## Error Handling

If an API request fails, the script will print an error message. Check your API key and internet connection if you encounter persistent errors.

## Rate Limiting

Be aware of Doodstream's rate limiting policies. The script does not implement rate limiting, so use it responsibly to avoid being blocked.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is not officially associated with Doodstream. Use at your own risk.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.
