#include "lists.h"

/**
 * get_pos - value of element in list at given index.
 * @head: given list.
 * @at: given index.
 *
 * Return: value of index, at fail -1.
 */
int get_pos(listint_t *head, int at)
{
	int n = 0;

	while (head)
	{
		if (n == at)
			return (head->n);
		head = head->next;
		n++;
	}

	return (-1);
}

/**
 * lits_len - get lengh of list
 * @head: given list
 *
 * Return: size of list
 */
int lits_len(listint_t *head)
{
	int n = 0;

	while (head)
	{
		head = head->next;
		n++;
	}

	return (n);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: given list
 *
 * Return: 1 if is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int n = 0, at = 0, X[1000];
	listint_t *tmp;

	if (!head)
		return (1);

	tmp = *head;

	while (tmp)
	{
		X[n] = tmp->n;
		n++;
		tmp = tmp->next;
	}
	
	tmp = *head;
	while (tmp)
	{
		if (tmp->n != X[n - at - 1])
			return (0);

		at++;
		tmp = tmp->next;
	}

	return (1);
}
