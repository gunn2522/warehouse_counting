from collections import defaultdict, deque

# Track inventory count by item label
inventory_map = defaultdict(int)

# Track flow events (FIFO queue)
flow_queue = deque()

# Organize items into categories
category_tree = defaultdict(list)

def update_inventory(label, action, qty=1):
    if action == 'IN':
        inventory_map[label] += qty
    elif action == 'OUT':
        inventory_map[label] -= qty

    flow_queue.append((label, action, qty))

    if label not in category_tree:
        category_tree[label.split("_")[0]].append(label)

    return inventory_map[label]
