#include "lists.h"

/**
 * is_palindrome - a function in C that checks if a singly linked
 * list is a palindrome.
 * @head: a pointer to the pointer of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int table[1024];
	listint_t *current;
	int i = 0;
	int check = 0;

	current = *head;
	while (current != NULL)
	{
		table[i] = current->n;
		i++;
		current = current->next;
	}
	if (i % 2 == 0)
	{
		int k = i / 2;

		for (int n = 0; n <= k; n++, i--)
		{
			if (table[n] == table[i])
				check = 1;
			else
				check = 0;
		}
	}
	return (check);
}
