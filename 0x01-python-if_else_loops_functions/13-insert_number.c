#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the pointer of head
 * @number: the new numbwer to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL || !number)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;

	while (current != NULL)
	{
		if (number <= (current->next)->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (new);
}
