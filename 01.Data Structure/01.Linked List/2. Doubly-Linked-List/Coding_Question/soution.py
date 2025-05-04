# Python program to find a pair with given sum x
# using map
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def findPairsWithGivenSum(target, head):
    ans = []
    visited = set()
    currNode = head

    # Traverse the doubly linked list
    while currNode is not None:
        x = target - currNode.data

        # Check if the target exists in the visited set
        if x in visited:
          
            # Pair found, add it to the answer
            ans.append([x, currNode.data])

        # Add the current node's value to the visited set
        visited.add(currNode.data)
        currNode = currNode.next

    # Sort the pairs by the first element of the pair
    ans.sort(key=lambda pair: pair[0])

    return ans

# Helper function to create a linked list
def create_linked_list(values):
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


if __name__ == "__main__":
  
    # Create a doubly linked list: 1 -> 2 -> 4 -> 5
    values = [1, 2, 4, 5]
    head = create_linked_list(values)

    target = 7
    pairs = findPairsWithGivenSum(target, head)

    if not pairs:
        print("No pairs found.")
    else:
        for pair in pairs:
            print(pair[0], pair[1])
