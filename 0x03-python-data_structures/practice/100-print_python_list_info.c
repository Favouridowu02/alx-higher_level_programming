#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a C function that prints some basic info
 * about Python lists
 * @p: the object
 */
void print_python_list_info(PyObject *p)
{
	size_t list_size, i, a;
	
	i = 0;
	list_size = PyList_Size(p);
	a = (((PyListObject *) p)->allocated);
	PyObject *obj;
	
	printf("[*] Size of the Python List = %zu\n", list_size);
	printf("[*] Allocated = %zu\n", a);

	while (i < list_size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
