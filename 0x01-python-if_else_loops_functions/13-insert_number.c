#include "lists.h"

/**
 * insert_node - insert a new node
 * @head: head of the linked list
 * @number: data to linked list
 *
 * Return: adress of the new node created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *h = NULL, *hback = NULL;

	h = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (h != NULL)
	{
		if (h->n > number)
			break;
		hback = h;
		h = h->next;
	}
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			hback->next = new;
	}
	return (new);
}
