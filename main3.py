

def read_all_json_files(folder_path="htmls"):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:

    data = list(set(data))
    return data