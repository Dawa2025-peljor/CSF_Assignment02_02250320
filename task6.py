def process_keyword_queue(keyword):
    queue = list(keyword)          # enqueue all characters
    print("Queue Processing:")
    while queue:
        ch = queue.pop(0)          # dequeue from front
        print(f"Processing: Analyse {ch}")