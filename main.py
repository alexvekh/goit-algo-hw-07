# повний код роботи з AVL-деревом.

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# ---- Завдання 1. ----  найбільше значення ---------------------------------
def max_val(root, max_value=float('inf')):
    if root:
        if root.right:
            max_value = max_val(root.right)
        else:
            max_value = root.key
    return max_value

# # найбільше значення (only print, no return)
# def max_val(root):
#     if root:
#         if root.right:
#             max_val(root.right)
#         else:
#             print("Найбільше значення:", root.key)
#             return root.key   # Return None
        

# ---- Завдання 2. ----  найменше  значення ---------------------------------
def min_val(root, min_value=-float('inf')):
   
    if root:
        if root.left:
            min_value = min_val(root.left, min_value)
        else:
            print("Найменше значення:", root.key)
            min_value = root.key
    return min_value

# # найменше  значення (only print, no return)
# def min_val(root):
#     if root:
#         if root.left:
#             min_val(root.left)
#         else:
#             print("Найменше значення:", root.key)
#             return root.key   # Return None


# ---- Завдання 3. ----  суму всіх значень  ---------------------------------
def sum(root, sum_val=0):   
    if root:
            sum_val =  root.key + sum(root.left, sum_val) + sum(root.right, sum_val)
    return sum_val

# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)

print("Найбільше значення:", max_val(root))
print("Найменше значення:", min_val(root))
print("Сума значеннь:", sum(root))

# # Delete
# keys_to_delete = [10, 27]
# for key in keys_to_delete:
#     root = delete_node(root, key)
#     print("Видалено:", key)
#     print("AVL-Дерево:")
#     print(root)