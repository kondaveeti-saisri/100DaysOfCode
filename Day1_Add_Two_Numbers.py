
---

## 💡 Solution Approach

- Use a **dummy node** to build the result linked list.
- Iterate through both lists while considering **carry** from the previous step.
- Extract values from `l1` and `l2` (use 0 if they don’t exist).
- Compute `sum = val1 + val2 + carry`, store last digit, update carry.
- Move to the next nodes in both linked lists.
- Return the `dummy.next`, which points to the result.

---

## 🖥️ Code Implementation

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
