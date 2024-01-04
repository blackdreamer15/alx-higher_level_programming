#include "lists"

/**
 * insert_node - Write a function in C that inserts a number into a sorted
 * singly linked list.
 * @head: Head of the linked list
 * @number: Number to be inserted to node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = NULL;

	current = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || new_node->n < current->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL && (current->n < new_node->n)
		&& ((current->next)->n < new_node->n))
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
