#include<stdio.h>
#include "lists.h"
#include<stdlib.h>
/**
 * check_cycle - function
 * @list: pointer
 * Return: 0 or 1
 */


int check_cycle(listint_t *list)
{
	listint_t *temp = list->next;
	listint_t *temp2 = list;

	if (list == NULL)
	{
		return (0);
	}

	while (temp != NULL && temp->next != NULL && temp2 != NULL)
	{
		if (list == temp)
		{
			return (1);
		}
		else
		{
			temp2 = list->next;
			temp = temp->next->next;
		}
	}
	return (0);
}
