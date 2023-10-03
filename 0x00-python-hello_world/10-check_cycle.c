#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in
 * the singly linked list
 * @list: argument
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	/* Slow pointer */
	listint_t *s = list;
	/* Fast pointer */
	listint_t *f = list;

	while (f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}
	return (0);
}
