#include<stdlib.h>
#include "lists.h"

/**
 * insert_node - function
 * @head: pointer to pointer
 * @number: integer
 * Return: address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *curr_node = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (curr_node == NULL || curr_node->n >= number)
	{
		newNode->next = curr_node;
		*head = newNode;
		return (newNode);
	}

	while (curr_node && curr_node->next && curr_node->next->n < number)
		curr_node = curr_node->next;

	newNode->next = curr_node->next;
	curr_node->next = newNode;

	return (newNode);
}
