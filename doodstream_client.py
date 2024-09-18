import requests
import os
import argparse
import json
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

class DoodstreamAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://doodapi.com/api/"
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        params = kwargs.pop('params', {})
        params['key'] = self.api_key
        try:
            response = self.session.request(method, url, params=params, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    # Upload methods
    def upload_server(self):
        return self._make_request('GET', 'upload/server')

    def upload_file(self, file_path, fld_id=None):
        server_response = self.upload_server()
        if not server_response or server_response.get('status') != 200:
            print("Failed to get upload server")
            return None

        upload_url = server_response['result']
        file_name = os.path.basename(file_path)

        def create_callback(encoder):
            encoder_len = encoder.len
            def callback(monitor):
                progress = monitor.bytes_read / encoder_len * 100
                print(f"\rUpload progress: {progress:.2f}%", end='', flush=True)
            return callback

        with open(file_path, 'rb') as f:
            form = {'api_key': self.api_key, 'file': (file_name, f, 'application/octet-stream')}
            if fld_id:
                form['fld_id'] = str(fld_id)
            encoder = MultipartEncoder(form)
            monitor = MultipartEncoderMonitor(encoder, create_callback(encoder))
            headers = {"Content-Type": monitor.content_type}
            response = requests.post(upload_url, data=monitor, headers=headers)
            print()  # New line after progress bar
            return response.json()

    def clone_file(self, file_code, fld_id=None):
        params = {'file_code': file_code}
        if fld_id:
            params['fld_id'] = fld_id
        return self._make_request('GET', 'file/clone', params=params)

    # Remote upload methods
    def remote_upload(self, url, fld_id=None, new_title=None):
        params = {'url': url}
        if fld_id:
            params['fld_id'] = fld_id
        if new_title:
            params['new_title'] = new_title
        return self._make_request('GET', 'upload/url', params=params)

    def remote_upload_list(self):
        return self._make_request('GET', 'urlupload/list')

    def remote_upload_status(self, file_code):
        return self._make_request('GET', 'urlupload/status', params={'file_code': file_code})

    def remote_upload_slots(self):
        return self._make_request('GET', 'urlupload/slots')

    def remote_upload_actions(self, action, file_code=None):
        params = {action: '1'}
        if file_code and action == 'delete_code':
            params['file_code'] = file_code
        return self._make_request('GET', 'urlupload/actions', params=params)

    # Folder management methods
    def create_folder(self, name, parent_id=None):
        params = {'name': name}
        if parent_id:
            params['parent_id'] = parent_id
        return self._make_request('GET', 'folder/create', params=params)

    def rename_folder(self, fld_id, name):
        return self._make_request('GET', 'folder/rename', params={'fld_id': fld_id, 'name': name})

    def list_contents(self, fld_id=0):
        return self._make_request('GET', 'folder/list', params={'fld_id': fld_id})

    # File management methods
    def list_files(self, page=1, per_page=100, fld_id=None, created=None):
        params = {'page': page, 'per_page': per_page}
        if fld_id:
            params['fld_id'] = fld_id
        if created:
            params['created'] = created
        return self._make_request('GET', 'file/list', params=params)

    def file_status(self, file_code):
        return self._make_request('GET', 'file/check', params={'file_code': file_code})

    def file_info(self, file_code):
        return self._make_request('GET', 'file/info', params={'file_code': file_code})

    def file_image(self, file_code):
        return self._make_request('GET', 'file/image', params={'file_code': file_code})

    def rename_file(self, file_code, title):
        return self._make_request('GET', 'file/rename', params={'file_code': file_code, 'title': title})

    def move_file(self, file_code, fld_id):
        return self._make_request('GET', 'file/move', params={'file_code': file_code, 'fld_id': fld_id})

    def search_files(self, search_term):
        return self._make_request('GET', 'search/videos', params={'search_term': search_term})

def main():
    parser = argparse.ArgumentParser(description="Doodstream API Client")
    parser.add_argument("--api-key", help="Doodstream API Key")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Upload commands
    upload_parser = subparsers.add_parser("upload", help="Upload a local file")
    upload_parser.add_argument("file_path", help="Path to the file to upload")
    upload_parser.add_argument("--folder-id", help="Folder ID to upload to (optional)")

    clone_parser = subparsers.add_parser("clone", help="Clone a file")
    clone_parser.add_argument("file_code", help="File code to clone")
    clone_parser.add_argument("--folder-id", help="Folder ID to clone to (optional)")

    # Remote upload commands
    remote_upload_parser = subparsers.add_parser("remote-upload", help="Add a remote upload")
    remote_upload_parser.add_argument("url", help="URL to upload")
    remote_upload_parser.add_argument("--folder-id", help="Folder ID to upload to (optional)")
    remote_upload_parser.add_argument("--title", help="New title for the file (optional)")

    subparsers.add_parser("remote-upload-list", help="List remote uploads")

    remote_status_parser = subparsers.add_parser("remote-upload-status", help="Check remote upload status")
    remote_status_parser.add_argument("file_code", help="File code to check status")

    subparsers.add_parser("remote-upload-slots", help="Check remote upload slots")

    remote_actions_parser = subparsers.add_parser("remote-upload-actions", help="Perform remote upload actions")
    remote_actions_parser.add_argument("action", choices=['restart_errors', 'clear_errors', 'clear_all', 'delete_code'])
    remote_actions_parser.add_argument("--file-code", help="File code for delete action")

    # Folder management commands
    create_folder_parser = subparsers.add_parser("create-folder", help="Create a new folder")
    create_folder_parser.add_argument("name", help="Name of the folder to create")
    create_folder_parser.add_argument("--parent-id", help="Parent folder ID (optional)")

    rename_folder_parser = subparsers.add_parser("rename-folder", help="Rename a folder")
    rename_folder_parser.add_argument("folder_id", help="ID of the folder to rename")
    rename_folder_parser.add_argument("name", help="New name for the folder")

    list_contents_parser = subparsers.add_parser("list-contents", help="List folder contents")
    list_contents_parser.add_argument("--folder-id", default=0, help="Folder ID to list (optional)")

    # File management commands
    list_files_parser = subparsers.add_parser("list-files", help="List files")
    list_files_parser.add_argument("--folder-id", help="Folder ID to list files from (optional)")
    list_files_parser.add_argument("--page", type=int, default=1, help="Page number (optional)")
    list_files_parser.add_argument("--per-page", type=int, default=100, help="Results per page (optional)")

    file_status_parser = subparsers.add_parser("file-status", help="Check file status")
    file_status_parser.add_argument("file_code", help="File code to check status")

    file_info_parser = subparsers.add_parser("file-info", help="Get file information")
    file_info_parser.add_argument("file_code", help="File code to get info")

    file_image_parser = subparsers.add_parser("file-image", help="Get file image information")
    file_image_parser.add_argument("file_code", help="File code to get image info")

    rename_file_parser = subparsers.add_parser("rename-file", help="Rename a file")
    rename_file_parser.add_argument("file_code", help="File code to rename")
    rename_file_parser.add_argument("title", help="New title for the file")

    move_file_parser = subparsers.add_parser("move-file", help="Move a file")
    move_file_parser.add_argument("file_code", help="File code to move")
    move_file_parser.add_argument("folder_id", help="Folder ID to move the file to")

    search_parser = subparsers.add_parser("search", help="Search for files")
    search_parser.add_argument("search_term", help="Search term")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get('DOODSTREAM_API_KEY')
    if not api_key:
        print("API key not provided. Use --api-key or set DOODSTREAM_API_KEY environment variable.")
        return

    api = DoodstreamAPI(api_key)

    result = None

    if args.command == "upload":
        result = api.upload_file(args.file_path, args.folder_id)
    elif args.command == "clone":
        result = api.clone_file(args.file_code, args.folder_id)
    elif args.command == "remote-upload":
        result = api.remote_upload(args.url, args.folder_id, args.title)
    elif args.command == "remote-upload-list":
        result = api.remote_upload_list()
    elif args.command == "remote-upload-status":
        result = api.remote_upload_status(args.file_code)
    elif args.command == "remote-upload-slots":
        result = api.remote_upload_slots()
    elif args.command == "remote-upload-actions":
        result = api.remote_upload_actions(args.action, args.file_code)
    elif args.command == "create-folder":
        result = api.create_folder(args.name, args.parent_id)
    elif args.command == "rename-folder":
        result = api.rename_folder(args.folder_id, args.name)
    elif args.command == "list-contents":
        result = api.list_contents(args.folder_id)
    elif args.command == "list-files":
        result = api.list_files(args.page, args.per_page, args.folder_id)
    elif args.command == "file-status":
        result = api.file_status(args.file_code)
    elif args.command == "file-info":
        result = api.file_info(args.file_code)
    elif args.command == "file-image":
        result = api.file_image(args.file_code)
    elif args.command == "rename-file":
        result = api.rename_file(args.file_code, args.title)
    elif args.command == "move-file":
        result = api.move_file(args.file_code, args.folder_id)
    elif args.command == "search":
        result = api.search_files(args.search_term)

    if result:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
