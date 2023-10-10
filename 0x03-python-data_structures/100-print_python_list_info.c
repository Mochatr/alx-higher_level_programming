#include <Python.h>

/**
 * print_python_list_info - function
 * @p: parameter
 */

void print_python_list_info(PyObject *p)
{
	int list_size, allocated_size, i;
	PyObject *list_item;

	list_size = Py_SIZE(p);
	allocated_size = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", allocated_size);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: ", i);

		list_item = PyList_GelItem(p, i);
		printf("%s\n", Py_TYPE(list_item)->tp_name);
	}
}
