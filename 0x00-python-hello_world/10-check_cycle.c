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
	if (list == NULL)
		return (1);
	listint_t *temp = list;

	while (list->next != NULL && temp->next->next != NULL)
	{
		if (list == temp)
		{
			return (1);
		}
		else
		{
			list = list->next;
			temp = temp->next;
		}
	}
	return (1);
}
