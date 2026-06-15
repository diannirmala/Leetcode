from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next

    print()


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        print("\n=== LIST AWAL ===")
        print_linked_list(head)

        if not head.next:
            print("\nHanya ada 1 node.")
            print("Menghapus node tersebut.")
            return None

        slow = head
        fast = head
        prev = None

        step = 1

        print("\n=== MULAI MENCARI TENGAH ===")

        while fast and fast.next:

            print(f"\n--- Iterasi {step} ---")

            print(
                f"Sebelum bergerak:"
                f"\nprev = {prev.val if prev else None}"
                f"\nslow = {slow.val}"
                f"\nfast = {fast.val}"
            )

            prev = slow
            slow = slow.next
            fast = fast.next.next

            print(
                f"\nSetelah bergerak:"
                f"\nprev = {prev.val}"
                f"\nslow = {slow.val}"
                f"\nfast = {fast.val if fast else None}"
            )

            step += 1

        print("\n=== LOOP SELESAI ===")
        print(f"prev berada di node: {prev.val}")
        print(f"slow berada di node tengah: {slow.val}")

        print("\nMenghapus node tengah...")
        print(f"prev.next = slow.next")
        print(f"{prev.val}.next = {slow.next.val if slow.next else None}")

        prev.next = slow.next

        print("\n=== HASIL AKHIR ===")
        print_linked_list(head)

        return head


# ==========================
# TEST CASE
# ==========================

head = build_linked_list([1, 3, 4, 7, 1, 2, 6])

sol = Solution()
sol.deleteMiddle(head)