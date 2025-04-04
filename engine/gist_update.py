import os
import requests

GIST_ID = os.environ["GIST_ID"]
GIST_TOKEN = os.environ["GIST_TOKEN"]
SOURCE_FILE = "scope/rijksoverheid.txt"
TARGET_FILENAME = "scope.txt"

def update_gist():
    if not os.path.exists(SOURCE_FILE):
        print(f"❌ File not found: {SOURCE_FILE}")
        return

    with open(SOURCE_FILE, "r") as f:
        content = f.read()

    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {
        "Authorization": f"Bearer {GIST_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    get_response = requests.get(url, headers=headers)
    current_content = get_response.json()['files'].get(TARGET_FILENAME, {}).get('content', '')
    if current_content.strip() == content.strip():
        print("ℹ️ No changes in content. Skipping update.")
        return

    response = requests.patch(url, json={"files": {
        TARGET_FILENAME: {"content": content}
    }}, headers=headers)

    if response.status_code == 200:
        print("✅ Gist updated successfully")
    else:
        print(f"❌ Failed to update Gist: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    update_gist()
