#include "lists.h"

/**
 * insert_node - insert number in sorted linked list.
 * @head: start of list.
 * @number: number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *prev = NULL, *at = *head;

	if (!head)
		return (NULL);

	tmp = malloc(sizeof(listint_t));

	if (!tmp)
		return (NULL);

	tmp->n = number;
	tmp->next = NULL;

	if (!(*head))
		return (tmp);

	if ((*head)->n >= number)
	{
		tmp->next = *head;
		return (tmp);
	}

	while (at)
	{
		if (at->n >= number)
			break;

		prev = at;
		at = at->next;
	}

	prev->next = tmp;
	tmp->next = at;

	return (*head);
}
