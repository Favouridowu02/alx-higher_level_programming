#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next =  NULL;
	current = *head;

	while (current != NULL)
	{
		if (current->n < number && current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		else
		{
			current = current->next;
		}
	}
	return (new);
}
