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
	listint_t *temp;
	listint_t *temp2;

	if (!list)
	{
		return (0);
	}
	temp = list->next;
	temp2 = list;

	while (temp && temp->next && temp2)
	{
		if (temp2 == temp)
		{
			return (1);
		}
		temp2 = temp2->next;
		temp = temp->next->next;
	}
	return (0);
}
