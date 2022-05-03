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
	listint_t *data = NULL, *h = NULL, *hnew = NULL;

	h = *head;
	data = malloc(sizeof(listint_t));
	if (data == NULL)
		return (NULL);
	while (hnew != NULL)
	{
		if (h->n > number)
			break;
		h = hnew;
		hnew = hnew->next;
	}
	data->n = number
	if (*head == NULL)
	{
		data->next = NULL;
		*head = data;
	}
	else
	{
		data->next = hnew;
		if (h == *head)
			*head = data;
		else
			h->next = data;
	}
	return (data);
}
