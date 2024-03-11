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
	listint_t *temp = list;

	while (list->next != NULL && temp->next->next != NULL)
	{
		if (list->next == temp->next)
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
