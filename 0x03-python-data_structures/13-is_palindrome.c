#include "lists.h"
/**
 * is_palindrome - function
 * @head: pointer
 * Return: 0 0r 1
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->data != slow->data)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
