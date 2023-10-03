#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a node into a sorted list
 * @head: parameter
 * @number: parameter
 * Return: The node inserted
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
