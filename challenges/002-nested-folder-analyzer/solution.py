def analyze_directory(directory: dict) -> tuple[int, int]:
    
    file_count = 0
    total_size = 0

    for value in directory.values():
        if isinstance(value, int):
            total_size += value
            file_count += 1
        elif isinstance(value, dict):
            count, size = analyze_directory(value)
            file_count += count
            total_size += size


    
    return file_count, total_size



directory = {
    "a.txt": 100,
    "documents": {
        "resume.pdf": 200,
        "essay.txt": 150
    }
}

print(analyze_directory(directory))