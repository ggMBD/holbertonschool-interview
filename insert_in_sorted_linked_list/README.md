# Insert in Sorted Linked List

## Description
This project implements a function that inserts a new node into a sorted singly linked list of integers.

The list is sorted in ascending order and must remain sorted after insertion.

## Prototype
```c
listint_t *insert_node(listint_t **head, int number);
```

- `head`: address of the pointer to the first node of the list.
- `number`: value to insert.
- Return: address of the new node, or `NULL` on failure.

## Data Structure
Defined in `lists.h`:

```c
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
```

## Files
- `0-insert_number.c`: implementation of `insert_node`.
- `linked_lists.c`: helper functions (`print_listint`, `add_nodeint_end`, `free_listint`).
- `lists.h`: structure and function prototypes.
- `0-main.c`: sample test file.

## Compilation
```bash
gcc -Wall -Werror -Wextra -pedantic 0-main.c linked_lists.c 0-insert_number.c -o insert
```

## Usage
```bash
./insert
```

## Example Output
```text
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
```

## Algorithm Summary
1. Create a new node containing `number`.
2. If the list is empty, make the new node the head.
3. If `number` is smaller than the current head value, insert at beginning.
4. Otherwise, traverse until the correct insertion point is found.
5. Relink pointers so the new node is inserted while keeping ascending order.

## Notes
- The input list is assumed to be already sorted in ascending order.
- Memory allocation is checked and `NULL` is returned if allocation fails.
