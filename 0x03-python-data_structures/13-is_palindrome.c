#include "lists.h"

/**
 * is_palindrome - Entry point
 * @head: parameter
 * Return: Value
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (checkfor_palindrome(head, *head));
}

/**
 * checkfor_palindrome - Checks if a linked list is a palindrome
 * @head: head of the list
 * @end: end of the list
 * Return: Value
 */

int checkfor_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (checkfor_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
