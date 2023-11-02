#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	while (current != NULL)
	{
		current = current->next; 
		if (current == list)
		{
			return (1);
		}
	}
	free(current);
	return (0);
}