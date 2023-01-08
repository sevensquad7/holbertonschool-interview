#include "search_algos.h"

/**
 * binary_search - function that searches for a value in a sorted array
 * of integers using the Binary search algorithm
 * @array: in array task
 * @size: size of the array
 * @value: value to compare
 * Return: Every time you compare a value in the array to the value
 * you are searching, you have to print this value (see example below)
 */
int advanced_binary(int *array, size_t size, int value)
{
	int medium = 0, i = 0, j = 0;
	int top = size - 1;

	if (array == NULL)
		return (-1);

	while (i <= top)
	{
		printf("Searching in array : ");
		for (j = i; j < top; j++)
			printf("%d, ", array[j]);
		printf("%d\n", array[j]);

		medium = (top + i) / 2;

		if (array[medium] == value)
		{
			return (medium);
		}
		if (array[medium] < value)
		{
			i = medium + 1;
		}
		else
		{
			top = medium - 1;
		}
	}
	return (-1);
}
